import urequests

def send(distance):
    try:
        distance = str(distance)
        url = "https://eeromikkonen.com/sensor&distance=" +distance
        print(url)
        request = urequests.get(url)
        request.close()
    except Exception as e:
        print("Request failed: "+ str(e))
