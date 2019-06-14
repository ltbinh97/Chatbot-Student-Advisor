from flask import json, jsonify, request
from app import app
from app import db
from app.models import Menu
from flask_restful import Resource, reqparse, request
from "./binhle/" import rnn_lstm_seq2seq.py
#region 
@app.route('/')
def home():
	return jsonify({ "status": "ok" })

@app.route('/menu')
def menu():
    today = Menu.query.first()
    if today:
        body = { "today_special": today.name }
        status = 200
    else:
        body = { "error": "Sorry, the service is not available today." }
        status = 404
    return jsonify(body), status
# endregion


@app.route('/bot', methods = ['POST'])
def bot():
    req_data = request.get_json()
    ques = req_data["message"]
    #region ADD BOT RESPONSE FUNCTION HERE
    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-

    print(predict('how are you ?'))
    #endregion
    




    answer =  ques +  "12323"
    return jsonify({ "answer": answer })
