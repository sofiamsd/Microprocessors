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
Element = namedtuple("Element",field_names=["type", "inputs", "output"])

def process(element, SignalsTable):
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
    print("The siganl probabilities after the process:",SignalsTable)

def processEsw(element, SignalsTable):
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
    print("The switching ativity after the process:",SignalsTable)


#check if the input also belongs in the output list
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
        else:
            are_topInputs_given = False

        # parse elements and signals
        for elem_list in lines:
            element = Element(elem_list[0], elem_list[1:-1], elem_list[-1])
            ElementsTable.append( element )
            
            for j in elem_list[1:]:
                if j in signals:
                    pass
                else:
                    signals.append(j)
            

        if not are_topInputs_given:
            topInputs = find_topInputs(ElementsTable, signals)
            
        self.topInputs = topInputs
        self.ElementsTable = ElementsTable
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

    def process(self):
        for e in self.ElementsTable:
            process(e, self.SignalsTable)
    
    def processEsw(self):
        for e in self.ElementsTable:
            processEsw(e, self.SignalsTable)

def testbench(curcuit, *inputs):
    print("\nTestbench results with", inputs)
    print()
    curcuit.giveInputs(*inputs)
    curcuit.process()
    print("SignalsTable after process: ", curcuit.SignalsTable)
    print()
    curcuit.processEsw()
    print("SignalsTable after processEsw: ", curcuit.SignalsTable)

    

curcuit = Curcuit('model1.txt')
testbench(curcuit, 0.5, 0.5, 0.5)
testbench(curcuit, 0.4446, 0.4446, 0.4446)

curcuit = Curcuit('model2.txt')
testbench(curcuit, 0.5, 0.5, 0.5)
testbench(curcuit, 0.4446, 0.4446, 0.4446)