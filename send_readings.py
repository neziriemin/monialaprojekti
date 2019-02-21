import urequests

def send(distance):
    url = "https://eeromikkonen.com/sensor&distance=" +distance
    request = urequests.get(url)
