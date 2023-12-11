from flask import request, jsonify,Blueprint
from dotenv import load_dotenv
import pickle
from core.generator import generate



load_dotenv()
text_bp = Blueprint("text_suggestion",__name__)
file_pointer = open("model/text_suggestion_model","rb")
recomender = pickle.load(file_pointer)
file_pointer.close()

#ROUTE TO SUGGEST TEXT FOR THE GIVEN INPUT DATA
@text_bp.route("/suggest_text",methods = ['GET'])
def suggest():
    data = request.args.get("data")
    if data != None:
        suggestion_text = generate( recomender,max=2,start = tuple(data.split()))
        return jsonify({"suggestion":suggestion_text }),200
    else:
        return jsonify({"error":"UNPROCESSABLE INPUT PLEASE GIVE SOME VALID INPUT DATA"}),422


