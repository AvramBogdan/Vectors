def zeroElement(A):

  for item in A:
    
    if 0 == int(item):
      return True

  return False
          		
def mulByTwo(matrix):
  
  listM = []
  for item in matrix:
    	listM.append(int(item) * 2)
      
  return listM
        