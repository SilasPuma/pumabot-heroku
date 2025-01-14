from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    event = request.json

    # Check if the event is a message
    if event.get("type") == "MESSAGE":
        user_message = event["message"]["text"]
        
        # Respond based on user message
        response = {
            "text": f"You said: {user_message}. How can I assist you further?"
        }
        return jsonify(response)

    # Default response for non-message events
    return jsonify({"text": "This bot only handles messages."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
