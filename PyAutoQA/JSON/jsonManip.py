import json

apiData = '{"name":"Josiah", "grade":12, "age":21}'
jsonData = json.loads(apiData)
jsonData
jsonData['name']
jsonData['grade']
jsonData['age']

foodDict = {'apple':'red', 'banana':'yellow', 'cherry':'red'}
stringFoodDict = json.dumps(foodDict)
stringFoodDict