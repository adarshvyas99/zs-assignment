from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-ansible', methods=['GET'])
def run_ansible():
    result = subprocess.run(["ansible-playbook", "-i", "inventory/hosts.yml", "playbooks/site.yml"], capture_output=True, text=True)
    return jsonify({"status": "success", "output": result.stdout})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
