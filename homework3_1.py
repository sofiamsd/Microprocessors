def spNOT(inp):
    spnot=1-inp
    return spnot

def sp2AND(in1,in2):
    and2= in1*in2
    return and2

def swNOT(inp):
    esw=2*(spNOT(inp)*(1-spNOT(inp)))
    return esw

def sw2AND(in1,in2):
    esw=2*(sp2AND(in1,in2)*(1-sp2AND(in1,in2)))
    return esw

print(""" 
        Truth Table
        a b c e f d
        0 1 0 0 1 0
        1 1 0 1 1 1
        1 0 0 0 1 0
        0 0 1 0 0 0""")
from collections import namedtuple
Element = namedtuple("Element",field_names=["type", "inputs", "output"])

def give_inputs(a,b,c):
    SignalsTable[topInputs[0]] = a
    SignalsTable[topInputs[1]] = b
    SignalsTable[topInputs[2]] = c

E1 = Element('AND', [0, 1], 4)
E2 = Element('NOT', [2], 5)
E3 = Element('AND', [4,5], 3)
Elements = [E1,E2,E3]

SignalsTable= [0,0,0,0,0,0] #a=0,b=1,c=2,d=3,e=4,f=5
topInputs = [0,1,2]

def process(element):
    if element.type=='NOT':
        SignalsTable[element.output] = spNOT(SignalsTable[element.inputs[0]])
    elif element.type=="AND":
        SignalsTable[element.output] = sp2AND(SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]])
    
    print("The signal probabilities after the process :",SignalsTable)

def process_circuit(elements):
    for e in elements:
        process(e)

def processEsw(element):
    if element.type=='NOT':
        SignalsTable[element.output] = swNOT(SignalsTable[element.inputs[0]])
    elif element.type=="AND":
        SignalsTable[element.output] = sw2AND(SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]])
    print("The result of switcing activity:",SignalsTable)

def processEsw_circuit(elements):
    for e in elements:
        processEsw(e)




def testbench(a,b,c):
    print("Testbench results with", a, b, c)
    print()
    give_inputs(a,b,c)
    process_circuit(Elements)
    print()
    print("SignalsTable [a,b,c,d,e,f]= ", SignalsTable)
    print()
    processEsw_circuit(Elements)
    print("SignalsTable [a,b,c,d,e,f]= ", SignalsTable)


testbench(0.5, 0.5, 0.5)
testbench(0.4446, 0.4446, 0.4446)