from unittest.mock import patch, MagicMock
from main import main


@patch("builtins.print")
def test_main_logic(mock_print: MagicMock) -> None:
    main()
    mock_print.assert_called_with("Hello python!")
