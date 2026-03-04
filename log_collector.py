import requests
from config import BOARDS

def collect_logs(name):
    url = BOARDS[name]["url"]
    print(f"📋 Collecting logs from {name}...")
    
    try:
        response = requests.get(f"{url}/logs")
        result = response.json()
        print(f"📋 {name} logs: {result['logs']}")
        return result["logs"]
    
    except Exception as e:
        print(f"❌ Could not collect logs from {name}: {e}")
        return []

def collect_failed_logs():
    print("\n=== Log Collector ===")
    for name in BOARDS:
        if BOARDS[name]["deploy"] == "failed" or BOARDS[name]["validation"] == "failed":
            collect_logs(name)
        else:
            print(f"⏭️  Skipping {name} — no failures")