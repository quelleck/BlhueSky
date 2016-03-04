#! /usr/bin/env python3
# BlhueSky
# Bluetooth Philips Hue Controller
# Ethan Seyl - 2016

from time import sleep
import config
import controls

home_wait = config.home_wait
away_wait = config.away_wait
device_list = config.device_mac.split()
choice = config.option


def arrived_home():
    print("Arrived")
    bri_ct_values = controls.get_ct_of_sun()
    if config.sun_tracking:
        print("Sun tracking is enabled")
        if controls.are_lights_in_group_off(config.group_num):
            if choice == "option_one":
                controls.option_one(bri_ct_values)
            elif choice == "option_two":
                controls.option_two(bri_ct_values)
            elif choice == "option_three":
                controls.option_three(bri_ct_values)
        else:
            print("Arrived - lights already on")
    else:
        print("Sun tracking is disabled")
        if controls.are_lights_in_group_off(config.group_num):
            default = controls.default_on_state(config.manual_ct)
            if choice == "option_one":
                controls.option_one(default)
            elif choice == "option_two":
                controls.option_two(default)
        else:
            print("Arrived - lights already on")
    print("Sleeping for %s seconds" % home_wait)
    sleep(home_wait)
    print("Returning last bri and ct values: %s" % bri_ct_values)
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
            print("Sleeping for %s seconds" % home_wait)
            sleep(home_wait)
            print("Return the bri and ct values")
            return bri_ct_values
        else:
            print("Sleeping for %s seconds" % home_wait)
            sleep(home_wait)
            return bri_ct_values
    else:
        print("Home - sun tracking disabled - changing nothing")
    print("Sleeping for %s seconds" % home_wait)
    sleep(home_wait)


def left():
    if config.shutoff_enabled:
        controls.lights_off(config.group_to_turn_off)
        print("Left - sleeping for %s seconds" % away_wait)
    else:
        print("Left - shutoff disabled - sleeping for %s seconds" % away_wait)
    sleep(away_wait)


def gone():
    print("Gone - sleeping for %s seconds" % away_wait)
    sleep(away_wait)

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
