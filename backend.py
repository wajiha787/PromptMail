from flask import Flask, request, jsonify
import openai
import os
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
@app.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    prompt = data['prompt']
    tone = data['tone']
    tone_instruction = "Write this email in a professional tone." if tone == "professional" else "Write this email in an informal tone."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{tone_instruction} {prompt}",
        max_tokens=150
    )
    email = response['choices'][0]['text'].strip()
    return jsonify({"email": email})

if __name__ == '__main__':
    app.run(debug=True)
