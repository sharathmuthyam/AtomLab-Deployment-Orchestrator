import pytest
from unittest.mock import patch, MagicMock
from config import BOARDS
from deployer import deploy_to_board

def test_deploy_to_board():
    BOARDS["board_1"]["deploy"] = None
    BOARDS["board_1"]["error"] = None

    board_1 = "board_1"
    mock = MagicMock()

    mock.json.return_value = {"status" : "success", "firmware":"V2.0.0"}

    with patch("deployer.requests.post",return_value = mock):
        deploy_to_board(board_1)
        assert BOARDS[board_1]["deploy"] == "success"
        
def test_deploy_to_board_fail():
    BOARDS["board_1"]["deploy"] = None
    BOARDS["board_1"]["error"] = None

    board_1 = "board_1"
    mock = MagicMock()

    mock.json.return_value = {"status" : "failed", "firmware":"V2.0.0"}

    with patch("deployer.requests.post",return_value = mock):
        deploy_to_board(board_1)
        assert BOARDS[board_1]["deploy"] == "failed"

def test_deploy_to_board_network_error():
    BOARDS["board_1"]["deploy"] = None
    BOARDS["board_1"]["error"] = None

    board_1 = "board_1"
    mock = MagicMock()

    with patch("deployer.requests.post", side_effect = Exception("network down")):
        deploy_to_board(board_1)
        assert BOARDS[board_1]["deploy"] == "failed"
        assert "network down" in BOARDS[board_1]["error"]

