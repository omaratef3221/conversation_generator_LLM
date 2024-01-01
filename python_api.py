from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
from chatting import *
import re

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

@app.route('/generate', methods=['POST'])
def process_input():
    data = request.json
    input_text = data['text']
    button_label = data['button']

    # Process the input here
    # response_text = f"Processed {input_text} using {button_label}"

    
    input_text = f'''
    generate conversation about {input_text}
    dialogue:\n
    '''
    print(button_label)
    model = 't5' if button_label == 'Generate w/ Flan-T5' else 'bloom'
    output = generate_conversation(input_text, model=model)
    output = re.sub(r'(?<!^)#Person', r'\n#Person', output).replace("\n", "<br>")
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
