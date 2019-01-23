'''
Created on Sep 23, 2018
Due Sep 26, 2018
@author: J. Sawyer
@author: D. Umphress
'''
import unittest
import httplib
import json

class DispatchTest(unittest.TestCase):
        
    def setUp(self):
        self.key = "status"
        self.errorValue = "error:"
        self.operation ="op"
        self.scramble ="create"

    @classmethod
    def setUpClass(cls):
        cls.ERROR = "error:"
        cls.DEFAULT_SIZE = 3
        cls.MICROSERVICE_PATH = "/rcube?"
        cls.MICROSERVICE_URL="127.0.0.1"
        cls.MICROSERVICE_PORT = 5000
#         cls.MICFROSERVICE_URL="umphrda-rcube.mybluemix.net"
#         cls.MICROSERVICE_PORT = 80
        
    def httpGetAndResponse(self, queryString):
        '''Make HTTP request to URL:PORT for /rcube?querystring; result is a JSON string'''
        try:
            theConnection = httplib.HTTPConnection(self.MICROSERVICE_URL, self.MICROSERVICE_PORT)
            theConnection.request("GET", self.MICROSERVICE_PATH + queryString)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse 
        except Exception as e:
            theStringResponse = "{'diagnostic': 'error: " + str(e) + "'}"
            return theStringResponse
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result
        
#Acceptance Tests
#
# 100 dispatch - basic functionality
# Desired level of confidence: boundary value analysis
# Analysis 
# inputs:     http:// ...myURL... /httpGetAndResponse?parm
#            parm is a string consisting of key-value pairs
#            At a minimum, parm must contain one key of "op"
#
# outputs:    A JSON string containing, at a minimum, a key of "status"
#
# Happy path 
#      input:   parm having at least one element with a key of "op"        
#      output:  JSON string containing a key of "status" 
#
# Sad path 
#      input:   no string       
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#      input:   valid parm string with at least one key-value pair, no key of "op"
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#
#
# Note:  These tests require an active web service
#
#
# Happy path
    def test100_010_ShouldReturnSuccessKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        
    
    
    
    # Sad path
    
    def test100_900_ShouldReturnErrorOnEmptyParm(self):
        queryString=""
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
    
    def test100_910_ShouldReturnErrorOnMissingOp(self):
        queryString="f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])


# Acceptance Tests
#
# 200 dispatch -- op=create
#Desired level of confidence is bVA
# Analysis
#    inputs: http://...myURL.../rcube?op=create<options>
#        where <options> can be zero or one of:
#             "f"    Specifies the color of the front side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "green" if missing.  Arrives unvalidated.        
#             "r"    Specifies the color of the right side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "yellow" if missing.  Arrives unvalidated.        
#             "b"    Specifies the color of the back side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "blue" if missing.  Arrives unvalidated.        
#             "l"    Specifies the color of the top side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "white" if missing.  Arrives unvalidated.        
#             "t"    Specifies the color of the under side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "red" if missing.  Arrives unvalidated.        
#             "u"    Specifies the color of the front of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "orange" if missing.  Arrives unvalidated.        
#    outputs:    A JSON string containing, at a minimum, a key "status

# HAppy path
#    input: zero options
#        http://...myURL.../rcube?op=create
#    output:    default model cube, which is a JSON String
#         '{'status': 'created', 'cube': ['green',  'green', 'green', 
#                                         'green', 'green', 'green', 
#                                         'green', 'green', 'green', 
#                                         'yellow', 'yellow', 'yellow', 
#                                         'yellow', 'yellow', 'yellow', 
#                                         'yellow', 'yellow', 'yellow',  
#                                         'blue', 'blue', 'blue', 
#                                         'blue', 'blue', 'blue', 
#                                         'blue', 'blue', 'blue', 
#                                         'white', 'white', 'white', 
#                                         'white', 'white', 'white', 
#                                         'white', 'white', 'white', 
#                                         'red', 'red', 'red', 
#                                         'red', 'red', 'red', 
#                                         'red', 'red', 'red', 
#                                         'orange', 'orange', 'orange', 
#                                         'orange', 'orange', 'orange', 
#                                         'orange', 'orange', 'orange']}

    def test200_010_ShouldCreateDefaultCubeStatus(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('full', resultDict['status'])
        
        
        
        
    def test200_020_ShouldCreateDefaultCubeKey(self):
        queryString = "op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)
    
    # Tests the creation of a default cube and makes sure that each element of
    # each face is the correct color
    def test_200_130_ShouldCreateDefaultCubeValue(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[actualFaceIndex])
                actualFaceIndex += 1
                
    # Tests the creation of a cube where all the faces' elements are the letter
    # of their orientation, for instance front is 'f' so all elements on the
    # front face are labeled as 'f'        
    def test100_630_ShouldCreateMultipleFaceCubeWithLetterOfSide(self):
        queryString = "op=create&r=r&l=l&t=t&u=u&f=f&b=b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','t','u']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[actualFaceIndex])
                actualFaceIndex += 1
    
    # Tests the creation of a cube where all the faces' elements are the letter
    # of their orientation, for instance front is 'f' so all elements on the
    # front face are labeled as 'f', except we set t to 1 (an integer)
    def test100_640_ShouldCreateMultipleFaceCubeWithLetterOfSide2(self):
        queryString = "op=create&f=f&r=r&b=b&l=l&t=1"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','1','orange']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[actualFaceIndex])
                actualFaceIndex += 1
    
    # Tests the creation of a cube where one of the parameters for a face
    # is not the correct label for a face to make sure it does not change 
    # anything
    def test100_650_ShouldCreateMultipleFaceCubeWithLetterOfSide3(self):
        queryString = "op=create&f=f&r=r&b=b&l=l&t=1&under=42"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','1','orange']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0, 9):
                self.assertEqual(face, actualResult[actualFaceIndex])
                actualFaceIndex += 1

    # Tests the creation of a cube where two sides are set to the same value.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_660_ShouldTryToCreateTwoFacesWithDuplicateColors(self):
        queryString = "op=create&f=red&u=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        errorMessage = "error: at least two faces have the same color"
        self.assertEqual(errorMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_670_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=create&f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        errorMessage = "error: at least two faces have the same color"
        self.assertEqual(errorMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_680_ShouldTryToCreateFull(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "full"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_690_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=create&f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: at least two faces have the same color"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_700_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=check&cube=y,y,y,y,r,y,y,y,y,o,o,o,o,b,o,o,o,o,w,w,w,w,o,w,w,w,w,r,r,r,r,g,r,r,r,r,b,b,b,b,w,b,b,b,b,g,g,g,g,y,g,g,g,g"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "spots"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_710_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=check&f=w&r=g&b=r&l=b&t=r&u=o&cube=r,w,r,w,w,w,r,w,r,w,g,w,g,g,g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b,b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "crosses"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_720_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=check&f=2&r=o&b=g&l=r&t=b&u=y&cube=y,y,b,b,o,g,o,b,w,r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: cube is not sized properly"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_730_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=create&f=&r=r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: face color is missing"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_740_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,b,f,f,f,r,r,r,r,r,r,r,r,r,f,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: illegal cube"
        self.assertEqual(statusMessage, resultDict['status'])

    ''' ASSIGNMENT 6 '''

    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_750_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=F"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "rotated"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_760_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "rotated"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_770_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=rotate"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: cube must be specified"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_780_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: face is unknown"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_790_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: face is missing"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_800_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=scramble"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "scrambled"
        self.assertEqual(statusMessage, resultDict['status'][0:9])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_810_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=scramble&n=1"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "scrambled"
        self.assertEqual(statusMessage, resultDict['status'][0:9])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_820_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=scramble&method=none"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: method is unknown"
        self.assertEqual(statusMessage, resultDict['status'])
        
    # Tests the creation of a cube where one face is set to a color that
    # another face is set to by default.
    # Should set key cube to value 0, and status is updated as needed.
    def test100_830_ShouldTryToCreateTwoFacesWithDuplicateColors2(self):
        queryString = "op=scramble&n=999"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        statusMessage = "error: n is invalid"
        self.assertEqual(statusMessage, resultDict['status'])
        
        
        
    
