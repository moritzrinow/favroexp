import os
import json
import requests
import urllib

try:
  with open('config.json') as f:
    conf = json.load(f)
except IOError:
  print('Config file does not exist')
  exit(1)

url = 'https://favro.com/api/v1/'
user = conf['user']
org = conf['organization']
token = conf['token']
auth = (user, token)

def get_url(method):
  return url + method
    
def get_collections():
  path = get_url("collections")
  r = requests.get(path, headers={
    "organizationId": org,
    "archived": "true"
  }, auth=auth).content
  return json.loads(r)['entities']

collections = get_collections()

for collection in collections:
  print(collection['name'])
