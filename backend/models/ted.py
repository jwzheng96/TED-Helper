from sqlalchemy import PrimaryKeyConstraint

from app import db
import json

class TED(db.Model):
    __tablename__ = 'ted'

    id = db.Column(db.String(256))
    sentence_id = db.Column(db.Integer)
    url = db.Column(db.String(256))
    ted_content = db.Column(db.Text)
    total_content = db.Column(db.Text)
    author_name = db.Column(db.String(256))
    ted_title = db.Column(db.String(256))
    image = db.Column(db.String(256))
    add_timestamp = db.Column(db.String(256)) # add to DB timestamp
    filmed_timestamp = db.Column(db.String(256))
    slug = db.Column(db.String(256))
    published_timestamp = db.Column(db.String(256))
    languages =  db.Column(db.String(256))
    name = db.Column(db.String(256))
    description = db.Column(db.Text)
    media_pad = db.Column(db.Integer)
    media_slug = db.Column(db.String(256))

    __table_args__ = (
        PrimaryKeyConstraint('id', 'sentence_id'),
        {},
    )
    def get_author_and_title(self):
        return "author name: {}, ted title: {}".format((self.author_name, self.ted_title))

    def get_description(self):
        return self.description

    def get_content(self):
        return self.ted_content
