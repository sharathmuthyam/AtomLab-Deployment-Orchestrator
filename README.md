# AtomLab Deployment Orchestrator

A Python-based deployment orchestration system that automates firmware deployment across multiple AtomLab boards, runs post-deployment validation, collects logs on failure, and generates structured failure reports.

## Project Structure
```
├── board_server.py       # Flask server simulating a real AtomLab board
├── config.py             # Shared board configuration and state
├── deployer.py           # Deploys firmware to all boards via HTTP
├── validator.py          # Validates boards are running after deployment
├── log_collector.py      # Collects logs from failed boards
├── report_generator.py   # Generates structured failure report
└── orchestrator.py       # Runs the full pipeline end to end
```

## How It Works
```
orchestrator.py
    ├── deploy firmware to all boards
    ├── validate successfully deployed boards
    ├── collect logs from failed boards
    └── generate failure report
```

## Simulated Failure Modes

| Failure | Description |
|---|---|
| SSH connection timeout | Board unreachable |
| OS busy | Board cannot accept firmware |
| Board rebooted mid-deploy | Connection dropped |
| Boot failed | Firmware transferred but board failed to start |

## Run It Yourself
```bash
# terminal 1,2,3 — start board servers
python board_server.py 5001 board_1
python board_server.py 5002 board_2
python board_server.py 5003 board_3

# terminal 4 — run full pipeline
python orchestrator.py
```

## Sample Output
```
=== Deployment Orchestrator ===
✅ board_1: SUCCESS
❌ board_2: FAILED — OS busy
✅ board_3: SUCCESS

=== Validation Runner ===
✅ board_1: validation PASSED
⏭️  Skipping board_2 — deployment failed
✅ board_3: validation PASSED

=== Log Collector ===
📋 Collecting logs from board_2...

=== Failure Report ===
{
    "summary": "1 board(s) failed out of 3",
    "failures": [{"board": "board_2", "error": "OS busy"}]
}
```

## Tech Stack
Python | Flask | REST API | JSON | Git
