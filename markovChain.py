
from geopy.distance import vincenty
import numpy as np
                        #ijs,dom
statPointsLjubljana=[(46.042324, 14.488047),(46.043446, 14.485427)]

statPointsLondon=[(46.042324, 14.488047),(46.043446, 14.485427)]
distance=50



def determineState(cordinate,states,distance):
    for i in range(len(states)):
            dist = (vincenty(states[i], cordinate).meters)
            if(dist<distance):
                return i
    return -1



def calculateTransitionMatrix(data,states,distance):
    matrix = [[0 for x in range(len(states))] for y in range(len(states))]

    for i in range(len(data)-1):
        row=determineState(data[i],states,distance)
        coloumn=determineState(data[i+1],states,distance)
        if(row!=-1 and coloumn!=-1):
            matrix[row][coloumn]=matrix[row][coloumn]+1;

    array=[]
    for a in matrix:
        sumArray=sum(a)
        if(sumArray>0):
            newList = [x*1.0 / sumArray for x in a]
        else:
            newList=a
        array.append(newList);
    return array