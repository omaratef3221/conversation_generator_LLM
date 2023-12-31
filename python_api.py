from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
sys.path.append("..")
import chatting

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

@app.route('/generate', methods=['POST'])
def process_input():
    data = request.json
    input_text = data['text']
    button_label = data['button']

    # Process the input here
    # response_text = f"Processed {input_text} using {button_label}"

    response_text = chatting(input_text, button_label)
    return jsonify(response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
