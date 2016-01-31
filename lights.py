import requests
import os
import sys 

token = os.environ.get('LIFX_TOKEN')

settings = {
	"on": {
	  "power": "on",
	  "color": "kelvin:4000",
	  "brightness": 8.0,
	  "duration": 5
	},

	"morning": {
	  "power": "on",
	  "color": "kelvin:4000",
	  "brightness": 1.0,
	  "duration": 50
	},

	"off": {
	  "power": "on",
	  "color": "kelvin:2500",
	  "brightness": 0.0,
	  "duration": 2
	},

	"mood": {
	  "power": "on",
	  "color": "kelvin:2500",
	  "brightness": 0.6,
	  "duration": 5
	}
}

lighting = settings.get("on")

def set_light_value_from_args():
	global lighting
	if sys.argv[1]:
		arg = sys.argv[1]
		if not arg in settings:
			return
		lighting = settings.get(arg)


def set_lights(lighting):
	response = requests.put('https://api.lifx.com/v1/lights/all/state', auth=(token, ''), json=lighting)

set_light_value_from_args()
set_lights(lighting)