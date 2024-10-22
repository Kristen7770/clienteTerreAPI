import requests
from datetime import datetime, timezone

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {
    "format": "geojson",
    "starttime": "2024-01-01",
    "endtime": "2024-12-31",
    "minmagnitude": 5
}

response = requests.get(url, params=params)

if response.status_code == 200:
    
    data = response.json()
    
    if "features" in data and len(data["features"]) > 0:
        earthquake = data["features"][0]
        lugar = earthquake['properties']['place']
        magnitud = earthquake['properties']['mag']
        tiempo = earthquake['properties']['time']
        fecha_hora = datetime.fromtimestamp(tiempo / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Localización: {lugar}")
        print(f"Magnitud: {magnitud}")
        print(f"Fecha y hora: {fecha_hora}")
    else:
        print("No se encontraron terremotos con los criterios especificados.")
else:
    print(f"Error en la solicitud: {response.status_code}")