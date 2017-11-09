#!/usr/bin/python3
import subprocess
from flask import Flask, jsonify, request
app = Flask(__name__)
updateCommands=["git stash", "git pull"]
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
    lang = [lang for lang in langs if lang['name'] == name]
    if len (lang) > 0:
        lang = lang[0]
    return jsonify({'lang' : lang})
            
@app.route('/langs', methods=['POST'])
def addlang():
    lang = { 'name' : request.json['name'], 'pros' : request.json['pros'], 'cons' : request.json['cons'] }
    if len([tlang for tlang in langs if tlang['name'] == lang['name']]) == 0:
        langs.append(lang)
    return jsonify({'langs' : langs})
@app.route('/pull', methods=['GET'])
def update():
    responses = []
    for command in updateCommands:
        response = {}
        response['NAME'] = command
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if output != None:
            out = output.decode()
            print ("OUT", out)
            response['OUT'] = out
            if error != None:
                err = error.decode()
                print("ERROR", err)
                response['ERROR'] = err
            else:
                response['ERROR'] = ""
        else:
            response['OUT'] = ""
        responses.append(response)
    return jsonify({'responses' : responses})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)

