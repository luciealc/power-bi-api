from flask import Flask, jsonify
import requests

app = Flask(__name__)

#USE: flask --app apiflask run --debug
# to run

full_cities = []

#get cities min 15
@app.route("/", methods=["GET"])
def get_all():

    def get_paris():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=46.2276&lng=2.2137&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})

    def get_tokyo():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=35.6762&lng=139.6503&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})

    def get_delhi():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=28.6139&lng=77.2090&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})

    def get_shanghai():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=31.2304&lng=121.4737&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_sao():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=-23.5558&lng=-46.6396&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_mexico():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=19.4326&lng=-99.1332&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})

    def get_london():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=51.5072&lng=-0.1276&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_ny():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=40.7128&lng=-74.0060&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_la():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=34.0549&lng=-118.2426&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_dhaka():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=23.8041&lng=90.4152&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_cairo():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=30.0444&lng=31.2357&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_singapore():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=1.3521&lng=103.8198&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    def get_lagos():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=6.5244&lng=3.3792&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_moscow():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=55.7558&lng=37.6173&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_oslo():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=59.9139&lng=10.7522&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_austin():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=30.2672&lng=-97.7431&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_italy():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=41.8719&lng=12.5674&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_spain():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=40.4637&lng=-3.7492&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_southafrica():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=-33.9249&lng=18.4241&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_australia():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=-33.8688&lng=151.2093&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_greenland():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=71.7069&lng=-42.6043&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})
    
    def get_colombia():
        url = 'https://api.ambeedata.com/weather/latest/by-lat-lng?lat=4.5709&lng=-74.2973&x-api-key=9dc47602673271a6b94794221e4a5c80ba02dc82facb0dc40fcd0b003531f826'
        response = requests.get(url)
        data = response.json()
        return data.get("data", {})


    city_getters = [get_paris, get_tokyo, get_delhi, get_shanghai, get_sao, get_mexico, get_london, get_ny, get_la, get_dhaka, get_cairo, get_singapore, get_lagos, get_moscow, get_oslo, get_austin, get_italy, get_spain, get_southafrica, get_australia, get_greenland, get_colombia]
    full_cities = [city_getter() for city_getter in city_getters]

    return jsonify(full_cities), 200

# error management
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World"