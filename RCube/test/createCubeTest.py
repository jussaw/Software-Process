'''
Created on Sep 23, 2018
Due Sep 26, 2018
@author: J. Sawyer
@author: D. Umphress
'''
import unittest
import RCube.dispatch as RCube
from RCube.Cube import *



class CreateCubeTest(unittest.TestCase):
    # Tests the creation of a default cube and makes sure the first element
    # of the front face is green
    def test100_620_ShouldCreateMultipleElementCube(self):
        parm = {'op': 'create'}
        expectedResult = 'green'
        actualResult = RCube.createCube(parm)
        print actualResult
        for elementIndex in range(0, 9):
            self.assertEqual(expectedResult, actualResult[elementIndex])
            
    # Tests the creation of a default cube and makes sure that each element of
    # each face is the correct color
    def test100_010_ShouldCreateMultipleFaceCube(self):
        parm = {'op': 'create'}
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        actualResult = RCube.createCube(parm)
        print actualResult
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    # Tests the creation of a cube where all the faces' elements are the letter
    # of their orientation, for instance front is 'f' so all elements on the
    # front face are labeled as 'f'
    def test100_630_ShouldCreateMultipleFaceCubeWithLetterOfSide(self):
        parm = {'op':'create', 'f':'f', 'r':'r', 'b':'b', 'l':'l', 't':'t', 'u':'u'}
        expectedFaces = ['f','r','b','l','t','u']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        print actualResult
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1

    # Tests the creation of a cube where all the faces' elements are the letter
    # of their orientation, for instance front is 'f' so all elements on the
    # front face are labeled as 'f', except we set t to 1 (an integer)
    def test100_640_ShouldCreateMultipleFaces1(self):
        parm = {'op':'create', 'f':'f', 'r':'r', 'b':'b', 'l':'l', 't':'1'}
        expectedFaces = ['f','r','b','l','1','orange']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    # Tests the creation of a cube where one of the parameters for a face
    # is not the correct label for a face to make sure it does not change 
    # anything
    def test100_650_ShouldCreateMultipleFaces3(self):
        parm = {'op':'create', 'f':'f', 'r':'r', 'b':'b', 'l':'l', 't':'1','under':'42'}
        expectedFaces = ['f','r','b','l','1','orange']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
        
    # Tests the creation of a cube where two sides are set to the same value.
    # Should set key cube to value 0
    def test100_660_ShouldCreateMultipleFaces3(self):
        parm = {'op':'create', 'f':'red', 'u':'red'}
        actualResult = RCube.createCube(parm)
        self.assertEqual(0, 0)
        
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0
    def test100_670_ShouldCreateMultipleFaces4(self):
        parm = {'op':'create', 'f':'red'}
        actualResult = RCube.createCube(parm)
        self.assertEqual(0, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

