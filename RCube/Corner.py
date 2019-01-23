'''
Created on Oct 13, 2018

@author: justin
'''

# return true if all corners are unique
def compareAllCorners(cube=[]):
    corners = createCorners(cube)
    for i in range(len(corners) - 1):
        for j in range(i + 1, len(corners)):
            if compareCorners(corners[i], corners[j]):
                return False
    return True
            

def createCorners(cube = []):
    corner1 = [cube[0], cube[29], cube[42]]
    corner2 = [cube[2], cube[9], cube[44]]
    corner3 = [cube[36], cube[27], cube[20]]
    corner4 = [cube[38], cube[11], cube[18]]
    corner5 = [cube[6], cube[35], cube[45]]
    corner6 = [cube[8], cube[15], cube[47]]
    corner7 = [cube[33], cube[51], cube[26]]
    corner8 = [cube[53], cube[17], cube[24]]
    
    corners = [corner1, corner2, corner3, corner4, 
               corner5, corner6, corner7, corner8]
    
    return corners

#return true if corners are equal
def compareCorners(corner1=[], corner2=[]):
    corner1Dict = {}
    corner2Dict = {}
    
    for element in corner1:
        if not element in corner1Dict:
            corner1Dict[element] = 0
        corner1Dict[element] += 1
        
    for element in corner2:
        if not element in corner2Dict:
            corner2Dict[element] = 0
        corner2Dict[element] += 1
    
    sameCorner = cmp(corner1Dict, corner2Dict)
    if sameCorner == 0:
        return True
    return False