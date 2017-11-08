#!/usr/local/bin/python3

from flask import Flask, jsonify, request
app = Flask(__name__)

langs=[
        {'name':'Python', 'pros' : 'easy', 'cons' : 'high-level'}, 
        {'name':'C++', 'pros' : 'fast', 'cons' : 'hard'}, 
        {'name':'java', 'pros': 'best of both', 'cons' : 'stoopid'}
        ]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'It Works!'})
@app.route('/langs', methods=['GET'])
def returnlangs():
    return jsonify({'langs' : langs})
@app.route('/langs/<string:name>', methods=['GET'])
def returnlang(name):
    return jsonify({'lang': [lang for lang in langs if lang['name'] == name][0] })
@app.route('/langs', methods=['POST'])
def addlang():
    lang = { 'name' : request.json['name'], 'pros' : request.json['pros'], 'cons' : request.json['cons'] }
    if len([tlang for tlang in langs if tlang['name'] == lang['name']]) == 0:
        langs.append(lang)
    return jsonify({'langs' : langs})
if __name__ == '__main__':
    app.run(debug=True, port=8080)

