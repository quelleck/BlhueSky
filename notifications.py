import requests
import config

ifttt = config.ifttt_key


def ifttt_post(home):
    if ifttt:
        if home:
            print("Sending lights on notification")
            requests.post(
                'https://maker.ifttt.com/trigger/lights_on/with/key/{}'.format(
                    ifttt))

        else:
            print("Sending lights off notification")
            requests.post(
                'https://maker.ifttt.com/trigger/lights_off/with/key/{}'.format(
                    ifttt))
    else:
        print("No ifttt key")
