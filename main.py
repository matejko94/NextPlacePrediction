
import readFile
import detectStayPoints
import detectFrquentPlaces
import markovChain
import numpy as np
#write result
def saveMarkovChainResult(data):
    print data
    x = np.array(data, np.float64)
    np.savetxt("result.txt", x)

def saveCordinates(path,touples):
    f = open('spd.txt','w')

    for x,y in SP:
        print str(y)+","+str(x)
        f.write(str(x)+","+str(y)+"\n")
    f.close()

if __name__ == "__main__":

    file=readFile.loadTestDataset(readFile.fileLjubljana)
    #pridobimo zaporedje stay pointov
    SP=(detectStayPoints.stayPointDetection(file, 80, 300000));
    #racunanje markov chaina s prednstavljenimi stanji
    saveMarkovChainResult(markovChain.calculateTransitionMatrix(SP,markovChain.statPointsLjubljana,50));
    ##izracunamo markov chain z pomocjo ugotovljenih stanj algoritma DJCluster
    states= detectFrquentPlaces.DJCluster(detectFrquentPlaces.transformData(file),40,12);
    #izpis teh stanj
    print markovChain.calculateTransitionMatrix(SP,states,100);



