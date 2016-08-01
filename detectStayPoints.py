# aim of this script is compute a stay points, algoritem was taken from paper:
#Li, Q., Zheng, Y., Xie, X., Chen, Y., Liu, W., & Ma, W. (2008). Mining User Similarity Based on Location History, (c). http://doi.org/papers3://publication/uuid/2558F813-9877-4CA8-9C3E-C5E5F2D54BC6
import numpy as np
from geopy.distance import vincenty

#Class which purpose is to save Stay Point.
class Activity:
    arvT = 0
    levT = 0
    points = []
    coords = {};

    def __init__(self, arvT, levT, points,coords):
      self.arvT = arvT
      self.levT = levT
      self.points = points
      self.coords = coords



#method calculate centroid
def centeroidnp(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return sum_x/length, sum_y/length

def stayPointDetection(data, distThreh, timeThreh):
    "This prints a passed string into this function"
    i = 0;
    SP = []
    pointNum = len(data);  # The number of GPS points
    while (i < pointNum):
        j = i + 1;
        token = 0
        while (j < pointNum):
            point1 = ( data[i]['latitude'],data[i]['longitude'])
            point2 = (data[j]['latitude'],data[j]['longitude'])
            dist = (vincenty(point1, point2).meters)
            #dist = math.hypot(data[i]['longitude'] - data[j]['longitude'], data[i]['latitude'] - data[j]['latitude'])
            if dist > distThreh:
                deltaTime = data[j]['time'] - data[i]['time']
                if deltaTime > timeThreh:
                    #arvT, levT, points,coords
                    arrayOfCordinats=[]
                    coords=data[i:j]
                    for coord in coords:
                        tup=(coord['latitude'],coord['longitude'])
                        arrayOfCordinats.append(tup);

                    activity = Activity(data[i]['time'],data[j]['time'],coords,centeroidnp(np.array(arrayOfCordinats)))
                    SP.append(activity)
                    i = j;
                    token = 1;
                break;
            j = j + 1
        if token != 1:
            i = i + 1;
    result=[]
    for element in SP:
        result.append(element.coords)

    return result

