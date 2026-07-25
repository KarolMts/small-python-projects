import json 

def load_invoice(path:str) -> dict:
    
    with open(path, mode="r", encoding="utf-8") as file:
        return json.load(file)
    