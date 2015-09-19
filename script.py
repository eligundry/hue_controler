import ConfigParser

import requests

# Load config file
config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))

api_endpoint = 'http://{}/api'.format(config.get('hue', 'ip_address'))

def create_user():
    """
    Attempts to create a new authenticated user for the Hue. It will throw an
    exception if the link button has been pressed yes.
    """
    payload = { 'deveicetype': config.get('hue', 'devicetype') }
    r = requests.post(api_endpoint, json=payload)
    return r

    if 'error' in r.json()[0]:
        raise Exception(r.json()[0]['error']['description'])

    return True

def authenticate():
    """
    Authenticates the given devicetype provided in the config file. If the
    devicetype is not a valid user, it will attempt to create the user using
    the Hue API.
    """
    r = requests.get('{}/newdeveloper'.format(api_endpoint))

    if 'error' in r.json()[0]:
        return create_user()

    return True

if __name__ == '__main__':
    authenticate()
