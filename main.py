
import readFile
import detectStayPoints
import detectFrquentPlaces
import markovChain

def saveCordinates(path,touples):
    f = open('spd.txt','w')

    for x,y in SP:
        print str(y)+","+str(x)
        f.write(str(x)+","+str(y)+"\n")
    f.close()

if __name__ == "__main__":

    file=readFile.loadTestDataset(readFile.fileName)
    #Za next place prediction potrebujemo vec
    SP=(detectStayPoints.stayPointDetection(file, 80, 300000));

    ##with menual list of states
    print markovChain.calculateTransitionMatrix(SP,markovChain.statPointsLjubljana,50);



    states= detectFrquentPlaces.DJCluster(detectFrquentPlaces.transformData(file),40,12);

    print markovChain.calculateTransitionMatrix(SP,states,100);



