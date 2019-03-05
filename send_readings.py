import urequests

def send(distance, room):
    distance = str(distance)
    room = str(room)
    url = "https://eeromikkonen.com/sensor/distance.php?distance=" + distance + "&room=" + room
    print(url)
    try:
        request = urequests.get(url)
        request.close()
    except Exception as e:
        print("Request failed: "+ str(e))
