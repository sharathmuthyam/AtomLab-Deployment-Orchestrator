from config import BOARDS
from deployer import run_deployments
from validator import run_validation
from log_collector import collect_failed_logs
from report_generator import generate_report
import json 
from github_notifier import send_to_github




def run_pipeline():
    print("🚀 Starting AtomLab Deployment Pipeline...")

    run_deployments()
    run_validation()
    collect_failed_logs()
    generate_report()
    
    # 3. Decision Logic: Should we notify GitHub?
    try:
        with open("failure_report.json", "r") as f:
            data = json.load(f)
            
        # If your file is a list, grab the last one. If a dict, use it directly.
        latest_report = data[-1]

        if len(latest_report["failures"]) > 0:
            print(f"🚨 {len(latest_report['failures'])} failures found. Triggering GitHub Notifier...")
            send_to_github(latest_report) # Call the function directly
        else:
            print("✅ Deployment successful. No notification required.")
            
    except Exception as e:
        print(f"❌ Error during orchestration logic: {e}")

if __name__ == "__main__":
    run_pipeline()
    print("\n=== Final Board States ===")
    for name, data in BOARDS.items():
        print(f"  {name}: {data}")