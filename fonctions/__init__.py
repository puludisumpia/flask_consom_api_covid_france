import json
import requests

def get_covid_data(lien):
    """
        Cette fonction a été pensée pour accepter en parametre un lien
        et renvoi les données du type dictionnaire (dict)
    """
    req = requests.get(lien)
    req_json = json.loads(req.text)
    for data in req_json.values():
        for elements in data:
            return elements
