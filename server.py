import openai
from flask import Flask, request, jsonify, render_template

# Set your OpenAI API key here
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"User: {user_input}\nAI:",
        max_tokens= 1000
    )
    ai_response = response.choices[0].text.strip()
    return jsonify({"ai_response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)