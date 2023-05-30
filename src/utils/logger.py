from pathlib import Path
from datetime import date, datetime


class Logger:
    """
    Use python built in logger instead:
    https://docs.python.org/3/library/logging.html
    """

    LOGS_ROOT_FOLDER = "logs"

    def __init__(self, logs_location: str):
        self._logs_location = logs_location
        self._setup_path()

    def info(self, msg: str) -> None:
        self._insert_log(type_tag="INFO", msg=msg)

    def warning(self, msg: str) -> None:
        self._insert_log(type_tag="WARNING", msg=msg)

    def error(self, msg: str) -> None:
        self._insert_log(type_tag="ERROR", msg=msg)

    def _insert_log(self, type_tag: str, msg: str) -> None:
        current_time = self._get_current_time()
        log_row = f"[{type_tag}][{current_time}] {msg}"
        self._write_log_row_to_file(log_row)

    def _write_log_row_to_file(self, log_row: str) -> None:
        day = self._get_current_day()
        with open(f"{self.LOGS_ROOT_FOLDER}/{self._logs_location}/{day}.log", mode="a", encoding="utf-8") as f:
            print(log_row)
            f.write(f"\n{log_row}")

    def _get_current_time(self) -> str:
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    def _setup_path(self) -> None:
        Path(f"{self.LOGS_ROOT_FOLDER}/{self._logs_location}").mkdir(parents=True, exist_ok=True)

    def _get_current_day(self) -> str:
        today = date.today()
        return today.strftime("%Y_%m_%d")
