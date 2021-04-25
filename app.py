from datetime import date
import json
import requests


from flask import Flask, render_template
from flask_moment import Moment

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


app = Flask(__name__)
moment = Moment(app)

@app.route("/")
def index():
    # Données france
    url_france = "https://coronavirusapi-france.now.sh/FranceLiveGlobalData"
    data_france = get_covid_data(url_france)
    
    # Données Paris
    url_paris = "https://coronavirusapi-france.now.sh/LiveDataByDepartement?Departement=Paris"
    data_paris = get_covid_data(url_paris)

    # Données Val-de-Marne
    url_marne = "https://coronavirusapi-france.now.sh/LiveDataByDepartement?Departement=Val-de-Marne"
    data_marne = get_covid_data(url_marne)

    # Données génériques
    date_generic = data_france["date"]
    date_generic_split = date_generic.split("-")
    date_format = date(
        int(date_generic_split[0]), 
        int(date_generic_split[1]), 
        int(date_generic_split[2])
    )
    
    return render_template(
        "index.html", 
        data=data_france, 
        data_paris=data_paris,
        data_marne=data_marne,
        date=date_format
    )


if __name__ == "__main__":
    app.run(debug=True)