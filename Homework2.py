from random import random
import matplotlib.pyplot as plt


# 1-input NOT gate truth table
# 0:1
# 1:0

def spNOT(inp):
    spnot=1-inp
    return spnot


def switchingActivityNOT(inp):
    esw=2*(spNOT(inp)*(1-spNOT(inp)))
    return esw


def sp2AND(in1,in2):
    and2= in1*in2
    return and2

def sw2AND(in1,in2):
    esw=2*(sp2AND(in1,in2)*(1-sp2AND(in1,in2)))
    return esw

def circuit(a,b,c):
    e=sp2AND(a,b)
    f=spNOT(c)
    d=sp2AND(e,f)
    return d

print("The signal probability for the circuit is :",circuit(0.5,0.5,0.5))
print()

def switchingActivityC(a,b,c):
    e=sw2AND(a,b)
    f=switchingActivityNOT(c)
    d=sw2AND(e,f)
    return d,e,f

print("The switching activity for the f , e and the final output d are : :",switchingActivityC(0.5,0.5,0.5))
print()
print("The switching activity for the f , e and the final output d are : :",switchingActivityC(0.4446,0.4446,0.4446))

def MCAND(N):
    
    workload= [[0,0],[0,1],[1,0],[1,1]]
    MonteCarloSize=N
    for i in range (MonteCarloSize) :
        workload.append([
            round(random()),
            round(random())    
            ])
    
    vectorsNumber=len(workload)
    
    gateInputNumber=2
    gateOutput=0&0
    switchesNumber=0
    for i in range(vectorsNumber):
        NewGateOutput= workload[i][0] \
                     and workload[i][1] 
                     
        if gateOutput!=NewGateOutput:
            gateOutput=NewGateOutput
            switchesNumber+=1
    
    SwitchingActivity=switchesNumber/vectorsNumber
    print("MonteCarloSize = ",MonteCarloSize)
    print("switchesNumber = ",switchesNumber)
    print("vectosNumber = ",vectorsNumber)
    print("SwitcingActivity = ",SwitchingActivity)
    print()
    # x = [N]
    # y = [SwitchingActivity]
    # plt.title("Switching Activity for N")
    # plt.ylabel("Switchig Activity")
    # plt.xlabel("N")
    # plt.grid()
    # plt.plot(x, y, marker="*", markersize=5, markeredgecolor="red")
    # plt.show()

    
#MCAND(4446)

def MCNot(N):
     
    workload= [[0],[1]]
    MonteCarloSize=N
    for i in range (MonteCarloSize) :
        workload.append([
            round(random())  
            ])
    
    
    vectorsNumber=len(workload)
    
    gateInputNumber=1
    gateOutput=0
    switchesNumber=0
    for i in range(vectorsNumber):
        NewGateOutput= not workload[i][0] 
                                   
        if gateOutput!=NewGateOutput:
            gateOutput=NewGateOutput
            switchesNumber+=1
    SwitchingActivity=switchesNumber/vectorsNumber
    print("MonteCarloSizeNOT = ",MonteCarloSize)
    print("switchesNumberNOT = ",switchesNumber)
    print("vectosNumberNOT = ",vectorsNumber)
    print("SwitcingActivityNOT = ",SwitchingActivity)
    x = [N]
    y = [SwitchingActivity]
    # plt.title("Switching Activity for N")
    # plt.ylabel("Switchig Activity")
    # plt.xlabel("N")
    # plt.grid()
    # plt.plot(x, y, marker="*", markersize=5, markeredgecolor="red")
    # plt.show()

#MCNot(4446)


