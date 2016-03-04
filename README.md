#BlhueSky

Blhue Sky is a feature filled, customizable python script for controlling Philips Hue lights. Built specifically for a Raspberry Pi with bluetooth. Requires python 3.

#Features
- Bluetooth proximity detection to turn on/off lights. Use any bluetooth device, no pairing required.
- Changes the color temperature of your lights throughout the day based on location and altitude of the Sun over the horizon. Smart enough to not override your settings if you make a change with another app. #HealthyCircadianRhythms
- If you disable Sun tracking, choose a color temp you prefer for when the lights turn on.
- Unlimited number of devices can be used for proximity detection.
- Multiple fun light transitions for when your device is detected. No more coming home to a boring scene!
- IFTTT notifications.
- Stays out of your way! If you arrive home but someone else already turned on the lights, their settings won't be overridden.

#Customizations
- Choose any of your light groups to control.
- Choose from a variety of transitions (each only last a few seconds) to use when your device is detected.
- Enable/Disable Sun tracking. If disabled, choose a default color temp for your lights to turn on to.
- FOR LARGER LIVING SPACES: Enable/Disable ability to turn off the lights when your device leaves bluetooth range. VERY handy if you live in a large apartment or house. Simply use the geofence in the Philips Hue app to turn your lights off when you leave. DO NOT use the geofence for arriving, just make sure the Raspberry Pi is in bluetooth range of your front door.

#Features in Development
- WeMo switch support
