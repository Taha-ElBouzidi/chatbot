from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response
import time
time.clock = time.time
app = Flask(__name__)

chatbot = ChatBot(
    'clearBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.6
        }
    ],
    response_selection_method=get_most_frequent_response,
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)
