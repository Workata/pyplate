from unittest.mock import MagicMock, patch

from pyplate.main import main


@patch("builtins.print")
def test_main_logic(mock_print: MagicMock) -> None:
    main()
    mock_print.assert_any_call("Hello python!")
