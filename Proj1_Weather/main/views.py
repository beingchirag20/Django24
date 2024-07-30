from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        api_key = 'eb726d1a82fd4cabb1e211929243007'
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

        try:
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data['location']['country']),
                "coordinate": str(list_of_data['location']['lon']) + ' ' + str(list_of_data['location']['lat']),
                "temp": str(list_of_data['current']['temp_c']) + '°C',
                "pressure": str(list_of_data['current']['pressure_mb']) + ' hPa',
                "humidity": str(list_of_data['current']['humidity']) + '%',
            }
        except Exception as e:
            data = {"error": str(e)}

    else:
        data = {}
    
    return render(request, "main/index.html", data)
