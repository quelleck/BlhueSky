import re
import subprocess
import notifications
from time import sleep
from random import randint
from qhue import Bridge
from pysolar.solar import *
import datetime
import config
from collections import deque
import requests


def get_bridge_ip():
    sleep(20)
    meethue_page = requests.get('https://www.meethue.com/api/nupnp').json()
    print("IP address of Bridge: {}".format(meethue_page[0][
        'internalipaddress']))
    return meethue_page[0]['internalipaddress']


host_ip = get_bridge_ip()
user = config.hue_user_key
b = Bridge(host_ip, user)

lights = b.lights
groups = b.groups

# ACTIONS -------------------


def fast_color_loop(light):
    number_of_colors_to_cycle = 6
    while number_of_colors_to_cycle > 0:
        random_hue_value = randint(0, 65535)
        lights(light, 'state', hue=random_hue_value)
        sleep(.14)
        number_of_colors_to_cycle -= 1


def blink_group(group):
    groups(group, 'action', alert="select")
    sleep(1)
    groups(group, 'action', alert="none", transitiontime=0, on=False)


def lights_off(group):
    notifications.ifttt_post(False)
    groups(group, 'action', on=False)


def default_on_state(manual_ct):
    print("Sun tracking not enabled, default ct value will be used")
    if manual_ct == "Cold":
        values = [254, 155]
        return values
    elif manual_ct == "Cool":
        values = [254, 250]
        return values
    elif manual_ct == "Warm":
        values = [254, 350]
        return values
    elif manual_ct == "Warmer":
        values = [254, 450]
        return values


def update_ct(bri_ct_values):
    print("No manual change was found")
    print("Change lights to updated ct value")
    print("If lights are off, they will stay off")
    groups(config.group_num, 'action', ct=bri_ct_values[1])
    print("Home - Updated")

# OPTIONS ------------------------


def boring_on(bri_ct_values):
    print("Boring on chosen in config")
    notifications.ifttt_post(True)
    groups(config.group_num,
           'action',
           on=True,
           bri=bri_ct_values[0],
           ct=bri_ct_values[1])


def loop_each_on(bri_ct_values):
    print("Loop each on chosen in config")
    notifications.ifttt_post(True)
    light_list = get_lights_from_group(config.group_num)
    light_deque = deque(light_list)
    num_of_lights = how_many_lights()
    print(light_deque)
    random_hue_value = randint(0, 65535)
    print("Number of lights to rotate through: {}".format(num_of_lights))
    while num_of_lights > 0:
        lights(light_deque[0],
               'state',
               on=True,
               transitiontime=0,
               bri=127,
               hue=random_hue_value,
               sat=254)
        sleep(.1)
        fast_color_loop(light_deque[0])
        lights(light_deque[0],
               'state',
               bri=bri_ct_values[0],
               ct=bri_ct_values[1])
        sleep(.3)
        light_deque.rotate()
        print("Rotated deque = {}".format(light_deque))
        random_hue_value = randint(0, 65535)
        num_of_lights -= 1
    sleep(.7)


def random_color_bursts(bri_ct_values):
    print("Random color bursts chosen in config")
    notifications.ifttt_post(True)
    light_list = get_lights_from_group(config.group_num)
    num_of_lights = how_many_lights()
    light_deque = deque(light_list)
    hue_value = randint(0, 65535)
    while num_of_lights > 0:
        lights(light_deque[0],
               'state',
               on=True,
               transitiontime=0,
               bri=254,
               hue=hue_value,
               sat=254)
        sleep(.1)
        lights(light_deque[0],
               'state',
               bri=bri_ct_values[0],
               ct=bri_ct_values[1])
        sleep(.1)
        light_deque.rotate()
        hue_value = randint(0, 65535)
        num_of_lights -= 1
        sleep(.3)


def police(bri_ct_values):
    print("Police chosen in config")
    notifications.ifttt_post(True)
    num_red_blue = 7
    groups(config.group_num,
           'action',
           on=True,
           transitiontime=0,
           bri=254,
           hue=1,
           sat=254)
    sleep(1)
    while num_red_blue > 0:
        groups(config.group_num, 'action', transitiontime=0, hue=42500)
        sleep(1)
        groups(config.group_num, 'action', transitiontime=0, hue=1)
        sleep(1)
        num_red_blue -= 1
    groups(config.group_num, 'action', ct=bri_ct_values[1])


def police_chase(bri_ct_values):
    print("Police chase chosen in config")
    notifications.ifttt_post(True)
    light_list = get_lights_from_group(config.group_num)
    light_deque = deque(light_list)
    groups(config.group_num, 'action', on=True, bri=254, hue=1, sat=254)
    length_of_chase = 80
    while length_of_chase > 0:
        lights(light_deque[0], 'state', transitiontime=0, hue=1)
        sleep(.1)
        lights(light_deque[0], 'state', transitiontime=0, hue=42500)
        sleep(.1)
        light_deque.rotate()
        length_of_chase -= 1
    groups(config.group_num, 'action', ct=bri_ct_values[1])


def mothership(bri_ct_values):
    print("Mothership chosen in config")
    notifications.ifttt_post(True)
    light_list = get_lights_from_group(config.group_num)
    light_deque = deque(light_list)
    num_of_lights = how_many_lights() * 3
    sleep(1)
    while num_of_lights > 0:
        lights(light_deque[0], 'state', on=True, bri=100, hue=46600, sat=254)
        sleep(0.1)
        lights(light_deque[1], 'state', on=True, bri=100, ct=50)
        sleep(0.1)
        light_deque.rotate(-2)
        num_of_lights -= 1
    groups(config.group_num, 'action', transitiontime=20, bri=bri_ct_values[0], ct=bri_ct_values[1])

# INFO -----------------


def how_many_lights():
    light_list = get_lights_from_group(config.group_num)
    num_of_lights = len(light_list)
    return num_of_lights


def check_for_changes(current_settings, last_bri_ct_values):
    print("Check for a manual change")
    num_of_lights = how_many_lights()
    current_settings = str(current_settings)
    current_ct_settings = str(re.findall(r"'ct': [0-9]*", current_settings))
    current_bri_settings = str(re.findall(r"'bri': [0-9]*", current_settings))
    num_searched = 0
    lights_with_unchanged_settings = 0
    x = 4
    print("Current ct settings: {}".format(current_ct_settings))
    print("Current bri settings: {}".format(current_bri_settings))
    while num_searched < 7:
        ct_search_num = (last_bri_ct_values[1] - x)
        bri_search_num = (last_bri_ct_values[0] - x)
        current_ct_search = str(ct_search_num)
        current_bri_search = str(bri_search_num)
        num_found = current_ct_settings.count(
            current_ct_search) + current_bri_settings.count(current_bri_search)
        lights_with_unchanged_settings += num_found
        x -= 1
        num_searched += 1
        print("Searching for num: {} and {}".format(ct_search_num,
                                                    bri_search_num))
    print(
        "number of lights with the same settings (should be lights x2): {}".format(
            lights_with_unchanged_settings))
    print("Number of lights: {}".format(num_of_lights))
    if lights_with_unchanged_settings == num_of_lights * 2:
        print("Home - no manual changes")
        return True
    else:
        print("Home - there was a manual change")
        return False


def get_lights_from_group(group):
    light_info = groups(group, http_method='get')
    lights_used = light_info['lights']
    return lights_used


def save_light_attributes(lights_used):
    print("Get current light settings")
    sleep(2)
    light_info = []
    for light in lights_used:
        saves = lights(light, http_method='get')
        light_info.append(saves['state'])
    return light_info


def lets_check(device_list):
    num_of_devices = len(device_list)
    index = 0
    while num_of_devices > 0:
        device = device_list[index]
        print("Checking for device {}".format(device))
        attempts = 1
        while attempts < 3:
            print("Attempt {}".format(attempts))
            output = subprocess.check_output(
                ["sudo", "rfcomm", "connect", "0", device, "10"],
                stderr=subprocess.STDOUT)
            decode = output.decode("utf-8")
            print(decode)
            away = re.search("Host", decode)
            if away:
                print("Device not found")
                attempts += 1
                sleep(1)
            else:
                print("Device found")
                return True
        num_of_devices -= 1
        index += 1
    return False

# SUN ------------------


def get_ct_of_sun():
    values = sun_status(config.lon, config.lat)
    print("Brightness, CT values from get_ct_of_sun(): {}".format(values))
    return values


def sun_status(longitude, latitude):
    d = datetime.datetime.now()
    print("Current time: {}".format(d))
    altitude = get_altitude(longitude, latitude, d)
    print("Sun is {} degrees above/below the horizon".format(altitude))
    if altitude <= -18:
        value = [254, 470]
    elif altitude >= -18 and altitude < -13:
        value = [254, 430]
    elif altitude >= -13 and altitude < -10:
        value = [254, 400]
    elif altitude >= -10 and altitude < -7:
        value = [254, 370]
    elif altitude >= -7 and altitude < -5:
        value = [254, 350]
    elif altitude >= -5 and altitude < -2:
        value = [254, 320]
    elif altitude >= -2 and altitude < 0:
        value = [254, 300]
    elif altitude >= 0 and altitude < 5:
        value = [254, 280]
    elif altitude >= 5 and altitude < 10:
        value = [254, 270]
    elif altitude >= 5 and altitude < 10:
        value = [254, 260]
    elif altitude >= 10 and altitude < 20:
        value = [254, 254]
    elif altitude >= 20 and altitude < 30:
        value = [254, 245]
    elif altitude >= 30 and altitude < 40:
        value = [254, 234]
    elif altitude >= 40 and altitude <= 90:
        value = [254, 153]
    return value
