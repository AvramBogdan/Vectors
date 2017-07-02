import vectorOp

def readFromFile(file)
  
  vector = " "
  vectorSplit = list()
  with open(file) as f:
  	vector = f.readline()
   
  vectorSplit = vector.split(" ")
  return vectorSplit

def calculate(A, B):
  	
    stateA = True
    stateB = True
    
    if vectorOp.zeroElement(A) == True:
    	print("Vector A is not well defined")
    else:
    	stateA = False
    
    if vectorOp.zeroElement(B) == True:
    	print("Vector B is not well defined")
    else:
    	stateB = False
     
    if stateA == False:
    	A = vectorOp.mulByTwo(A)
     
    if stateB == False:
        B = vectorOp.mulByTwo(B)
   	
    print("Vector A: ", A)
    print("Vector B: ", B)
    
#Main

A = list()
B = list()

A = readFromFile("VectorA.txt")
B = readFromFile("VectorB.txt")


calculate(A, B)



