'''
Created on Oct 13, 2018

@author: justin
'''

def createMiddles(cube=[]):
    middle1 = cube[4]
    middle2 = cube[13]
    middle3 = cube[22]
    middle4 = cube[31]
    middle5 = cube[40]
    middle6 = cube[49]
    
    middles = [middle1, middle2, middle3, middle4, middle5, middle6]
    
    return middles

# Return true if all middles are unique
def compareAllMiddles(cube=[]):
    middles = createMiddles(cube)
    
    for i in range(len(middles) - 1):
        for j in range(i+1, len(middles)):
            if middles[i] == middles[j]:
                return False
    return True