
##4

from flask import Flask, jsonify

app = Flask(__name__)
task_status = {}  # {task_id: "running"/"completed"/"failed"}

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(task_status)

@app.route('/update_task', methods=['POST'])
def update_task():
    data = request.json
    task_status[data["task_id"]] = data["status"]
    return jsonify({"message": "Updated"})
