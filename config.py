# Configuration for Blhue Sky

# Enter your Hue bridge user API key within
# the quotes. Follow instructions here to get your key:
# http://www.developers.meethue.com/documentation/getting-started
hue_user_key = ''

# Enter the MAC address of the bluetooth device
# that the Pi will scan for within the quotes. If you have
# more than one device, separate them with spaces within
# the quotes.
# Example: 'AA:BB:CC:DD:EE:FF AB:BC:CD:DE:EF'
device_mac = ''

# If you'd like to enable IFTTT notifications,
# replace False with your API key
# within quotes. Get an IFTTT key here:
# https://ifttt.com/maker
# Make two notification recipes - one called
# lights_on and the other lights_off.
ifttt_key = False

# Set the seconds between bluetooth scans
# while you're away here. Default is 20
# seconds.
seconds_between_bluetooth_scans_when_away = 20

# Set the seconds between bluetooth scans
# while you're away here. Default is 180
# seconds.
seconds_between_bluetooth_scans_when_home = 180

# Set which light transition happens when you arrive.
# boring_on:
# Plain old turn the lights on
# loop_each_on:
# Fast color loop 10 colors randomly through all lights
# ending on the color temp of Sun or default chosen value.
# random_color_bursts:
# Random color bursts rotating through all lights twice.
# police:
# police_chase:
# Example: 'loop_each_on'
option = 'loop_each_on'

# Enable sunlight hue adjustments?
# Default is True.
# Turn off is False
sun_tracking = True

# What is the number of the group of
# lights you'd like to use? Default is
# group 0 - all lights. Use instructions here
# to find your group numbers:
# http://www.developers.meethue.com/documentation/getting-started
group_num = 0

# What group should turn off
# when you leave? Default is group 0,
# all lights.
group_to_turn_off = 0

# Enter your longitude and latitude in
# decimal form. Easy to grab from google maps.
# Don't use quotes.
lon = 41
lat = -95

# If you don't want to enable sun tracking
# choose your default color temp.
# Options: "Cold" "Cool" "Warm" "Warmer"
manual_ct = "Warm"

# If your living space is too big and you keep
# coming in/out of BT signal while home, you can
# disable he ability to turn the lights off when
# you leave bluetooth range.
shutoff_enabled = True
