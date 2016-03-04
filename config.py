# Configuration for BlhueSky

# Enter the IP address of your hue bridge
# within the quotes. Find the bridge IP
# in your wireless router. I would highly recommend
# manually assigning the IP.
hue_bridge_ip = ''

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
# uncomment this line and enter your API key
# within the quotes. Get an IFTTT key here:
# https://ifttt.com/maker
# Make two notification recipes - one called
# lights_on and the other lights_off.
ifttt_key = ''

# Set the seconds between bluetooth scans
# while you're away here. Default is 20
# seconds.
away_wait = 5

# Set the seconds between bluetooth scans
# while you're away here. Default is 180
# seconds.
home_wait = 5

# Set which light transition happens when you arrive.
# Option One:
# Plain old turn the lights on
# Option Two:
# Fast color loop 10 colors randomly through all lights
# ending on the color temp of Sun or default chosen value.
# Option Three:
# Random color bursts rotating through all lights twice.
# Example: option_one
option = 'option_two'

# Enable sunlight hue adjustments?
# Default is True.
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
manual_ct = "Cold"

# If your living space is too big and you keep
# coming in/out of BT signal while home, you can
# disable he ability to turn the lights off when
# you leave bluetooth range.
shutoff_enabled = True
