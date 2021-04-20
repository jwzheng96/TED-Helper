from flask_restplus import Namespace, Resource
from flask import request
from maintenance import check_maintenance, not_under_maintenance


ted_api = Namespace('ted', description='ted related public interface')


def get_ted_handle():
    from app import db
    from controllers.crawl import Crawl
    ted_controller = Crawl(db)
    return ted_controller


@ted_api.route('/offset/<offset>')
@ted_api.param('offset', 'The TED offset')
@ted_api.response(404, 'TEDs not found')
@ted_api.response(400, 'Bad parameters')
class TedInfo(Resource):
    @ted_api.doc('share_ted')
    def put(self, offset):
        ted_handle = get_ted_handle()
        res, error_msg = ted_handle.add(offset)
        if res:
            return {"status": "ok", "code": 0, "message": "ted record added."}
        else:
            return {"status": "error", "code": 100, "message": error_msg}


@ted_api.route('/patch/<begin>/<end>/<offset>')
@ted_api.param('begin', 'The newest TED page number')
@ted_api.param('end', 'The oldest TED page number')
@ted_api.param('offset', 'The TED page offset, is default to 1')
@ted_api.response(404, 'TEDs not found')
@ted_api.response(400, 'Bad parameters')
class TedPatchInfo(Resource):
    @ted_api.doc('patch_share_ted')
    def put(self, begin, end, offset):
        ted_handle = get_ted_handle()
        res, error_msg = ted_handle.patch_add(begin, end, offset)
        if res:
            return {"status": "ok", "code": 0, "message": "ted record added."}
        else:
            return {"status": "error", "code": 100, "message": error_msg}

@ted_api.route('/retrieve/<id>/<s_id>')
@ted_api.param('id', 'The TED id')
@ted_api.response(404, 'TEDs not found')
@ted_api.response(400, 'Bad parameters')
class TedPatchInfo(Resource):
    @ted_api.doc('get_ted_content_by_id')
    def get(self, id, s_id):
        ted_handle = get_ted_handle()
        res = ted_handle.get_ted_by_id(id, s_id)
        if res:
            return res
        else:
            error_msg = "failed to get the ted!"
            return {"status": "error", "code": 100, "message": error_msg}

@ted_api.route('/retrieve/<word>')
@ted_api.param('word', 'The key word search')
@ted_api.response(404, 'TEDs not found')
@ted_api.response(400, 'Bad parameters')
class TedPatchInfo(Resource):
    @ted_api.doc('get_ted_content_by_word')
    def get(self, word):
        print(word)
        ted_handle = get_ted_handle()
        res = ted_handle.get_ted_by_id(word)
        if res:
            return res
        else:
            error_msg = "failed to get the ted!"
            return {"status": "error", "code": 100, "message": error_msg}

@ted_api.route('/retrieve/<word>')
@ted_api.param('word', 'The author name search')
@ted_api.response(404, 'TEDs not found')
@ted_api.response(400, 'Bad parameters')
class TedPatchInfo(Resource):
    @ted_api.doc('get_ted_content_by_name')
    def get(self, word):
        print(word)
        ted_handle = get_ted_handle()
        res = ted_handle.get_ted_by_name(word)
        if res:
            return res
        else:
            error_msg = "failed to get the ted!"
            return {"status": "error", "code": 100, "message": error_msg}