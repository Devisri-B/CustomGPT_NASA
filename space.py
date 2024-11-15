from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

# NASA API Key
NASA_API_KEY = "DEMO_KEY"


SERVICE_AUTH_KEY = "398759872845632392323758730397456"
ERROR_STRING = "The authorization header is missing or doesn't match the required key."

# Requires token be present
def assert_auth_header():
    assert request.headers.get(
        "Authorization", None) == f"Bearer {SERVICE_AUTH_KEY}"

# Utility function to make requests to NASA APIs
def get_data_from_nasa(url, params=None):
    if params is None:
        params = {}
    params['api_key'] = NASA_API_KEY
    try:
        assert_auth_header()
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except AssertionError:
     return ERROR_STRING
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# 1. International Space Station (ISS) Current Location
@app.route('/api/iss_location', methods=['GET'])
def iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    data = get_data_from_nasa(url)
    return jsonify(data)


# 2. Near-Earth Object (NEO) Data
@app.route('/api/neo', methods=['GET'])
def neo():
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Set default dates to today if not provided
    if not start_date:
        start_date = datetime.today().strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.today().strftime('%Y-%m-%d')

    params = {"start_date": start_date, "end_date": end_date}
    data = get_data_from_nasa(url, params)
    return jsonify(data)

# 3. Astronomy Picture of the Day (APOD)
@app.route('/api/apod', methods=['GET'])
def apod():
    url = "https://api.nasa.gov/planetary/apod"
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Set default dates to today if not provided
    if not start_date:
        start_date = datetime.today().strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.today().strftime('%Y-%m-%d')

    params = {"start_date": start_date, "end_date": end_date}
    data = get_data_from_nasa(url,params)
    return jsonify(data)


def get_lat_lon_from_place(place_name):
    geo_url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place_name, "format": "jsonv2"}
    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return lat, lon
    return None, None

# 4. Earth observation Data
@app.route('/api/earth', methods=['GET'])
def earth():
    url = "https://api.nasa.gov/planetary/earth/assets"
    
    place_name = request.args.get('place')
    if place_name:
        lat, lon = get_lat_lon_from_place(place_name)
        if not lat or not lon:
            return jsonify({"error": "Unable to find coordinates for the specified place"}), 400
    else:
        # Default coordinates if no place is provided
        lat = request.args.get('lat', '1.5')
        lon = request.args.get('lon', '100.75')

    date = datetime.today().strftime('%Y-%m-%d')
    params = {"lat": lat, "lon": lon, "dim": "0.1", "date": date}
    data = get_data_from_nasa(url, params)
    return jsonify(data)

# 5. Space Weather Data (DONKI) - solar flares
@app.route('/api/space_weather', methods=['GET'])
def space_weather():
    url = "https://api.nasa.gov/DONKI/FLR"
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    params = {"start_date": start_date, "end_date": end_date}
    data = get_data_from_nasa(url, params)
    return jsonify(data)


# 7. Space Weather Data (DONKI) - geomagnetic storms
@app.route('/api/geomagnetic_storms', methods=['GET'])
def geomagnetic_storms():
    url = "https://api.nasa.gov/DONKI/GST"
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    params = {"start_date": start_date, "end_date": end_date}
    data = get_data_from_nasa(url, params)
    return jsonify(data)

# 8. Space Weather Data (DONKI) - Interplanetary Shock (IPS)
@app.route('/api/interplanetary', methods=['GET'])
def interplanetary():
    url = "https://api.nasa.gov/DONKI/IPS"
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    params = {"start_date": start_date, "end_date": end_date}
    data = get_data_from_nasa(url, params)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
