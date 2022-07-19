from flask import Flask, render_template, request
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import torch

app = Flask(__name__)


with open('data.txt', 'r') as file:
    data = file.read().replace('\n', '')

model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    QA_input = {
    'question': userText,
    'context': data
    }
    res=nlp(QA_input)
    
    return res['answer']


if __name__ == "__main__":
    app.run()


