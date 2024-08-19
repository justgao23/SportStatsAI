from flask import Flask, request, jsonify
import openai
import requests

app = Flask(__name__)
openai.api_key = 'your_openai_api_key'

@app.route('/player-stats', methods=['POST'])
def player_stats():
    user_query = request.json['query']
    
    # Step 1: Use ChatGPT to process the query
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"User asked: '{user_query}'. Provide the relevant basketball statistics.",
        max_tokens=150
    )
    
    gpt_answer = response.choices[0].text.strip()

    # Step 2: Parse the GPT response (assuming it's structured)
    # Here you would parse the response, fetch data from your database/API, and return it.
    
    return jsonify({"answer": gpt_answer})

if __name__ == '__main__':
    app.run(debug=True)
