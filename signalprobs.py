import random as rand
import math 


#signal probability for two input gates

# 2-input AND gate truth table
# 0 0:0
# 0 1:0
# 1 0:0
# 1 1:1

def sp2AND(in1,in2):
    and2= in1*in2
    return and2


# 2-input OR gate truth table
# 0 0:0
# 0 1:1
# 1 0:1
# 1 1:1

def sp2OR(in1,in2):
    or2= 1-(1-in1)*(1-in2)
    return or2
    

# 2-input XOR gate truth table
# 0 0:0
# 0 1:1
# 1 0:1
# 1 1:0

def sp2XOR(in1,in2):
    xor2=(1-in1)*in2 + in1*(1-in2)
    return xor2


# 2-input NAND gate truth table
# 0 0:1
# 0 1:1
# 1 0:1
# 1 1:0
def sp2NAND(in1,in2):
    nand2=1-(in1*in2)
    return nand2

# 2-input NOR gate truth table
# 0 0:1
# 0 1:0
# 1 0:0
# 1 1:0     

def sp2NOR(in1,in2):
    nor2=(1-in1)*(1-in2)
    return nor2
    

#switching activity for two input gates


def sw2AND(in1,in2):
    esw=2*(sp2AND(in1,in2)*(1-sp2AND(in1,in2)))
    return esw

def sw2OR(in1,in2):
    esw=2*(sp2OR(in1,in2)*(1-sp2OR(in1,in2)))
    return esw

def sw2XOR(in1,in2):
    esw=2*(sp2XOR(in1,in2)*(1-sp2XOR(in1,in2)))
    return esw

def sw2NAND(in1,in2):
    esw=2*(sp2NAND(in1,in2)*(1-sp2NAND(in1,in2)))
    return esw

def sw2NOR(in1,in2):
    esw=2*(sp2NOR(in1,in2)*(1-sp2NOR(in1,in2)))
    return esw

#signal probability for 3 input gates


def sp3AND(in1,in2,in3):
    and3= sp2AND(sp2AND(in1,in2),in3)
    return and3


    
def sp3OR(in1,in2,in3):
    or3= sp2OR(sp2OR(in1,in3),in3)
    return or3


def sp3XOR(in1,in2,in3):
    xor3= sp2XOR(sp2XOR(in1,in2),in3) 
    return xor3
    

def sp3NAND(in1,in2,in3):
    nand3=sp2NAND(sp2NAND(in1,in2),in3)
    return nand3 

def sp3NOR(in1,in2,in3):
    nor3=sp2NOR(sp2NOR(in1,in2),in3)
    return nor3

#switching activity for 3 input gates

def sw3AND(in1,in2,in3):
    esw=2*(sp2AND(sp2AND(in1,in2),in3)*(1-sp2AND(sp2AND(in1,in2),in3)))
    return esw

def sw3OR(in1,in2,in3):
    esw=2*(sp2OR(sp2OR(in1,in2),in3)*(1-sp2OR(sp2OR(in1,in2),in3)))
    return esw

def sw3XOR(in1,in2,in3):
    esw=2*(sp2XOR(sp2XOR(in1,in2),in3)*(1-sp2OR(sp2XOR(in1,in2),in3)))
    return esw

def sw3NAND(in1,in2,in3):
    esw=2*(sp2NAND(sp2NAND(in1,in2),in3)*(1-sp2NAND(sp2NAND(in1,in2),in3)))
    return esw

def sw3NOR(in1,in2,in3):
    esw=2*(sp2NOR(sp2NOR(in1,in2),in3)*(1-sp2NOR(sp2NOR(in1,in2),in3)))
    return esw



#signal probability for N input gates

def spnAND(inputN):
    andN=sp2AND(inputN[0],inputN[1])
    for i in range(2,len(inputN)):
        andN=sp2AND(andN,inputN[i])
    return andN       
        

def spnOR(inputN):
    orN=sp2OR(inputN[0],inputN[1])
    for i in range(2,len(inputN)):
        orN=sp2OR(orN,inputN[i])
    return orN       
        
def spnXOR(inputN):
    xorN=sp2XOR(inputN[0],inputN[1])
    for i in range(2,len(inputN)):
        xorN=sp2XOR(xorN,inputN[i])
    return xorN  

def spnNOR(inputN):
    norN=sp2NOR(inputN[0],inputN[1])
    for i in range(2,len(inputN)):
        norN=sp2NOR(norN,inputN[i])
    return norN  


def spnNAND(inputN):
    nandN=sp2NAND(inputN[0],inputN[1])
    for i in range(2,len(inputN)):
        nandN=sp2NAND(nandN,inputN[i])
    return nandN       
        

#switching activity for N input gates

def swnAND(inputN):
    eswn=2*(sp2AND(inputN[0],inputN[1])*(1-sp2AND(inputN[0],inputN[1])))
    for i in range(2,len(inputN)):
        eswn=2*(sp2AND(eswn,inputN[i])*(1-sp2AND(eswn,inputN[i])))

    return eswn

def swnOR(inputN):
    eswn=2*(sp2OR(inputN[0],inputN[1])*(1-sp2OR(inputN[0],inputN[1])))
    for i in range(2,len(inputN)):
        eswn=2*(sp2OR(eswn,inputN[i])*(1-sp2OR(eswn,inputN[i])))

    return eswn

def swnXOR(inputN):
    eswn=2*(sp2XOR(inputN[0],inputN[1])*(1-sp2XOR(inputN[0],inputN[1])))
    for i in range(2,len(inputN)):
        eswn=2*(sp2XOR(eswn,inputN[i])*(1-sp2XOR(eswn,inputN[i])))

    return eswn

def swnNAND(inputN):
    eswn=2*(sp2NAND(inputN[0],inputN[1])*(1-sp2NAND(inputN[0],inputN[1])))
    for i in range(2,len(inputN)):
        eswn=2*(sp2NAND(eswn,inputN[i])*(1-sp2NAND(eswn,inputN[i])))

    return eswn


def swnNOR(inputN):
    eswn=2*(sp2NOR(inputN[0],inputN[1])*(1-sp2NOR(inputN[0],inputN[1])))
    for i in range(2,len(inputN)):
        eswn=2*(sp2NOR(eswn,inputN[i])*(1-sp2NOR(eswn,inputN[i])))
    return eswn


def signalprobs(in1,in2) :

    print("AND gate for input probabilities :",in1,in2,"is:" ,sp2AND(in1,in2))
    print("OR gate for input probabilities :",in1,in2 ,"is :",sp2OR(in1,in2))
    print("XOR gate for input probabilities :",in1,in2 ,"is :",sp2XOR(in1,in2))
    print("NAND gate for input probabilities :",in1,in2 ,"is :",sp2NAND(in1,in2))
    print("NOR gate for input probabilities :",in1,in2 ,"is :",sp2NOR(in1,in2))
    print(" ")
    print(" ")

signalprobs(0.5,0.5)


def SwitchingActivity2(in1,in2):
    print("The switching activity of AND gate with 2 inputs for :",in1,in2,"is:",sw2AND(in1,in2))
    print("The switching activity of OR gate with 2 inputs for :",in1,in2,"is:",sw2OR(in1,in2))
    print("The switching activity of XOR gate with 2 inputs for :",in1,in2,"is:",sw2XOR(in1,in2))
    print("The switching activity of NAND gate with 2 inputs  for :",in1,in2,"is:",sw2NAND(in1,in2))
    print("The switching activity of NOR gate with 2 inputs for :",in1,in2,"is:",sw2NOR(in1,in2))
    print(" ")
    print(" ")

SwitchingActivity2(0.5,0.5)

def signalprobs3(in1,in2,in3):
    print("AND 3 gate for input probabilities :",in1,in2,in3,"is:" ,sp3AND(in1,in2,in3))
    print("OR 3 gate for input probabilities :",in1,in2,in3,"is:" ,sp3OR(in1,in2,in3))
    print("XOR 3 gate for input probabilities :",in1,in2,in3,"is:" ,sp3XOR(in1,in2,in3))
    print("NAND 3 gate for input probabilities :",in1,in2,in3,"is:" ,sp3NAND(in1,in2,in3))
    print("NOR 3 gate for input probabilities :",in1,in2,in3,"is:" ,sp3NOR(in1,in2,in3))
    print(" ")
    print(" ")

signalprobs3(0.5,0.5,0.5)

def SwitchingActivity3(in1,in2,in3):
    print("The switching activity of AND gate with 3 inputs for :",in1,in2,in3,"is:",sw3AND(in1,in2,in3))
    print("The switching activity of OR gate with 3 inputs for :",in1,in2,in3,"is:",sw3OR(in1,in2,in3))
    print("The switching activity of XOR gate with 3 inputs for :",in1,in2,in3,"is:",sw3XOR(in1,in2,in3))
    print("The switching activity of NAND gate with 3 inputs for :",in1,in2,in3,"is:",sw3NAND(in1,in2,in3))
    print("The switching activity of NOR gate with 3 inputs for :",in1,in2,in3,"is:",sw3NOR(in1,in2,in3))
    print(" ")
    print(" ")

SwitchingActivity3(0.5,0.5,0.5)

def signalprobsN(inputN):
    print("AND N gate for input probabilities :",inputN,"is:" ,spnAND(inputN))
    print("OR N gate for input probabilities :",inputN ,"is :",spnOR(inputN))
    print("XOR N gate for input probabilities :",inputN ,"is :",spnXOR(inputN))
    print("NAND N gate for input probabilities :",inputN ,"is :",spnNAND(inputN))
    print("NOR N gate for input probabilities :",inputN ,"is :",spnNOR(inputN))
    print(" ")
    print(" ")

signalprobsN([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])    

def SwitchingActivityN(inputN):
    print("The switching activity of AND gate with",len(inputN),"inputs for :",inputN,"is:",swnAND(inputN))
    print("The switching activity of OR gate with",len(inputN),"inputs for :",inputN,"is:",swnOR(inputN))
    print("The switching activity of XOR gate with",len(inputN),"inputs for :",inputN,"is:",swnXOR(inputN))
    print("The switching activity of NAND gate with",len(inputN),"inputs for :",inputN,"is:",swnNAND(inputN))
    print("The switching activity of NOR gate with",len(inputN),"inputs for :",inputN,"is:",swnNOR(inputN))
    print(" ")
    print(" ")

SwitchingActivityN([0.5,0.5,0.5,0.5,0.5,0.5])