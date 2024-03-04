from random import randint
from statistics import mean, variance
import matplotlib.pyplot as plt
import statsmodels.api as sm


def spNOT(inp):
    spnot=1-inp
    return spnot

def sp2AND(in1,in2):
    and2= in1*in2
    return and2

def sp2OR(in1,in2):
    or2= 1-(1-in1)*(1-in2)
    return or2
    
def sp2XOR(in1,in2):
    xor2=(1-in1)*in2 + in1*(1-in2)
    return xor2

def sp2NAND(in1,in2):
    nand2=1-(in1*in2)
    return nand2   

def sp2NOR(in1,in2):
    nor2=(1-in1)*(1-in2)
    return nor2
    
def sp2XNOR(in1,in2):
    xnor2=1-sp2XOR(in1,in2)
    return xnor2

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

def spnXNOR(inputN):
    xnorN=sp2XNOR(inputN[0],inputN[1])
    for i in range(2,len(inputN)):
        xnorN=sp2XNOR(xnorN,inputN[i])
    return xnorN           

def swNOT(inp):
    esw=2*(spNOT(inp)*(1-spNOT(inp)))
    return esw

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
 
def swnXNOR(inputN):
    eswn=2*(sp2XNOR(inputN[0],inputN[1])*(1-sp2XNOR(inputN[0],inputN[1])))
    for i in range(2,len(inputN)):
        eswn=2*(sp2XNOR(eswn,inputN[i])*(1-sp2XNOR(eswn,inputN[i])))

    return eswn



from collections import namedtuple
Element = namedtuple("Element",field_names=["type", "output", "inputs"])

def process(element, SignalsTable, print_SignalsTable=False):
    if element.type=='NOT':
        SignalsTable[element.output] = spNOT(SignalsTable[element.inputs[0]])
    elif element.type=="AND":
        SignalsTable[element.output] = spnAND([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="OR":
        SignalsTable[element.output] = spnOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="XOR":
        SignalsTable[element.output] = spnXOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="NAND":
        SignalsTable[element.output] = spnNAND([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="NOR":
        SignalsTable[element.output] = spnNOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="XNOR":
        SignalsTable[element.output] = spnXNOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    if print_SignalsTable:
        print("The signal probabilities after the process:",SignalsTable)

def processEsw(element, SignalsTable, print_SignalsTable=False):
    if element.type=='NOT':
        SignalsTable[element.output] = swNOT(SignalsTable[element.inputs[0]])
    elif element.type=="AND":
        SignalsTable[element.output] = swnAND([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="OR":
        SignalsTable[element.output] = swnOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="XOR":
        SignalsTable[element.output] = swnXOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="NAND":
        SignalsTable[element.output] = swnNAND([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="NOR":
        SignalsTable[element.output] = swnNOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    elif element.type=="XNOR":
        SignalsTable[element.output] = swnXNOR([SignalsTable[element.inputs[0]],SignalsTable[element.inputs[1]]])
    if print_SignalsTable:
        print("The switching ativity after the process:",SignalsTable)


def find_topInputs(elements, signals):
    topInputs = []
    outputs = []
    for elem in elements:
        outputs.append(elem.output)
    for s in signals:
        if s in outputs:
            pass
        else:
            topInputs.append(s)
    return topInputs
   



def sort_elements(elements, set_inputs, sortedElementsTable):
    if len(elements) == 1:
        elem = elements[0]
        sortedElementsTable.append(elem)
        return sortedElementsTable
    
    for elem in elements:
        if set_inputs.issuperset( set(elem.inputs) ):
            elements.remove(elem)
            sortedElementsTable.append(elem)
            set_inputs.add(elem.output)

            return sort_elements(elements, set_inputs, sortedElementsTable)

    print("Error: Sort failed")


class Curcuit:
    def __init__(self, filename):    
        #open file    
        f = open(filename, 'r')
        lines = []
        for i in f:
            lines.append(i.split())

        ElementsTable = []
        signals = [] #all the signal names
        

        #check for top inputs
        first_line = lines[0]
        if first_line[0]=='top_inputs':
            are_topInputs_given = True
            topInputs = first_line[1:]
            lines.pop(0)
        else:
            are_topInputs_given = False

        # parse elements and signals
        for elem_list in lines:
            element = Element(elem_list[0], elem_list[1], elem_list[2:])
            ElementsTable.append( element )
            
            for j in elem_list[1:]:
                if j in signals:
                    pass
                else:
                    signals.append(j)
            
        if not are_topInputs_given:
            topInputs = find_topInputs(ElementsTable, signals)
        
        SortedElementsTable = sort_elements(ElementsTable, set(topInputs), [])
        
        self.topInputs = topInputs
        self.ElementsTable = SortedElementsTable
        self.signals = signals
        self.SignalsTable = dict()
        for s in signals:
            self.SignalsTable[s] = 0


    def giveInputs(self, *inputs):
        """The inputs should be given in the order that they appear in topInputs."""
        if len(inputs) != len(self.topInputs):
            print("Error: Not given enough top inputs or more than enough top inputs given.")
            print("Number of inputs given:", len(inputs))
            print("Number of top inputs expected:", len(self.topInputs))
            return
        for i in range(len(inputs)):
            self.SignalsTable[self.topInputs[i]] = inputs[i]

    def process(self, print_print_SignalsTable=False):
        for e in self.ElementsTable:
            process(e, self.SignalsTable)
    
    def processEsw(self, print_SignalsTable=False):
        for e in self.ElementsTable:
            processEsw(e, self.SignalsTable)

    def inputsNumber(self):
        return len(self.topInputs)

    def fromSignalsTableCopyOutputs(self):
        outputsTable = dict()
        for s in self.SignalsTable:
            if s in self.topInputs:
                pass
            else:
                outputsTable[s] = self.SignalsTable[s]
        return outputsTable

    def countSwitches(self, workload1, workload2):
        curcuit.giveInputs(*workload1)
        curcuit.process()
        outputsBefore = curcuit.fromSignalsTableCopyOutputs()
        
        curcuit.giveInputs(*workload2)
        curcuit.process()
        outputsAfter = curcuit.fromSignalsTableCopyOutputs()

        switchesNumber = 0
        for outputsignal in outputsBefore:
            if (outputsBefore[outputsignal]!=outputsAfter[outputsignal]):
                switchesNumber+=1
        return switchesNumber



def generateRandomWorkload(curcuit, L):
    workload=[]

    for i in range(L):
        workload.append([])
        for j in range(curcuit.inputsNumber()):
            workload[i].append(randint(0,1))

    return workload


class Individual:
    def __init__(self, curcuit):
        self.workload = generateRandomWorkload(curcuit, 2)
        self.score = curcuit.countSwitches(self.workload[0], self.workload[1])



curcuit = Curcuit('form2.txt')

individuals = []
num_individuals = 2000
for i in range(num_individuals):
    individuals.append( Individual(curcuit) )

scores = []
for i in individuals:
    scores.append(i.score)

print("Mean :",mean(scores))
print("Variance:",variance(scores))

plt.plot( range(num_individuals) , scores )
plt.ylabel("Number of switches")
plt.xlabel("Number of individuals")
plt.show()



