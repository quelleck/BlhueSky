import re
import subprocess
import notifications
from time import sleep
from random import randint
from qhue.qhue import Bridge
from pysolar.solar import *
import datetime
import config
from collections import deque

user = config.hue_user_key
host_ip = config.hue_bridge_ip
b = Bridge(host_ip, user)

lights = b.lights
groups = b.groups

# ACTIONS -------------------


def fast_color_loop(light):
    number_of_colors_to_cylce = 5
    while number_of_colors_to_cylce > 0:
        random_hue_value = randint(0, 65535)
        lights(light, 'state', bri=127, hue=random_hue_value, sat=254)
        sleep(.2)
        number_of_colors_to_cylce -= 1


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
    print("Change lights to updated ct values")
    print("If lights are off, they will stay off")
    groups(config.group_num,
           'action',
           bri=bri_ct_values[0],
           ct=bri_ct_values[1])
    print("Home - Updated")


# OPTIONS ------------------------


def option_one(bri_ct_values):
    print("Transition one chosen in config")
    notifications.ifttt_post(True)
    groups(config.group_num,
           'action',
           on=True,
           bri=bri_ct_values[0],
           ct=bri_ct_values[1])


def option_two(bri_ct_values):
    print("Transition two chosen in config")
    notifications.ifttt_post(True)
    light_list = get_lights_from_group(config.group_num)
    light_deque = deque(light_list)
    num_of_lights = how_many_lights()
    print(light_deque)
    random_hue_value = randint(0, 65535)
    print("Number of lights to rotate through: %s" % num_of_lights)
    while num_of_lights > 0:
        lights(light_deque[0],
               'state',
               on=True,
               transitiontime=0,
               bri=254,
               hue=random_hue_value,
               sat=254)
        sleep(.1)
        fast_color_loop(light_deque[0])
        lights(light_deque[0],
               'state',
               bri=bri_ct_values[0],
               ct=bri_ct_values[1])
        sleep(.1)
        light_deque.rotate()
        print("Rotated deque = %s" % light_deque)
        random_hue_value = randint(0, 65535)
        num_of_lights -= 1
    sleep(.7)


def option_three(bri_ct_values):
    print("Transition three chosen in config")
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
        sleep(.7)


# INFO -----------------


def how_many_lights():
    light_list = get_lights_from_group(config.group_num)
    num_of_lights = len(light_list)
    return num_of_lights

'''
The check_for_changes function searches the selected light group's JSON data for the previously set
ct value plus the closest 6 numbers. Example: If ct: 430 was set, this function will search for ct
values 426 - 432 in the JSON data. This is done because the Philips Hue bridge is inconsistent with setting values
between different light models, resulting in some lights set to values off by a few numbers. In the future,
retrieving only the ct values is a good idea since values like bri and sat could be confused for the ct.

'''
def check_for_changes(current_settings, last_bri_ct_values):
    print("Check for a manual change")
    num_of_lights = how_many_lights()
    current_settings_string = str(current_settings)
    num_searched = 0
    lights_with_unchanged_settings = 0
    x = 4
    print("Current settings: %s" % current_settings)
    while num_searched < 7:
        search_num = (last_bri_ct_values[1] - x)
        current_search = str(search_num)
        num_found = current_settings_string.count(current_search)
        lights_with_unchanged_settings += num_found
        x -= 1
        num_searched += 1
        print("Searching for num: %s" % search_num)
    print("number of lights with the same settings: %s" %
          lights_with_unchanged_settings)
    print("Number of lights: %s" % num_of_lights)
    if lights_with_unchanged_settings == num_of_lights:
        print("Home - no manual changes")
        return True
    else:
        print("Home - there was a manual change")
        return False


def get_lights_from_group(group):
    light_info = groups(group, http_method='get')
    lights_used = light_info['lights']
    return lights_used


def are_lights_in_group_off(group):
    number_of_lights = how_many_lights()
    light_info = str(save_light_attributes(get_lights_from_group(group)))
    num_lights_on = light_info.count("True")
    if num_lights_on > number_of_lights:
        return False
    else:
        return True


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
        print("Checking for device %s" % device)
        attempts = 1
        while attempts < 3:
            print("Attempt %s" % attempts)
            output = subprocess.check_output(
                ["sudo", "rfcomm", "connect", "0", device, "10"],
                stderr=subprocess.STDOUT)
            decode = output.decode("utf-8")
            print(decode)
            home_ios = re.search('Permission', decode)
            home_android = re.search('refused', decode)
            if home_ios or home_android:
                print("Device Found")
                return True
            else:
                attempts += 1
                sleep(3)
        num_of_devices -= 1
        index += 1
    return False

# SUN ------------------


def get_ct_of_sun():
    values = sun_status(config.lon, config.lat)
    print("Brightness, CT values from get_ct_of_sun(): %s" % values)
    return values


def sun_status(longitude, latitude):
    d = datetime.datetime.now()
    print("Current time: %s" % d)
    altitude = get_altitude(longitude, latitude, d)
    print("Sun is %s degrees above/below the horizon" % altitude)
    if altitude <= -18:
        value = [254, 470]
        return value
    elif altitude >= -18 and altitude < -13:
        value = [254, 430]
        return value
    elif altitude >= -13 and altitude < -10:
        value = [254, 400]
        return value
    elif altitude >= -10 and altitude < -7:
        value = [254, 370]
        return value
    elif altitude >= -7 and altitude < -5:
        value = [254, 350]
        return value
    elif altitude >= -5 and altitude < -2:
        value = [254, 320]
        return value
    elif altitude >= -2 and altitude < 0:
        value = [254, 300]
        return value
    elif altitude >= 0 and altitude < 5:
        value = [254, 280]
        return value
    elif altitude >= 5 and altitude < 10:
        value = [254, 270]
        return value
    elif altitude >= 5 and altitude < 10:
        value = [254, 260]
        return value
    elif altitude >= 10 and altitude < 20:
        value = [254, 254]
        return value
    elif altitude >= 20 and altitude < 30:
        value = [254, 245]
        return value
    elif altitude >= 30 and altitude < 40:
        value = [254, 234]
        return value
    elif altitude >= 40 and altitude <= 90:
        value = [254, 153]
        return value
