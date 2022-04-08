import json

filename = 'data2.json'
json_data = open(filename).read()
data = json.loads(json_data)

for i in range(len(data)):
  print(data[i]["title"])
