
from random import random
import random as rand
import numpy
import numpy as np
import matplotlib.pyplot as plt


def SwitchingActivity(N):
    
    workload= [
        [0,0,0,0],
        [1,1,1,1],
        [0,0,0,1],
        [1,1,1,1],
        [0,1,0,1]
    ]
    MonteCarloSize=N
    #print(workload)
    for i in range (MonteCarloSize) :
        workload.append([
            round(random()),
            round(random()),
            round(random()),
            round(random())
    
            ])
    
    # print(workload)  
    vectorsNumber=len(workload)
    
    gateInputNumber=4
    gateOutput=0&0&0&0
    switchesNumber=0
    for i in range(vectorsNumber):
        NewGateOutput= workload[i][0] \
                     or workload[i][1] \
                     or workload[i][2] \
                     or workload[i][3]
        #if debug: print(i,gateOutput,NewGateOutput,workload[i],switchesNumber)
        if gateOutput!=NewGateOutput:
            gateOutput=NewGateOutput
            switchesNumber+=1
    
    SwitchingActivity=switchesNumber/vectorsNumber
    print("MonteCarloSize = ",MonteCarloSize)
    print("switchesNumber = ",switchesNumber)
    print("vectosNumber = ",vectorsNumber)
    print("SwitcingActivity = ",SwitchingActivity)
    x = [N]
    y = [SwitchingActivity]
    plt.title("Switching activity for N ")
    plt.ylabel("Switchig Activity")
    plt.xlabel("N")
    plt.grid()
    plt.plot(x, y, marker="*", markersize=5, markeredgecolor="red")
    plt.show()

    
SwitchingActivity(4446)