import requests
import sys
import json

def main(argv):
    key = argv[0]
    r1 = requests.get("https://inf551-49f71.firebaseio.com/country.json")
    r2 = requests.get("https://inf551-49f71.firebaseio.com/city.json")
    r3 = requests.get("https://inf551-49f71.firebaseio.com/countrylanguage.json")
    json1 = r1.json()
    result = function(json1, key)
    json2 = r2.json()
    function2(json2,result)
    json3 = r3.json()
    function3(json3,result)

def function(json_object, name):
    finalresult = []
    for dict in json_object:
        dict2 = {y:x for x,y in dict.items()}
        res = [val for key, val in dict2.items() if name in key.lower()]
        if len(res) != 0:
            finalresult.append(dict[' Code'])
    print("country: " + (str(finalresult)))
    return finalresult

def function2(json_object, result):
    finalresult = []
    for dict in json_object:
        dict2 = {y: x for x, y in dict.items()}
        for i in result:
            res = [val for key, val in dict2.items() if i in key]
            if len(res) != 0:
                finalresult.append(dict[' District'])
    print("city: " + (str(finalresult)))

def function3(json_object, result):
    finalresult = []
    for dict in json_object:
        dict2 = {y: x for x, y in dict.items()}
        for i in result:
            res = [val for key, val in dict2.items() if i in key]
            if len(res) != 0:
                finalresult.append(dict[' Language'])
    print("countrylanguage: " + str(finalresult))

if __name__ == "__main__":
   main(sys.argv[1:])