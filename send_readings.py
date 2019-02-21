import urequests

def send(distance):
    distance = str(distance)
    url = "https://eeromikkonen.com/sensor&distance=" +distance
    print(url)
    try:
        request = urequests.get(url)
    except Exception as e:
        print("Request failed: "+ str(e))
