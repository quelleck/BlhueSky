#Blhue Sky

Blhue Sky is a feature filled, customizable python script for controlling Philips Hue lights. Built specifically for a Raspberry Pi with bluetooth. Requires python 3.

#Features
- Bluetooth proximity detection to turn lights on/off. Use any bluetooth device, no pairing required.
- Changes the color temperature of your lights throughout the day based on location and altitude of the Sun over the horizon. Smart enough to not override your settings if you make a change with another app. #HealthyCircadianRhythms
- If you disable Sun tracking, have the lights turn on to a color temp of your choice.
- Unlimited number of devices can be used for proximity detection.
- Multiple fun light transitions for when your device is detected!
- IFTTT notifications.
- Stays out of your way! If you arrive home but someone else already turned on the lights, their settings won't be overridden.

#Customizations
- Choose any of your light groups to control.
- Choose from a variety of transitions (each only last a few seconds) to use when your device is detected on arrival.
- Enable/Disable Sun tracking. If disabled, choose a default color temp for your lights to turn on to.
- FOR LARGER LIVING SPACES: Enable/Disable ability to turn off the lights when your device leaves bluetooth range. VERY handy if bluetooth doesn't cover your entire living space. Simply use the geofence in the Philips Hue app to turn your lights off when you leave. DO NOT use the geofence for arriving, just make sure the Raspberry Pi is in bluetooth range of your front door.

#Features in Development
- Install via pip
- WeMo switch support

#Installing (before pip install is ready)
- Clone the repo to your home directory (/home/pi/BlhueSky)
- Copy blhuesky.sh to /etc/init.d/
- Run this command in the terminal sudo update-rc.d blhuesky.sh defaults
- Fill out the config.py file with your info and settings
- Reboot the pi (The service takes about 30 seconds to start after reboot. Lights in the group you selected will flash.)
