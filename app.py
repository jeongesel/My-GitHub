from flask import Flask, request
from flask_cors import CORS
from dotenv improt load_dotenv
from assistant import callchat
load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def chatbot():
  if request.method == 'POST':
    messages = request.get_json()
    if 'message' = messages['message']
    result = callchat(user-message)
    return result
    return "message not found", 400


if __name__ '__main__':
app.run(host='0.0.0.0', port=1234) 
