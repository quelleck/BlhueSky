# Configuration for Blhue Sky

# (now found automatically)
# Enter the IP address of your hue bridge
# within the quotes. Find the bridge IP
# in your wireless router.
# hue_bridge_ip = ''

# Enter your Hue bridge user API key within
# the quotes. Follow instructions here to get your key:
# http://www.developers.meethue.com/documentation/getting-started
hue_user_key = '155119e41f09a34f2651b60c3f5e6cd7'

# Enter the MAC address of the bluetooth device
# that the Pi will scan for within the quotes. If you have
# more than one device, separate them with spaces within
# the quotes.
# Example: 'AA:BB:CC:DD:EE:FF AB:BC:CD:DE:EF'
device_mac = 'A8:8E:24:5F:3B:23'

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
seconds_between_bluetooth_scans_when_away = 5

# Set the seconds between bluetooth scans
# while you're away here. Default is 180
# seconds.
seconds_between_bluetooth_scans_when_home = 5

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
option = 'police_chase'

# Enable sunlight hue adjustments?
# Default is True.
# Turn off is False
sun_tracking = True

# What is the number of the group of
# lights you'd like to use? Default is
# group 0 - all lights. Use instructions here
# to find your group numbers:
# http://www.developers.meethue.com/documentation/getting-started
group_num = 1

# What group should turn off
# when you leave? Default is group 0,
# all lights.
group_to_turn_off = 0

# Enter your longitude and latitude in
# decimal form. Easy to grab from google maps.
lon = 41.252904
lat = -95.929074

# If you don't want to enable sun tracking
# choose your default color temp.
# Options: "Cold" "Cool" "Warm" "Warmer"
manual_ct = "Warm"

# If your living space is too big and you keep
# coming in/out of BT signal while home, you can
# disable he ability to turn the lights off when
# you leave bluetooth range.
shutoff_enabled = True
