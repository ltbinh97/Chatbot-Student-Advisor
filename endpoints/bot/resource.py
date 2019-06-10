from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from app import db



class BotResource(Resource):
    def get(self, ques = None):
        ques = "Question: " + ques 
        # // function QNA(ques)
        # // return ans
        ans = "Ans: answer"
        result = ques + " - " + ans
        return  result
        