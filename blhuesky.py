#! /usr/bin/env python3
# BlhueSky
# Bluetooth Philips Hue Controller
# Ethan Seyl - 2016

from time import sleep
import config
import controls

seconds_between_bluetooth_scans_when_home = config.seconds_between_bluetooth_scans_when_home
seconds_between_bluetooth_scans_when_away = config.seconds_between_bluetooth_scans_when_away
device_list = config.device_mac.split()
choice = config.option


def arrived_home():
    print("Arrived")
    bri_ct_values = controls.get_ct_of_sun()
    if config.sun_tracking:
        print("Sun tracking is enabled")
        if choice == "boring_on":
            controls.boring_on(bri_ct_values)
        elif choice == "loop_each_on":
            controls.loop_each_on(bri_ct_values)
        elif choice == "random_color_bursts":
            controls.random_color_bursts(bri_ct_values)
        elif choice == "police":
            controls.police(bri_ct_values)
        elif choice == "police_chase":
            controls.police_chase(bri_ct_values)
        elif choice == "mothership":
            controls.mothership(bri_ct_values)
    else:
        print("Sun tracking is disabled")
        default = controls.default_on_state(config.manual_ct)
        if choice == "boring_on":
            controls.boring_on(default)
        elif choice == "loop_each_on":
            controls.loop_each_on(default)
        elif choice == "random_color_bursts":
            controls.random_color_bursts(default)
        elif choice == "police":
            controls.police(default)
        elif choice == "police_chase":
            controls.police_chase(default)
        elif choice == "mothership":
            controls.mothership(default)
    print("Sleeping for {} seconds".format(
        seconds_between_bluetooth_scans_when_home))
    sleep(seconds_between_bluetooth_scans_when_home)
    print("Returning last bri and ct values: {}".format(bri_ct_values))
    return bri_ct_values


def home(last_bri_ct_values):
    print("Home")
    if config.sun_tracking:
        print("Sun tracking is enabled")
        bri_ct_values = controls.get_ct_of_sun()
        current_settings = controls.save_light_attributes(
            controls.get_lights_from_group(config.group_num))
        no_changes = controls.check_for_changes(current_settings,
                                                last_bri_ct_values)
        if no_changes:
            controls.update_ct(bri_ct_values)
            print("Sleeping for {} seconds".format(
                seconds_between_bluetooth_scans_when_home))
            sleep(seconds_between_bluetooth_scans_when_home)
            print("Return the bri and ct values")
            return bri_ct_values
        else:
            print("Sleeping for {} seconds".format(
                seconds_between_bluetooth_scans_when_home))
            sleep(seconds_between_bluetooth_scans_when_home)
            return bri_ct_values
    else:
        print("Home - sun tracking disabled - changing nothing")
    print("Sleeping for {} seconds".format(
        seconds_between_bluetooth_scans_when_home))
    sleep(seconds_between_bluetooth_scans_when_home)


def left():
    if config.shutoff_enabled:
        controls.lights_off(config.group_to_turn_off)
        print("Left - sleeping for {} seconds".format(
            seconds_between_bluetooth_scans_when_away))
    else:
        print("Left - shutoff disabled - sleeping for {} seconds".format(
            seconds_between_bluetooth_scans_when_away))
    sleep(seconds_between_bluetooth_scans_when_away)


def gone():
    print("Gone - sleeping for {} seconds".format(
        seconds_between_bluetooth_scans_when_away))
    sleep(seconds_between_bluetooth_scans_when_away)

# -----------------------------------------------------------------------------------------

sleep(20)  # WAIT UNTIL BLUETOOTH STARTS
controls.blink_group(0)  # STARTUP NOTIFICATION
infinite_loop = True
was_i_gone = True
while infinite_loop:
    am_i_home = controls.lets_check(device_list)
    if am_i_home and was_i_gone:
        last_bri_ct_values = arrived_home()
        was_i_gone = False

    elif am_i_home and was_i_gone is False:
        last_bri_ct_values = home(last_bri_ct_values)

    elif am_i_home is False and was_i_gone is False:
        left()
        was_i_gone = True

    elif am_i_home is False and was_i_gone:
        gone()
