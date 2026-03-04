import requests
from config import BOARDS

def deploy_to_board(name):
    url = BOARDS[name]["url"]
    print(f"🔄 Deploying to {name}...")
    
    try:
        response = requests.post(
            f"{url}/deploy",
            json={"firmware_version": "v2.0.0"}
        )
        result = response.json()
        
        if result["status"] == "success":
            BOARDS[name]["deploy"] = "success"
            print(f"✅ {name}: SUCCESS")
        else:
            BOARDS[name]["deploy"] = "failed"
            BOARDS[name]["error"] = result["error"]
            print(f"❌ {name}: FAILED — {result['error']}")
    
    except Exception as e:
        BOARDS[name]["deploy"] = "failed"
        BOARDS[name]["error"] = str(e)
        print(f"❌ {name}: CRASHED — {e}")

def run_deployments():
    print("=== Deployment Orchestrator ===")
    for name in BOARDS:
        deploy_to_board(name)
    
    success = [n for n in BOARDS if BOARDS[n]["deploy"] == "success"]
    failed = [n for n in BOARDS if BOARDS[n]["deploy"] == "failed"]
    print(f"\n✅ Deployed: {len(success)}")
    print(f"❌ Failed: {len(failed)}")