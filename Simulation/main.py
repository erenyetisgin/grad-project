import time
import numpy as np
import random

car_list = []


class Car:
    # action_completed = False
    iter_id = 1
    velo =[0,0]
    def __init__(self, posx, posy, lane):
        self.pos = np.array([posx, posy])
        self.id = Car.iter_id
        self.lane = lane
        Car.iter_id += 1

    def print_obj(self):
        print(self.id, self.pos, self.lane)
    def setvelocity(self,v):
        self.velo = v

    def move(self):
        self.pos +=velo
  #  def move(self,direction):

       # if (self.direction == 0):
          # for i in range(12):
              #  for j in range(12):
                   # if(self.pos[i][j]!= self.pos[0][0]):
                      #  self.pos[i][j] = self.pos[i + 1][j]


def velDraw(M,cars):
    for i in range(cars.shape[0]):
        cars[i].move()




# Adds a new car on the surface of the specified lane
def add_car(M, lane):
    if lane == 0:
        if M[0, 5] == 0:
            car = Car(0, 5, 0)
            car_list.append(car)
            M[0, 5] = car.id
    elif lane == 1:
        if M[6, 0] == 0:
            car = Car(6, 0, 1)
            car_list.append(car)
            M[6, 0] = car.id
    elif lane == 2:
        if M[11, 6] == 0:
            car = Car(11, 6, 2)
            car_list.append(car)
            M[11, 6] = car.id
    elif lane == 3:
        if M[5, 11] == 0:
            car = Car(5, 11, 3)
            car_list.append(car)
            M[5, 11] = car.id


# Function to initialize car objects. (Do not select n bigger than 5)
def init_cars(M, n):
    for i in range(n):
        lane = random.randint(0, 3)
        if lane == 0:
            for j in range(4, -1, -1):
                if M[j, 5] == 0:
                    car = Car(j, 5, 0)
                    car_list.append(car)
                    M[j, 5] = car.id
                    break
        elif lane == 1:
            for j in range(4, -1, -1):
                if M[6, j] == 0:
                    car = Car(6, j, 1)
                    car_list.append(car)
                    M[6, j] = car.id
                    break
        elif lane == 2:
            for j in range(7, 12):
                if M[j, 6] == 0:
                    car = Car(j, 6, 2)
                    car_list.append(car)
                    M[j, 6] = car.id
                    break
        elif lane == 3:
            for j in range(7, 12)
                if M[5, j] == 0:
                    car = Car(5, j, 3)
                    car_list.append(car)
                    M[5, j] = car.id
                    break
        else:
            print("randint() error.")

M = np.zeros((12, 12))
M = M.astype(int)
init_cars(M, 5)
iteration = 0
while True:
    if iteration % 4 == 0:
        rand = random.random()
        if rand > 0.5:
            lane = random.randint(0, 3)
            add_car(M, lane)
            
            
            
    print("\n", iteration)
    print(M)
           
   

    for car in car_list:
        car.print_obj()
    iteration += 1

    # time.sleep(1)
    input()
