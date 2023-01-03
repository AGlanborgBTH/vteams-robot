import threading
import requests
import random
import time

@profile
def update_destination(object_id):

  print(f'Updating destination for all Scooters {object_id}')

  requests.patch(f'http://localhost:3000/v1/scooters/{object_id}', json={'destination': {'lat': lat, 'lng': lng}})


while True:
  start_time = time.perf_counter()
  response = requests.get('http://localhost:3000/v1/scooters')
  objects = response.json()

  # Loop through all objects
  for object in objects['data']:
    # Check if the object is in use
    if object['inUse']:

      lat = None
      lng = None


      if object['city'] == str('Göteborg'):
        lat = random.uniform(57.687300367053496, 57.71646139531549)
        lng = random.uniform(11.888231715434216, 12.013669635629554)
        print("Göteborg")

      elif object['city'] == str('Linköping'):
        lat = random.uniform(58.406333, 58.422808)
        lng = random.uniform(15.592416, 15.648206)
        print("Linköping")

      elif object['city'] == str('Uppsala'):
        lat = random.uniform(17.603621, 17.698512)
        lng = random.uniform(59.8439, 59.874093)
        print("Uppsala")

      # Update the destination for the object
      thread = threading.Thread(target=update_destination, args=(object['_id'],))
      thread.start()
      end_time = time.perf_counter()
      elapsed_time = end_time - start_time
      print("The function took %f seconds to execute" % elapsed_time)
      # time.sleep(5)