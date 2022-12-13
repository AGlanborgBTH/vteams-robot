import requests
import random
import threading
import time

def update_scooter_location(scooter_id, lat, long):
  url = "http://localhost:3000/v1/scooters/{}".format(scooter_id)
  payload = {"location": {"lat": lat, "long": long}}
  r = requests.patch(url, json=payload)
  if r.status_code == 200:
    print("Scooter {} location updated to lat: {}, long: {}".format(scooter_id, lat, long))
  else:
    print("Failed to update scooter location: {}".format(r.text))

def update_scooter_locations(scooter_ids):
  while True:
    for scooter_id in scooter_ids:
      lat = random.uniform(-90, 90)
      long = random.uniform(-180, 180)
      update_scooter_location(scooter_id, lat, long)
    time.sleep(1)

# Update three scooters with random lat/long values
scooter_ids = ["63974faf07b8f76aa2137b0c", "63974faf07b8f76aa2137b0d", "63974faf07b8f76aa2137b0e", ]
for scooter_id in scooter_ids:
  lat = random.uniform(-90, 90)
  long = random.uniform(-180, 180)
  update_scooter_location(scooter_id, lat, long)

# Start a thread for each scooter to update its location every second
threads = []
for scooter_id in scooter_ids:
  t = threading.Thread(target=update_scooter_locations, args=([scooter_id],))
  threads.append(t)
  t.start()
