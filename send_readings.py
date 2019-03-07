import urequests
import ujson
from time import sleep_ms

def send(distance, room):
    distance = str(distance)
    room = str(room)
    url = "https://eeromikkonen.com/sensor/distance.php?distance=" + distance + "&room=" + room
    print(url)
    try:
        request = urequests.get(url)
        response = request.content
        responseJSON = ujson.loads(response)
        if (responseJSON["success"]):
            print("Upload succesful")
        else:
            print("Upload failed")
            sleep_ms(30000)
        request.close()
    except Exception as e:
        print("Request failed: "+ str(e))
