
RESET = "\033[0m"

LEVEL_COLORS = {
    "INFO": "\033[32m",
    "WARNING": "\033[33m",
    "ERROR": "\033[31m",
}

SYMBOLS = {
    "INFO": "🟢",
    "WARNING": "🟡",
    "ERROR": "🔴",
}


class Formatter:
    def console(self, data: dict) -> str:
        result = ( 
            f"<< [{data["date"]}] "
            f"{LEVEL_COLORS[data["level"]]}[{data["level"]}]{RESET} "
            f"- {data["message"]}" 
        )

        return result

    def file(self, data: dict) -> str:
        result = ( 
            f"<< [{data["date"]}] "
            f"[{SYMBOLS[data['level']]}] [{data["level"]}] "
            f"- {data["message"]}"
            "\n" 
        )
 
        return result 

    def headline(self, data: dict) -> str:
        result = (    
            "\n"       
            f"{'_'*27}"
            f"[ {data['date-short']} ]" 
            f"{'_'*27}"
            "\n"
        )

        return result
        

