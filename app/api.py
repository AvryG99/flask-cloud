from flask import Flask, request, jsonify
from agent import LLM_Agent
from flask_cors import CORS
import os
from werkzeug.serving import WSGIRequestHandler

# Flask app
app = Flask(__name__)
CORS(app)

# Increase timeout to 5 minutes
WSGIRequestHandler.timeout = 300

# Database configuration
db_config = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': os.getenv('DB_SERVER'),
    'database': os.getenv('DB_DATABASE'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Initialize LLM Agent
agent = LLM_Agent(db_config)

@app.route('/flask/process_question', methods=['POST'])
def process_question():
    try:
        data = request.get_json()
        if 'question' not in data:
            return jsonify({"error": "Missing 'question' field in request"}), 400
        
        question = data['question']
        answer = agent.process_question(question)  # Gets the actual answer
        return jsonify({
            "question": question,
            "answer": answer
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flask/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running.'}), 200

@app.route('/flask/get_logs', methods=['GET'])
def get_logs():
    log_file_path = 'agent_log.log'
    try:
        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
        return jsonify({"logs": logs}), 200
    except FileNotFoundError:
        return jsonify({"error": "Log file not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flask/set_model', methods=['POST'])
def set_model():
    try:
        data = request.get_json()
        if 'model' not in data:
            return jsonify({"error": "Missing 'model' field in request"}), 400

        model = data['model']
        agent.set_gpt_model(model)
        return jsonify({"message": f"Model updated to {model}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flask/set_max_tokens', methods=['POST'])
def set_max_tokens():
    try:
        data = request.get_json()
        if 'max_tokens' not in data:
            return jsonify({"error": "Missing 'max_tokens' field in request"}), 400

        max_tokens = int(data['max_tokens'])
        agent.set_max_tokens(max_tokens)
        return jsonify({"message": f"Max tokens updated to {max_tokens}"}), 200
    except ValueError:
        return jsonify({"error": "'max_tokens' must be an integer."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flask/set_temperature', methods=['POST'])
def set_temperature():
    try:
        data = request.get_json()
        if 'temperature' not in data:
            return jsonify({"error": "Missing 'temperature' field in request"}), 400

        temperature = float(data['temperature'])
        agent.set_temperature(temperature)
        return jsonify({"message": f"Temperature updated to {temperature}"}), 200
    except ValueError:
        return jsonify({"error": "'temperature' must be a float."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
