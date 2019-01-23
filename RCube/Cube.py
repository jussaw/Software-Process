'''
Created on Oct 13, 2018

@author: justin
'''
from Face import *
import Rotations
import random
from __builtin__ import int

class Cube(object):

    def __init__(self, cubeStrListIn):
        self.cubeStrList = cubeStrListIn
        #self.facesList = self.createFacesList()
        
    def setCube(self, cubeIn):
        self.cubeStrList = cubeIn
    
    # Input: parm = parameters for cube, cubeIn = cube to be changed
    # If there was duplicate colors, then return 0
    # Returns the changed cube
    def changeCube(self, parm={}):
        usedValues = []
        for key, value in parm.items():
            
            if key == 'f':
                self.setValuesInRange(value, 0)
            elif key == 'r':
                self.setValuesInRange(value, 9)
            elif key == 'b':
                self.setValuesInRange(value, 18)
            elif key == 'l':
                self.setValuesInRange(value, 27)
            elif key == 't':
                self.setValuesInRange(value, 36)
            elif key == 'u':
                self.setValuesInRange(value, 45)
            
            usedValues.append(value)
    
    # Takes in input for current value and usedValues
    # Returns true if the value of valueIn is in usedValuesIn
    def duplicateFound(self):
        faces = [self.cubeStrList[4], self.cubeStrList[13], 
                 self.cubeStrList[22], self.cubeStrList[31],
                 self.cubeStrList[40], self.cubeStrList[49]]
        facesDict = {}
        
        for face in faces:
            if(face not in facesDict):
                facesDict[face] = 0
                
            facesDict[face] += 1
            
            if facesDict[face] > 1:
                return True        
            
        return False
    
    # Input: cubeIn = cube input, value = value input, startingIndex = which face to change
    # Changes all the elements on one side of the cube to the same value
    # Returns the changed cube
    def setValuesInRange(self, value, startingIndex):
        for i in range(startingIndex, startingIndex + 9):
            self.cubeStrList[i] = value
    
    def createFace(self, elements=[]):
        if len(elements) == 9:
            face = Face(elements)
        return face
    
    def createFacesList(self):
        facesList = []
        if len(self.cubeStrList) == 54:
            faceF = Face(self.cubeStrList[0, 9])
            faceR = Face(self.cubeStrList[9, 18])
            faceB = Face(self.cubeStrList[18, 27])
            faceL = Face(self.cubeStrList[27, 36])
            faceT = Face(self.cubeStrList[36, 45])
            faceU = Face(self.cubeStrList[45, 54])
            
            facesList = [faceF, faceR, faceB, faceL, faceT, faceU]
        
        return facesList
    
    
    def checkForFullFaces(self, cube=[]):
        if len(cube) == 54:
            for i in range(0, 54, 9):
                for j in range(i, i+9-1):
                    for k in range(j + 1, i+9-1):
                        if cube[j] != cube[k]:
                            return False
            return True
        return False
    
    def checkIfAllSame(self, cube=[]):
        for i in range (len(cube) - 1):
            for j in range(i, len(cube)):
                if cube[i] != cube[j]:
                    return False
        return True
    
    
    def checkForSpots(self, face=[]):
        facesNoMiddle = face[0:4]
        facesNoMiddle.append(face[5])
        facesNoMiddle.append(face[6])
        facesNoMiddle.append(face[7])
        facesNoMiddle.append(face[8])
        
        if self.checkIfAllSame(facesNoMiddle) and face[4] != face[0]:
            return True
        return False
    
    def checkForSpotsAllFaces(self, cube=[]):
        face1 = cube[0:9]
        face2 = cube[9:18]
        face3 = cube[18:27]
        face4 = cube[27:36]
        face5 = cube[46:45]
        face6 = cube[45:54]
        faces = [face1, face2, face3, face4, face5, face6]
        
        for face in faces:
            if not self.checkForSpots(face):
                return False
        return True
    
    def checkForCrosses(self, cube=[]):
        face1 = cube[0:9]
        face2 = cube[9:18]
        face3 = cube[18:27]
        face4 = cube[27:36]
        face5 = cube[36:45]
        face6 = cube[45:54]
        faces = [face1, face2, face3, face4, face5, face6]
        
        for face in faces:
            if not self.checkForCrossesFace(face):
                return False
        
        return True
    
    def checkForCrossesFace(self, face=[]):
        corners = []
        corners.append(face[0])
        corners.append(face[2])
        corners.append(face[6])
        corners.append(face[8])
        
        cross = []
        cross.append(face[1])
        cross.append(face[3])
        cross.append(face[4])
        cross.append(face[5])
        cross.append(face[7])
        
        if self.checkIfAllSame(corners) and self.checkIfAllSame(cross) and corners[0] != cross[0]:
            return True
        
        return False
    
    def calculateRandomness(self, cube):
        total = 0.0
        
        for i in range(0, 54, 9):
            for j in range(i, i + 8):
                for k in range(j + 1, i + 9):
                    if cube[j] == cube[k]:
                        total += 1
                        
        total /= 216.0
        total *= 100.0
        
        return int(round(total))
    
    def scramble(self, cubeIn, method, n):
        n = int(n)
        cube = cubeIn[:]
        if method == 'random':
            randomness, rotations = self.scrambleRandom(cube, n)
            return randomness, rotations
        
        if method == 'transition':
            randomness, rotations = self.scrambleTransition(cube, n)
            return randomness, rotations
        
    
    def scrambleRandom(self, cubeIn, n):
        cube = cubeIn[:]
        possibleRotations = ['f','F','r','R','b','B','l','L','t','T','u','U']
        rotations = []
        
        if n == 0:
            randomness = self.calculateRandomness(cube)
            return randomness, rotations
        
        for i in range(n):
            rotInt = random.randint(0, len(possibleRotations) - 1)
            rot = possibleRotations[rotInt]
            
            cube = Rotations.rotateCube(cube, rot)
            
            rotations.append(rot)
            
        randomness = self.calculateRandomness(cube)
        return randomness, rotations
    
    def scrambleTransition(self, cubeIn, n):
        cube = cubeIn[:]
        randomness = 0
        rotations = []
        
        for i in range(n):
            rotation = self.determineBestTransition(cube)
            cube = Rotations.rotateCube(cube, rotation)
            rotations.append(rotation)
        
        randomness = self.calculateRandomness(cube)
        return randomness, rotations
    
    def determineBestTransition(self, cubeIn):
        possibleRotations = ['f','F','r','R','b','B','l','L','t','T','u','U']
        bestRotation = 'f'
        lowestRandomScore = 100
        
        for rotation in possibleRotations:
            cube = cubeIn[:]
            cube = Rotations.rotateCube(cube, rotation)
            currentScore = self.calculateRandomness(cube)
            
            if currentScore < lowestRandomScore:
                bestRotation = rotation
                lowestRandomScore = currentScore
        
        return bestRotation
        
    
    
    
    
            
    
    
    
