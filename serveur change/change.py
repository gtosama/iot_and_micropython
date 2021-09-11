#https://microcontrollerslab.com/micropython-openweathermap-api-esp32-esp8266-sensorless-weather-station/
import urequests

currency_api_key = 'f889b1ec8e-66b0ae8641-qz8dte'

currency_api_url = 'https://api.fastforex.io/fetch-one?from=EUR&to=TND&api_key='+currency_api_key 

currency_data = urequests.get(currency_api_url)
print(currency_data.json())

