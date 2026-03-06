from flask import Flask, jsonify, request
import random
import sys
import datetime

app = Flask(__name__)

board_state = {
    "board_name": None,
    "firmware_version": None,
    "status": "idle",
    "logs": []
}

@app.route("/deploy", methods=["POST"])
def deploy():
    firmware = request.json.get("firmware_version")
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    board_state["logs"].append(f"[{timestamp}] Received firmware: {firmware}")
    
    if random.random() > 0.3:
        board_state["firmware_version"] = firmware
        board_state["status"] = "booting"
        board_state["logs"].append(f"[{timestamp}] Firmware transferred, booting...")
        return jsonify({"status": "success", "firmware": firmware})
    else:
        board_state["status"] = "failed"
        error = random.choice([
            "SSH connection timeout",
            "OS busy - cannot accept firmware",
            "Board rebooted mid-deploy"
        ])
        board_state["logs"].append(f"[{timestamp}] Transfer FAILED: {error}")
        return jsonify({"status": "failed", "error": error})

@app.route("/status", methods=["GET"])
def status():
    if board_state["status"] == "booting":
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        if random.random() > 0.1:
            board_state["status"] = "running"
            board_state["logs"].append(f"[{timestamp}] Boot SUCCESS")
        else:
            board_state["status"] = "boot_failed"
            board_state["logs"].append(f"[{timestamp}] Boot FAILED")
    
    return jsonify({
        "board_name": board_state["board_name"],
        "board_status": board_state["status"],
        "firmware_version": board_state["firmware_version"]
    })

@app.route("/logs", methods=["GET"])
def logs():
    return jsonify({
        "board_name": board_state["board_name"],
        "logs": board_state["logs"]
    })

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    board_name = sys.argv[2] if len(sys.argv) > 2 else f"board_{port}"
    board_state["board_name"] = board_name
    print(f"🔌 {board_name} starting on port {port}")
    app.run(port=port,debug=True)