'''
Created on Oct 13, 2018

@author: justin
'''

class Face(object):
    
    def __init__(self, elementsIn=[]):
        self.element0 = elementsIn[0]
        self.element1 = elementsIn[1]
        self.element2 = elementsIn[2]
        self.element3 = elementsIn[3]
        self.element4 = elementsIn[4]
        self.element5 = elementsIn[5]
        self.element6 = elementsIn[6]
        self.element7 = elementsIn[7]
        self.element8 = elementsIn[8]
    
    def checkForFullFace(self):
        elements = [self.element0, self.element1, self.element2, 
                    self.element3, self.element4, self.element5, 
                    self.element6, self.element7, self.element8]
        elementDict = {}
        
        for element in elements:
            if element not in elementDict:
                elementDict[element] = 0
        
        if len(elementDict) > 1:
            return False
        return True
            
        
        