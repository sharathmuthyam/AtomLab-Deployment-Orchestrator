import requests
from config import BOARDS

def validate_board(name):
    url = BOARDS[name]["url"]
    print(f"🔍 Validating {name}...")
    
    try:
        response = requests.get(f"{url}/status")
        result = response.json()
        
        if result["board_status"] == "running":
            BOARDS[name]["validation"] = "passed"
            print(f"✅ {name}: validation PASSED")
        else:
            BOARDS[name]["validation"] = "failed"
            print(f"❌ {name}: validation FAILED — {result['board_status']}")
    
    except Exception as e:
        BOARDS[name]["validation"] = "failed"
        BOARDS[name]["error"] = str(e)
        print(f"❌ {name}: UNREACHABLE — {e}")

def run_validation():
    print("\n=== Validation Runner ===")
    for name in BOARDS:
        if BOARDS[name]["deploy"] == "success":
            validate_board(name)
        else:
            print(f"⏭️  Skipping {name} — deployment failed")