'''
Created on Sep 23, 2018
Due Sep 26, 2018
@author: J. Sawyer
@author: D. Umphress
'''
from Cube import *
from Corner import *
from RCube.Edge import *
from RCube.Middle import *
from RCube.Rotations import *

# Sends the httpResponse to the microservice
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: op code is missing'
    
    # Creates Cube with op
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube'] = createCube(parm)
        cube = createCube(parm)
        cubeObj = Cube(cube)
         
        # If cube has two faces with same colors, then return error
        if httpResponse['cube'] == 0:
            del httpResponse['cube']
            httpResponse['status'] = 'error: at least two faces have the same color'
             
        #If illegal cube, update status
        elif len(cube) != 54:
            httpResponse['status'] = 'cube is not sized properly'
         
        # If no parm for face, update status
        elif checkFaceParmMissing(parm):
            httpResponse['status'] = 'error: face color is missing'
    
    # Checks Cube with op
    elif(parm['op'] == 'check'):
        httpResponse['status'] = 'checked'
        httpResponse['cube'] = createCube(parm)
        cube = createCube(parm)
        for i in range(len(cube)):
            cube[i] = cube[i].strip()
        cubeObj = Cube(cube)
            
        #If illegal cube, update status
        if len(cube) != 54:
            httpResponse['status'] = 'error: cube is not sized properly'
        
        # If no parm for face, update status
        elif checkFaceParmMissing(parm):
            httpResponse['status'] = 'error: face color is missing'
            
            
        elif cubeNotInParm(parm):
            del httpResponse['cube']
            httpResponse['status'] = 'error: cube must be specified'
            
            
        # If illegak cube, update status
        elif illegalCube(cube):
            httpResponse['status'] = 'error: illegal cube'
        
        # If cube has two faces with same colors, then return error
        elif httpResponse['cube'] == 0:
            del httpResponse['cube']
            httpResponse['status'] = 'error: at least two faces have the same color'
         
        # If full appear, update status
        elif cubeObj.checkForFullFaces(cube):
            httpResponse['status'] = 'full'
       
        # If spots appear, update status
        elif cubeObj.checkForSpots(cube):
            httpResponse['status'] = 'spots'
             
        # If crosses appear, update status
        elif cubeObj.checkForCrosses(cube):
            httpResponse['status'] = 'crosses'
        
        else:
            httpResponse['status'] = 'unknown'
            
    # Rotates Cube with op
    elif(parm['op'] == 'rotate'):
        httpResponse['status'] = 'rotated'
        httpResponse['cube'] = createCube(parm)
        cube = createCube(parm)
#         for i in range(len(cube)):
#             cube[i] = cube[i].strip()
        
        if 'face' not in parm:
            httpResponse['status'] = 'error: face is missing'
        else:
            rotateOp = parm['face']
            if not validRotationOp(rotateOp):
                httpResponse['status'] = 'error: face is unknown'
            else:
                cube = rotateCube(cube, rotateOp)
                  
            
        httpResponse['cube'] = cube
        cubeObj = Cube(cube)
        
        #If illegal cube, update status
        if len(cube) != 54:
            httpResponse['status'] = 'error: cube is not sized properly'
        
        elif cubeNotInParm(parm):
            del httpResponse['cube']
            httpResponse['status'] = 'error: cube must be specified'
        
        elif 'face' not in parm:
            del httpResponse['cube']
            httpResponse['status'] = 'error: face is missing'
            
        elif not validRotationOp(rotateOp):
            del httpResponse['cube']
            httpResponse['status'] = 'error: face is unknown'
            
        # If no parm for face, update status
        elif checkFaceParmMissing(parm):
            httpResponse['status'] = 'error: face color is missing'
            
        # If illegal cube, update status
        elif illegalCube(cube):
            httpResponse['status'] = 'error: illegal cube'
        
        # If cube has two faces with same colors, then return error
        elif httpResponse['cube'] == 0:
            del httpResponse['cube']
            httpResponse['status'] = 'error: at least two faces have the same color'
         
        # If full appear, update status
        elif cubeObj.checkForFullFaces(cube):
            httpResponse['status'] = 'full'
       
        # If spots appear, update status
        elif cubeObj.checkForSpots(cube):
            httpResponse['status'] = 'spots'
             
        # If crosses appear, update status
        elif cubeObj.checkForCrosses(cube):
            httpResponse['status'] = 'crosses'

    # Scrambles cube
    elif(parm['op'] == 'scramble'):
        httpResponse['status'] = 'status'
        cube = createDefaultCube()
        cubeObj = Cube(cube)
        n = 0
        method = 'random'
        
        if 'n' in parm:
            n = parm['n'] 
        if 'method' in parm:
            method = parm['method']
            
        try:
            n = int(n)
        except:
            pass
        
        if n > 99 or n < 0 or not isinstance(n, int):
            httpResponse['status'] = 'error: n is invalid'
        
        elif method == 'random' or method == 'transition':
            randomness, rotations = cubeObj.scramble(cube, method, n)
            status = "scrambled " + str(randomness)
            httpResponse['status'] = status
            httpResponse['rotations'] = rotations
             
        else:
            httpResponse['status'] = 'error: method is unknown'
        
        
        
    elif opIsNotPresent(parm['op']):
        httpResponse['status'] = 'error: op code is missing'
        
        
    else:
        httpResponse['status'] = 'None'
    return httpResponse

def opIsNotPresent(opIn):
    validOPs = ["create", "check"]
    for op in validOPs:
        if opIn == op:
            return False
    return True

def checkFaceParmMissing(parm = {}):
    for key, value in parm.items():
        if key == 'f' or key == 'r' or key == 'b' or key == 'l' or key == 't' or key == 'u':
            if len(value) == 0:
                return True
    return False

def cubeNotInParm(parm={}):
    if 'cube' in parm:
        return False
    return True

def validRotationOp(rotateOp):
    validOps = ['f','F','r','R','b','B','l','L','t','T','u','U']
    for op in validOps:
        if rotateOp == op:
            return True
    return False

# Creates a cube, adjusting the cube with parm input
def createCube(parm):
    cube = ['green',  'green', 'green', 
            'green', 'green', 'green', 
            'green', 'green', 'green', 
            'yellow', 'yellow', 'yellow', 
            'yellow', 'yellow', 'yellow', 
            'yellow', 'yellow', 'yellow',  
            'blue', 'blue', 'blue', 
            'blue', 'blue', 'blue', 
            'blue', 'blue', 'blue', 
            'white', 'white', 'white', 
            'white', 'white', 'white', 
            'white', 'white', 'white', 
            'red', 'red', 'red', 
            'red', 'red', 'red', 
            'red', 'red', 'red', 
            'orange', 'orange', 'orange', 
            'orange', 'orange', 'orange', 
            'orange', 'orange', 'orange']
        

#     cubeObj = Cube(cube)
    
#     cubeObj.changeCube(parm)
#     if cubeObj.duplicateFound():
#         cubeObj.cubeStrList.append(0)
#             
#     return cubeObj.cubeStrList

    cube = changeCube(parm, cube)
    if duplicateFound(cube):  
        cube = 0
    cubeObj = Cube(cube)
    
    
    if 'cube' in parm:
        cube = parm['cube'].split(",")
            
    return cube

def createDefaultCube():
    cube = ['green',  'green', 'green', 
            'green', 'green', 'green', 
            'green', 'green', 'green', 
            'yellow', 'yellow', 'yellow', 
            'yellow', 'yellow', 'yellow', 
            'yellow', 'yellow', 'yellow',  
            'blue', 'blue', 'blue', 
            'blue', 'blue', 'blue', 
            'blue', 'blue', 'blue', 
            'white', 'white', 'white', 
            'white', 'white', 'white', 
            'white', 'white', 'white', 
            'red', 'red', 'red', 
            'red', 'red', 'red', 
            'red', 'red', 'red', 
            'orange', 'orange', 'orange', 
            'orange', 'orange', 'orange', 
            'orange', 'orange', 'orange']
    return cube

# Input: parm = parameters for cube, cubeIn = cube to be changed
# If there was duplicate colors, then return 0
# Returns the changed cube
def changeCube(parm={}, cubeIn=[]):
    cube = cubeIn
    usedValues = []
    for key, value in parm.items():
        
        if key == 'f':
            setValuesInRange(cube, value, 0)
        elif key == 'r':
            setValuesInRange(cube, value, 9)
        elif key == 'b':
            setValuesInRange(cube, value, 18)
        elif key == 'l':
            setValuesInRange(cube, value, 27)
        elif key == 't':
            setValuesInRange(cube, value, 36)
        elif key == 'u':
            setValuesInRange(cube, value, 45)
        
        usedValues.append(value)
        
    return cube

# Takes in input for current value and usedValues
# Returns true if the value of valueIn is in usedValuesIn
def duplicateFound(cube=[]):
    faces = [cube[0], cube [9], cube, [18], cube[27], cube[36],
            cube[45]]
    
    for i in range(len(faces) - 1):
        for j in range(i + 1, len(faces)):
            if faces[i] == faces[j]:
                return True
            
    return False

# Input: cubeIn = cube input, value = value input, startingIndex = which face to change
# Changes all the elements on one side of the cube to the same value
# Returns the changed cube
def setValuesInRange(cubeIn, value, startingIndex):
    cube = cubeIn
    for i in range(startingIndex, startingIndex + 9):
        cubeIn[i] = value
        
    return cube
    
# Return true if cube is illegal
def illegalCube(cube=[]):
    if not countUpElements(cube):
        return True

    if not compareAllCorners(cube):
        return True
    
    if not compareAllEdges(cube):
        return True
    
    if not compareAllMiddles(cube):
        return True
    
    return False

def countUpElements(cube=[]):
    colorCounter = {}
    for element in cube:
        if not element in colorCounter:
            colorCounter[element] = 0
        colorCounter[element] += 1
    
    for key in colorCounter:
        if colorCounter[key] != 9:
            return False
    return True







