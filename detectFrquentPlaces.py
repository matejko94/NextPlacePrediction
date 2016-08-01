import numpy as np
from geopy.distance import vincenty
import operator

class ObjectDJCluster:
    processed=False
    timestamp=0
    coords=()
    cluster=0
    rawData=[]

    def __init__(self, timestamp, coords):
      self.timestamp = timestamp
      self.coords = coords


def getNeighbours(data,object, e, minPts):
    neighbours=[]
    for entry in data:

        #var distance = dist(object.attributes, entry.attributes);
        point1 = (entry.coords[0],entry.coords[1])
        point2 = (object.coords[0],object.coords[1])
        dist = (vincenty(point1, point2).meters)
        if object.timestamp!=entry.timestamp:
            if dist<e:
                neighbours.append(entry);

    if(len(neighbours)<minPts):
            return []
    return neighbours

def isDensityJoinable(dataset,neighbours,eps):
    for i in range(len(dataset)):
        for j in range(len(neighbours)):
            if(neighbours[j].timestamp!=dataset[i].timestamp):
                point1 = (dataset[i].coords[0],dataset[i].coords[0])
                point2 = (neighbours[j].coords[1],neighbours[j].coords[1])
                dist = (vincenty(point1, point2).meters)
                if(dist<eps):
                    if(dataset[i].cluster!=-1):
                        return dataset[i].cluster
    return -1


def transformData(datas):
    DJLocs=[]
    for data in datas:
        objectDJCluster= ObjectDJCluster(data['time'],(data['latitude'],data['longitude']));
        DJLocs.append(objectDJCluster);
    return DJLocs;


#method calculate centroid
def centeroidnp(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return sum_x/length, sum_y/length



def DJCluster(DJLocs,eps,minPts):
    cluster=[]
    clusterId=-1;
    for loc in DJLocs:
        if loc.processed==False:

           neighborhouds=getNeighbours(DJLocs,loc,eps,minPts);
           if(len(neighborhouds)==0):
                loc.processed=True
                loc.cluster=-1
           else:
               # N(p) is density-joinable to at least one existing cluster then
               clusterIdPom=isDensityJoinable(cluster,neighborhouds,eps);
               if(clusterIdPom!=-1):
                   for j in range(len(DJLocs)):
                       for k in range(len(neighborhouds)):

                           if(neighborhouds[k].timestamp==DJLocs[j].timestamp):
                               if(DJLocs[j].processed!=True):
                                   cluster.append(DJLocs[j])
                                   DJLocs[j].processed=True;
                                   DJLocs[j].clusterId=clusterIdPom;
               else:
                   #Create a new cluster C based on N(p).
                   clusterId=clusterId+1
                   loc.processed=True;
                   loc.cluster=clusterId;

                   for j in range(len(DJLocs)):
                       for k in range(len(neighborhouds)):
                           if(neighborhouds[k].timestamp==DJLocs[j].timestamp):
                                if(DJLocs[j].processed!=True):
                                   cluster.append(DJLocs[j])
                                   DJLocs[j].processed=True;
                                   DJLocs[j].cluster=clusterId;



    sez={};
    for element in DJLocs:
        if element.cluster in sez:
            array=sez[element.cluster]
            array.append(element.coords)
            sez[element.cluster]=array;
        else:
            sez[element.cluster]=[element.coords]

    result=[]
    for key in sez:
        result.append(centeroidnp(np.array(sez[key])))

    return result







