from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
import os

app = Flask(__name__)
load_dotenv()

@app.route('/generate-workout', methods=['GET'])
def load_workout():
    return render_template('index.html')

@app.route('/generate-workout', methods=['POST'])
def get_workout():
    data = request.form
    goal = data.get('goal')
    workout_type = data.get('workout_type')
    duration = data.get('duration')

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "developer", "content": "You are my personal fitness coach. You are to be tough but reasonable. I want the response to be well-listed, short, and consise."},
                {"role": "user", "content": f"I want to {goal} and I want a {workout_type} workout plan for {duration}."}
            ],
            max_tokens=100
        )
        print(response.choices[0].message)
        return jsonify({"workout_plan": response.choices[0]["message"]["content"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
