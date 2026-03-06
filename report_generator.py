import json
import datetime
from config import BOARDS
import uuid
import os

def generate_report():
    print("\n=== Failure Report ===")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    failures = []
    for name, data in BOARDS.items():
        if data["deploy"] == "failed" or data["validation"] == "failed":
            failures.append({
                "board": name,
                "deploy_status": data["deploy"],
                "validation_status": data["validation"],
                "error": data["error"]
            })
    
    report = {
        "report_id": str(uuid.uuid4())[:8], 
        "timestamp": timestamp,
        "total_boards": len(BOARDS),
        "failures": failures,
        "summary": f"{len(failures)} board(s) failed out of {len(BOARDS)}"
    }
    


# ... (keep your report dict logic the same) ...

    # REPLACE YOUR FILE OPEN LOGIC WITH THIS:
    filename = "failure_report.json"
    
    # 1. Load existing data as a list
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                history = json.load(f)
                if not isinstance(history, list): history = [history]
            except:
                history = []
    else:
        history = []

    # 2. Add the new report to the list
    history.append(report)

    # 3. Write it back using "w" to save the whole valid list
    with open(filename, "w") as f:
        json.dump(history, f, indent=4)
    
    print(json.dumps(report, indent=4))
    print(f"\n📄 Report saved to failure_report.json")