import time
import numpy as np
import random


class Car:
    # action_completed = False
    iter_id = 1
    velocity = [0,0]
    def __init__(self, posx, posy, lane, direction):
        self.pos = np.array([posx, posy])
        self.id = Car.iter_id
        self.lane = lane
        Car.iter_id += 1
        self.direction = direction #random.randrange(0,3) 
    def print_obj(self):
        print(self.id, self.pos, self.lane)
    def setVelocity(self, aVel):
        self.velocity = aVel
    def getVelocity(self):
        return self.velocity
    def move(self):
        self.pos = self.pos + self.velocity
    def getLane(self):
        return self.lane
    def setLane(self, lane):
        self.lane = lane
    def getPos(self):
        return self.pos
    def getDirection(self):
        return self.direction
    def getId(self):
        return self.id
    
def getSequence(lane):
    if lane == 0:
        leftSequence = [[1,0], [0,1],[0,1]]
        straigthSequence = [[1,0],[1,0]]
        rightSequence = [[0,-1]]  
    elif lane == 1:
        leftSequence = [[0,1], [-1,0], [-1,0]]
        straigthSequence = [[0,1], [0,1]]
        rightSequence = [[1,0]]
    elif lane == 2: 
        leftSequence = [[-1,0], [0,-1], [0,-1]]
        straigthSequence = [[-1,0], [-1,0]]
        rightSequence = [[0,1]]
    elif lane == 3: 
        leftSequence = [[0,-1], [1,0], [1,0]]
        straigthSequence = [[0,-1], [0,-1]]
        rightSequence = [[-1,0]]
    elif lane == -1:
        return
    sequences = [leftSequence, straigthSequence, rightSequence ]
    return sequences
    
def getCarsByLane(cars, lane):
    carsInLane = []
    for i in range(len(cars)):
        if cars[i].getLane() == lane:
            carsInLane.append(cars[i])
    return carsInLane
    
def greenLightHAN(lane, cars):
    carsToMove = []
    borders = [[5,5],[6,5],[6,6],[5,6]]
    border = borders[lane]
    originalCarIndexes = [] # use for index transformation between cars and cars2Move
    #distancesToBorder = []
    distancesToBorder = [] 
    #define the sequences
    for i in range(len(cars)):
        if cars[i].getLane() == lane:
            carsToMove.append(cars[i])
            originalCarIndexes.append(i)
            distancesToBorder.append( abs(sum( cars[i].getPos() - border )) )
    if len(carsToMove) == 0:
        printMatrix(cars)
        return         
    
    #now we have which cars to move
    casesOfCars = np.zeros(len(carsToMove)) # denoting whether cars have passed the light
                                        # 0 means still not passed the light(easy case)
    seqIndexes = np.zeros(len(carsToMove)) # seqIndexes[i] denotes the next move for the i'th car
    maxIndexes = np.zeros(len(carsToMove)) # for ex: if turning left, maxIndex = 3
    lastCarIndex = np.argmax(distancesToBorder) 
    hasFinished = False
    while hasFinished == False:
        printMatrix(cars)
        for i in range(len(carsToMove)):  
            #move the cars until they reach the green light
            if casesOfCars[i] == 0:
                velocity = border - carsToMove[i].getPos()
                velocity = velocity / distancesToBorder[i]
                carsToMove[i].setVelocity(velocity)
                distancesToBorder[i] -= 1
                if distancesToBorder[i] == 0:
                     casesOfCars[i] = 1
            #now move after they reach gren ligth
            elif casesOfCars[i] == 1:
                #create the velocity sequences 
                sequences = getSequence(carsToMove[i].getLane())   
                if sequences == None:
                    continue
                theSequence = sequences[carsToMove[i].getDirection()] 
                maxIndexes[i] = len(theSequence)
                index = seqIndexes[i]
                if index < maxIndexes[i]:
                    newVel = theSequence[int(index)]
                    carsToMove[i].setVelocity(newVel)
                    index += 1
                    seqIndexes[i] = index
                else:
                    carsToMove[i].setLane(-1)
                    #to do: destroy the car
                    # del carsToMove[i]
                    # np.delete(casesOfCars,i)
                    # np.delete(seqIndexes,i) WRONG!!!!!
                    # np.delete(maxIndexes,i)
                    # np.delete(distancesToBorder,i)
                    # del cars[originalCarIndexes[i]]
                    # print("sss")
                    #check if all the cars have gone
                    if i == lastCarIndex:
                        hasFinished = True
        updateForVelocity(cars)
        
        
    
    
#only initites cars accoring to car number and return a martix showing cars and car lits
def init_cars44(n):
    M = np.zeros((12,12))
    car_list = []
    for i in range(n):
        carDirection = random.randrange(0,3)
        lane = random.randint(0, 3)
        if lane == 0:
            for j in range(4, -1, -1):
                if M[j, 5] == 0:
                    car = Car(j, 5, 0, carDirection)
                    car_list.append(car)
                    M[j, 5] = car.id
                    break
        elif lane == 1:
            for j in range(4, -1, -1):
                if M[6, j] == 0:
                    car = Car(6, j, 1, carDirection)
                    car_list.append(car)
                    M[6, j] = car.id
                    break
        elif lane == 2:
            for j in range(7, 12):
                if M[j, 6] == 0:
                    car = Car(j, 6, 2, carDirection)
                    car_list.append(car)
                    M[j, 6] = car.id
                    break
        elif lane == 3:
            for j in range(7, 12):
                if M[5, j] == 0:
                    car = Car(5, j, 3, carDirection)
                    car_list.append(car)
                    M[5, j] = car.id
                    break
        else:
            print("randint() error.")
    return M,car_list


#only updates the matrix accoridng to velocity of cars
def updateForVelocity(cars):
    M = np.zeros((12,12))
    for i in range(len(cars)):
        cars[i].move()

# just print the matrix given cars
def printMatrix(cars):
    M = np.zeros((12,12))
    for i in range(len(cars)):
        x = int ( cars[i].getPos()[0] )
        y = int( cars[i].getPos()[1] )
        carId = cars[i].getId()
        try:
            M[x, y] = carId
        except: 
            print("end of the road for you", carId)
    print(M)
        
   

# Main code goes here, turn the lights on sequentially
M, cars = init_cars44(5)
for i in range(4):
    #find the crowded lane
    carNumLane0 = len( getCarsByLane(cars,0) )
    carNumLane1 = len( getCarsByLane(cars,1) )
    carNumLane2 = len( getCarsByLane(cars, 2) )
    carNumLane3 = len( getCarsByLane(cars, 3) )
    temp = np.array([carNumLane0, carNumLane1, carNumLane2, carNumLane3])
    maxLane = np.argmax(temp)
    max=np.max(temp)
   # start_time = time.time()
   #print("--- %s seconds ---" % (time.time() - start_time))
    greenLightHAN(maxLane,cars)

    #print('İterasyon: ',max)
    
    print("***************NEXT LIGHT**********")
   
    
    
    

# M, cars = init_cars44(5)
# greenLightHAN(0,cars)
# print("other light")
# greenLightHAN(1,cars)
# print("other light")
# greenLightHAN(2,cars)
# print("other light")
# greenLightHAN(3,cars)
    

