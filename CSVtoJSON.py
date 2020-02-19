#from firebase import firebase
import requests
from pprint import pprint
import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    for i in range(len(argv)):
        input_file = argv[i];
        print (input_file);
        output_file = input_file.rstrip(".csv") + ".json";
        read_csv(input_file, output_file, format)

#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file, encoding="latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    # firebase = firebase.FirebaseApplication("https://inf551-49f71.firebaseio.com")
    with open(json_file, "w") as f:
        jsondata = json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False, )
        jsondata = jsondata.replace("#","")
        f.write(jsondata)
        r2 = requests.put("https://inf551-49f71.firebaseio.com/.json", data = jsondata)

if __name__ == "__main__":
   main(sys.argv[1:])