import threading
import requests
import random
import time

# Update the lat and long for an object's destination with a given id
def update_destination(object_id):
  # Generate a random latitude and longitude
  lat = random.uniform(-90, 90)
  long = random.uniform(-180, 180)

  # Print the object id and the new lat and long values
  print(f'Updating destination for object: {object_id}')
  print(f'  New Lat = {lat}')
  print(f'  New Long = {long}')

  # Use a PATCH request to update the lat and long for the object's destination with the given id
  requests.patch(f'http://localhost:3000/v1/scooters/{object_id}', json={'destination': {'lat': lat, 'long': long}})

# Loop through all objects in the API
while True:
  # Use a GET request to retrieve the list of objects
  response = requests.get('http://localhost:3000/v1/scooters')
  objects = response.json()

  # Loop through all objects
  for object in objects['data']:
    # Check if the object is in use
    if object['inUse']:
      # Update the destination for the object
      thread = threading.Thread(target=update_destination, args=(object['_id'],))
      thread.start()

  # Sleep for 1 second before checking the objects again
  time.sleep(1)