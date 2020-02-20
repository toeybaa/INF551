import requests
from pprint import pprint
import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    for i in range(len(argv)):
        input_file = argv[i];
        print ("Creating", input_file);
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
        jsondata = json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
        jsondata = jsondata.replace("#","")
        write_invertedList(jsondata,json_file)
        f.write(jsondata)
        r2 = requests.put("https://inf551-49f71.firebaseio.com/"+json_file, data = jsondata)

def write_invertedList(db,json_file):
    v1 = inverted_index(db)
    Json = json.dumps(v1)
    json_file = json_file.rstrip(".json")
    print("Creating inverted list for " + "\"" + json_file+".csv\"")
    json_file = json_file + "_inverted_list" + ".json"
    with open (json_file, "w") as f:
        f.write(Json)
    r2 = requests.put("https://inf551-49f71.firebaseio.com/" + json_file, data=Json)

def word_split(text):
    word_list = []
    wcurrent = []
    windex = None
    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
            windex = i
        elif wcurrent:
            word = u''.join(wcurrent)
            word_list.append((windex - len(word) + 1, word))
            wcurrent = []
    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex - len(word) + 1, word))
    return word_list

def words_cleanup(words):
    cleaned_words = []
    for index, word in words:
        cleaned_words.append((index, word))
    return cleaned_words
def words_normalize(words):
    normalized_words = []
    for index, word in words:
        wnormalized = word.lower()
        normalized_words.append((index, wnormalized))
    return normalized_words
def word_index(text):
    words = word_split(text)
    words = words_normalize(words)
    words = words_cleanup(words)
    return words
def inverted_index(text):
    inverted = {}
    for index, word in word_index(text):
        locations = inverted.setdefault(word, [])
        locations.append(index)
    return inverted

if __name__ == "__main__":
   main(sys.argv[1:])