from flask import Flask
from dotenv import load_dotenv
from views.suggest_text import text_bp

app = Flask(__name__)
app.register_blueprint(text_bp)  #CREATING BLUEPRINT FOR TEXT SUGGESTIN VIEW

if __name__ == '__main__':
    app.run(debug=True)