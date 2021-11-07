from flask import Blueprint, render_template, request, flash
import requests

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def home_bage():

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fc6f13e2450958563e23414c529f3e8d'

    weather = {
        'city': '',
        'description': '',
        'temp': '',
        'icon': ''
        }
    city = request.form.get('city')
    if city == '':
        flash('no city added', category='error')
    elif request.method== 'POST':
        res = requests.get(url.format(city)).json()
        if res['cod']== "404":
            flash('Unvalid Name', category='error')
        else:
            TF = res['main']['temp']
            TC = (TF-32)*(5/9)
            TC = round(TC, 2)
            weather = {
                'city': '{}, {}'.format(res["name"], res["sys"]["country"]),
                'description': res['weather'][0]['description'],
                'tempF': '{}°F'.format(TF),
                'tempC': '{}°C'.format(TC),
                'icon':  'http://openweathermap.org/img/wn/{}@2x.png'.format(res['weather'][0]['icon'])
            }    

    return render_template('home.html', weather = weather)