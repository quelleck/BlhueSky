import requests
import config

ifttt = config.ifttt_key


def ifttt_post(home):
    if home:
        print("Sending lights on notification")
        requests.post('https://maker.ifttt.com/trigger/lights_on/with/key/%s' %
                      ifttt)

    else:
        print("Sending lights off notification")
        requests.post(
            'https://maker.ifttt.com/trigger/lights_off/with/key/%s' % ifttt)
