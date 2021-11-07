# Weather Flask App

project that Displays temperature of the weather in Cities


## Routes
```python
@views.route('/', methods=['POST', 'GET'])
def home_bage():
return render_template('home.html', weather = weather)
```
return Json to html home file with information of city. 
```python
{
'city': 'San Francisco, US',
'description': 'broken clouds', 
'tempF': '53.91°F', 
'tempC': '12.17°C', 
'icon': 'http://openweathermap.org/img/wn/04n@2x.png'
}
```

### you can run this project locally by clone it and install the requirements.txt 
## Installation
```bash
pip install requirements.txt
```
run app.py file and you can see it in [localhost](http://127.0.0.1:3000/) port:3000


