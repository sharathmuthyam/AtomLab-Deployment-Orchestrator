import json
import datetime
from config import BOARDS

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
        "timestamp": timestamp,
        "total_boards": len(BOARDS),
        "failures": failures,
        "summary": f"{len(failures)} board(s) failed out of {len(BOARDS)}"
    }
    
    with open("failure_report.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print(json.dumps(report, indent=4))
    print(f"\n📄 Report saved to failure_report.json")