from config import BOARDS
from deployer import run_deployments
from validator import run_validation
from log_collector import collect_failed_logs
from report_generator import generate_report

if __name__ == "__main__":
    run_deployments()
    run_validation()
    collect_failed_logs()
    generate_report()
    
    print("\n=== Final Board States ===")
    for name, data in BOARDS.items():
        print(f"  {name}: {data}")