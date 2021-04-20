# -*- coding: utf-8 -*-
import json
import os
import re
import requests
from bs4 import BeautifulSoup
import time
from controllers.base import Controller
from models.ted import TED
from sqlalchemy import desc, or_
from app import db

class Crawl(Controller):
    # def __init__(self, db):
    #     self.db = db
    #     self.name = 'TEDCrawl'
    #     self.allowed_domains = 'ted2srt.org'

    def get_ted_by_id(self, id, s_id):
        tedInfo = self.db.session.query(TED).filter(TED.id == id, TED.sentence_id == s_id).all()
        return Crawl.convert(tedInfo[0]) # tedInfo is a list but only has a record can be return

    def get_ted_by_name(self, name):
        tedInfo = self.db.session.query(TED).filter(TED.name == name).all()
        return Crawl.convert(tedInfo[0])

    def get_ted_by_id(self, word):
        tedInfo = self.db.session.query(TED).filter(TED.ted_content.like('%'+str(word)+'%')).all()
        print()
        result = []
        for each in tedInfo:
            print(100*'*')
            print(each)
            print(100 * '*')
            result.append(Crawl.convert(each))
        return result # tedInfo is a list but only has a record can be return

    #begin = 1, end = maxPageNum + 1, offset = 1
    def patch_add(self, begin, end, offset):
        begin = int(begin)
        end = int(end)
        offset = int(offset)
        for i in range(begin, end, offset):
            try:
                self.add(str(i))
            except:
                pass
        return True, None

    def add(self, offset):
        url = 'https://ted2srt.org/api/talks?offset=' + str(offset)
        response = requests.get(url)
        # soup = BeautifulSoup(resp.text, 'lxml') #lxml为解析器
        data = json.loads(response.text)

        for item in data:
            id = str(item.get('id'))
            image = item.get('image')
            filmedAt = item.get('filmedAt')
            slug = item.get('slug')
            ted_url = 'https://ted2srt.org/talks/'+slug
            publishedAt = item.get('publishedAt')
            if item.get('languages'):
                languages =  item.get('languages')[0]['languageCode']
            else:
                languages = ''
            name = item.get('name')
            description = item.get('description')
            mediaPad = item.get('mediaPad')
            mediaSlug = item.get('mediaSlug')

            author_name = name.split(":")[0]
            begin = name.find(author_name)
            title = (name[begin+len(author_name)+2:]).strip()

            print(("*" * 100))
            print(author_name)
            print(title)
            print(("*" * 100))

            if id:
                url = "https://ted2srt.org/api/talks/{}/transcripts/download/txt?lang=en".format(id)
                body = str(requests.get(url).content, encoding="utf-8-sig")
                print(body)
                if not body:
                    continue

            sentences = body.split(".")
            sentence_id = 0
            for sentence in sentences:
                if not sentence:
                    continue
                eachRecord = self.db.session.query(TED).filter(TED.id==id, TED.sentence_id==sentence_id).all()
                if not eachRecord:
                    ted = TED(
                        id=id,
                        sentence_id=sentence_id,
                        url=ted_url,
                        author_name=author_name,
                        ted_title=title,
                        ted_content=str(sentence.replace('\n', "") + "."),
                        total_content=body,
                        image=image,
                        add_timestamp=int(time.time()),
                        filmed_timestamp=filmedAt,
                        slug=slug,
                        published_timestamp=publishedAt,
                        languages=languages,
                        name=title,
                        description=description,
                        media_pad=mediaPad,
                        media_slug=mediaSlug
                    )
                    sentence_id += 1
                    self.db.session.add(ted)
                    self.db.session.commit()
                else:
                    pass

        
        return True, None
                # yield scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)

    @staticmethod
    def convert(ted):
        res = {
            "id": ted.id,
            "sentence_id":ted.sentence_id,
            "url": ted.url,
            "author_name": ted.author_name,
            "ted_title": ted.ted_title,
            "ted_content": ted.ted_content,
            "image": ted.image,
            "add_timestamp": ted.add_timestamp,
            "filmed_timestamp": ted.filmed_timestamp,
            "slug": ted.slug,
            "published_timestamp": ted.published_timestamp,
            "languages": ted.languages,
            "name": ted.name,
            "description": ted.description,
            "media_pad": ted.media_pad,
            "media_slug": ted.media_slug,
            "total_content":ted.total_content
        }
        return res