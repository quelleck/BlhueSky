#BlhueSky

BlhueSky is a feature filled, customizable python script for controlling Philips Hue lights. Built specifically for a Raspberry Pi with bluetooth. Requires python 3.

#Features
- Bluetooth proximity detection to turn lights on/off. Use any bluetooth device, no pairing required.
- Changes the color temperature of your lights throughout the day based on location and altitude of the Sun over the horizon. Smart enough to not override your settings if you make a change with another app. #HealthyCircadianRhythms
- If you disable automatic color temperature changing, have the lights turn on to a color temp of your choice.
- Unlimited number of devices can be used for proximity detection.
- Multiple fun light transitions for when your device is detected!
- IFTTT notifications.
- Stays out of your way! If you arrive home but someone else already turned on the lights, their settings won't be overridden.

#Customizations
- Choose any of your light groups to control.
- Choose from a variety of transitions (each only last a few seconds) to use when your device is detected on arrival.
- Enable/Disable automatic color temperature changing. If disabled, choose a default color temp.
- FOR LARGER LIVING SPACES: Enable/Disable ability to turn off the lights when your device leaves bluetooth range. Very handy if bluetooth doesn't cover your entire living space. Simply use the geofence in the Philips Hue app to turn your lights off when you leave.

#Features in Development
- Install via pip
- WeMo switch support

#Installing (before pip install is ready)
- Make sure you have your pi set to the correct time or else the color temperature of your lights will be off.
- Clone the repo to your home directory 
git clone https://github.com/quelleck/BlhueSky/
- Copy blhuesky.sh to /etc/init.d/
sudo cp ~/BlhueSky/blhuesky.sh /etc/init.d
- Run this command to get the script to start when you boot the pi 
sudo update-rc.d blhuesky.sh defaults
- cd into /BlhueSky and open the config.py file in your preferred text editor
cd Blhuesky
nano config.py
- Follow the instructions for each config variable. The main items are your Hue API key, the Bluetooth MAC address(s) of your device(s), and your longitude and latitude. If you'd like you can enter your IFTTT API key for push notifications, disable color temp tracking and set a default color temp, choose a different light effect, disable the pi from turning off your lights when you move out of range, choose a specific light group, and change the frequency of bluetooth pair requests.
- Install the python Hue library 'qhue' (https://github.com/quentinsf/qhue) for python3
sudo pip3 install qhue
- Install pysolar for tracking the sun
sudo pip3 install pysolar
- Make sure you have all other dependencies by starting BlhueSky from terminal and letting the BlhueSky start. Note: BlhueSky sleeps for 30 seconds to make sure it doesn't start before bluetooth when you boot the pi. You may need to install bluetooth or requests.
./lights.py
- Reboot the pi. Remember BlhueSky sleeps for 30 seconds on boot. Your lights will flash and turn off when it starts.
