
import json
import math

#Constants
fileName = 'data/test.json';


#load raw json file and return array structure with dictionary
def loadTestDataset(fileName):
    dataset = []
    with open(fileName) as data_file:
        data = json.load(data_file)
        for row in data:
            activity = {}
            if ('latitude' in row):
                activity['latitude'] = float(row['latitude'])
            if ('longitude' in row):
                activity['longitude'] = float(row['longitude'])
            if ('time' in row):
                activity['time'] = long(row['time'])
            dataset.append(activity)
    return dataset
