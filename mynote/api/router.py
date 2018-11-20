from flask import Blueprint, request
import markdown
from mynote.api import mode
from mynote.api.util import success, fail

api_blue = Blueprint('api', __name__, url_prefix='/api')


@api_blue.route('/articles', methods=['GET'])
def getArticles():
    result = []
    notes = mode.list_notes()
    for note in notes:
        result.append({'id':note[0], 'title':note[1], 'content':note[2]})
    return success(result)


@api_blue.route('/articles', methods=['POST'])
def addArticles():
    data = request.get_json()
    id = data['id']
    title = data['title']
    content = data['content']
    if title == '':
        return fail('title is None')

    if content == '':
        return fail('content is None')

    if id == '':
        mode.add_note(title, content)
    else:
        mode.update_note(id, title, content)
    return success()


@api_blue.route('/articles/<int:id>', methods=['DELETE'])
def deleteArticles(id):
    mode.delete_note(id)
    return success()


@api_blue.route('/articles/markdown/<int:id>', methods=['GET'])
def getMkrticles(id):
    note = mode.get_note(id)
    content = note[2]
    html = markdown.markdown(content,extensions=['markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.tables'])
    return success({'html':html})






