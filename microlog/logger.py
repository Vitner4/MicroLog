from pathlib import Path
from datetime import datetime
from .formatters import Formatter

class Logger:
    def __init__(self):
        self._path = Path("./microlog.log") # path to the log file
        self._logging = True # Logging operation status
        self._writing = False # status of the first log entry written to the file
        self._formatter = Formatter() # an instance of the Formatter class for formatting data into a log string

    @property
    def path(self):     
        return self._path

    @path.setter
    def path(self, value: str):
            self._path = Path(value)
            self._writing = False

    def enable(self):
        self._logging = True

    def disable(self):
        self._logging = False
        self._writing = False

    def info(self, message: str):
        self._log("INFO", message)

    def warning(self, message: str):
        self._log("WARNING", message)

    def error(self, message: str):
        self._log("ERROR", message)

    def _log(self, level: str, message: str):

        if self._logging:
            now = datetime.now()

            data = {
                "date": now,
                "date-short": now.strftime('%Y-%m-%d'),
                "level": level,
                "message": message
            }

            # Writing the log to a file
            with open(self.path, 'a', encoding='utf-8') as f:  

                # Header in the log file
                if self._writing is False:
                   f.write(self._formatter.headline(data))
                   self._writing = True 

                f.write(self._formatter.file(data))

            # Outputting the log to the console
            print(self._formatter.console(data))