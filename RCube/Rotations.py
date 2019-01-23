'''
Created on Oct 28, 2018

@author: justin
'''

def rotateCube(cubeIn, rotateOp):
    cube = cubeIn
    if rotateOp == 'f':
        return rotFrontCW(cube)
    elif rotateOp == 'F':
        return rotFrontCCW(cube)
    elif rotateOp == 'r':
        return rotRightCW(cube)
    elif rotateOp == 'R':
        return rotRightCCW(cube)
    elif rotateOp == 'b':
        return rotBackCW(cube)
    elif rotateOp == 'B':
        return rotBackCCW(cube)
    elif rotateOp == 'l':
        return rotLeftCW(cube)
    elif rotateOp == 'L':
        return rotLeftCCW(cube)
    elif rotateOp == 't':
        return rotTopCW(cube)
    elif rotateOp == 'T':
        return rotTopCCW(cube)
    elif rotateOp == 'u':
        return rotUnderCW(cube)
    elif rotateOp == 'U':
        return rotUnderCCW(cube)

def rotFrontCW(cubeIn):
    cube = cubeIn
    
    topThreeTemp = cube[42:45]
    
    cube[44] = cube[29]
    cube[43] = cube[32]
    cube[42] = cube[35]
    
    cube[29] = cube[45]
    cube[32] = cube[46]
    cube[35] = cube[47]
    
    cube[45] = cube[15]
    cube[46] = cube[12]
    cube[47] = cube[9]
    
    cube[15] = topThreeTemp[2]
    cube[12] = topThreeTemp[1]
    cube[9] = topThreeTemp[0]
    
    rotatedFace = rotFaceCW(cube[0:9])
    
    for i in range(9):
        cube[i] = rotatedFace[i]
        
    return cube

def rotFrontCCW(cubeIn):
    cube = cubeIn
    
    topThreeTemp = cube[42:45]
    
    cube[42] = cube[9]
    cube[43] = cube[12]
    cube[44] = cube[15]
    
    cube[9] = cube[47]
    cube[12] = cube[46]
    cube[15] = cube[45]
    
    cube[47] = cube[35]
    cube[46] = cube[32]
    cube[45] = cube[29]
    
    cube[35] = topThreeTemp[0]
    cube[32] = topThreeTemp[1]
    cube[29] = topThreeTemp[2]
    
    rotatedFace = rotFaceCCW(cube[0:9])
    
    for i in range(9):
        cube[i] = rotatedFace[i]
    
    return cube

def rotRightCW(cubeIn):
    cube = cubeIn
    
    topThreeTemp = [cube[44], cube[41], cube[38]]
    
    cube[44] = cube[8]
    cube[41] = cube[5]
    cube[38] = cube[2]
    
    cube[2] = cube[47]
    cube[5] = cube[50]
    cube[8] = cube[53]
    
    cube[47] = cube[24]
    cube[50] = cube[21]
    cube[53] = cube[18]

    cube[24] = topThreeTemp[2]
    cube[21] = topThreeTemp[1]
    cube[18] = topThreeTemp[0]
    
    rotatedFace = rotFaceCW(cube[9:18])
    
    for i in range(9):
        cube[i + 9] = rotatedFace[i]
        
    return cube

def rotRightCCW(cubeIn):
    cube = cubeIn
    
    topThreeTemp = [cube[44], cube[41], cube[38]]
    
    cube[44] = cube[18]
    cube[41] = cube[21]
    cube[38] = cube[24]
    
    cube[18] = cube[53]
    cube[21] = cube[50]
    cube[24] = cube[47]
    
    cube[53] = cube[8]
    cube[50] = cube[5]
    cube[47] = cube[2]
    
    cube[8] = topThreeTemp[0]
    cube[5] = topThreeTemp[1]
    cube[2] = topThreeTemp[2]
    
    rotatedFace = rotFaceCCW(cube[9:18])
    
    for i in range(9):
        cube[i+9] = rotatedFace[i]
        
    return cube

def rotBackCW(cubeIn):
    cube = cubeIn
    
    topThreeTemp = [cube[38], cube[37], cube[36]]
    
    cube[36] =cube[11]
    cube[37] = cube[14]
    cube[38] = cube[17]
    
    cube[11] = cube[53]
    cube[14] = cube[52]
    cube[17] = cube[51]
    
    cube[53] = cube[33]
    cube[52] = cube[30]
    cube[51] = cube[27]
    
    cube[33] = topThreeTemp[2]
    cube[30] = topThreeTemp[1]
    cube[27] = topThreeTemp[0]
    
    rotatedFace = rotFaceCW(cube[18:27])
    
    for i in range(9):
        cube[i+18] = rotatedFace[i]
        
    return cube

def rotBackCCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[38], cube[37], cube[36]]
    
    cube[38] = cube[27]
    cube[37] = cube[30]
    cube[36] = cube[33]
    
    cube[27] = cube[51]
    cube[30] = cube[52]
    cube[33] = cube[53]
    
    cube[51] = cube[17]
    cube[52] = cube[14]
    cube[53] = cube[11]
    
    cube[17] = topThreeTemp[0]
    cube[14] = topThreeTemp[1]
    cube[11] = topThreeTemp[2]
    
    rotatedFace = rotFaceCCW(cube[18:27])
    
    for i in range(9):
        cube[i+18] = rotatedFace[i]
        
    return cube
    
def rotLeftCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[36], cube[39], cube[42]]
    
    cube[36] = cube[26]
    cube[39] = cube[23]
    cube[42] = cube[20]
    
    cube[20] = cube[51]
    cube[23] = cube[48]
    cube[26] = cube[45]
    
    cube[51] = cube[6]
    cube[48] = cube[3]
    cube[45] = cube[0]
    
    cube[0] = topThreeTemp[0]
    cube[3] = topThreeTemp[1]
    cube[6] = topThreeTemp[2]
    
    rotatedFace = rotFaceCW(cube[27:36])
    
    for i in range(9):
        cube[i+27] = rotatedFace[i]
        
    return cube
    
def rotLeftCCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[36], cube[39], cube[42]]
    
    cube[36] = cube[0]
    cube[39] = cube[3]
    cube[42] = cube[6]
    
    cube[0] = cube[45]
    cube[3] = cube[48]
    cube[6] = cube[51]
    
    cube[51] = cube[20]
    cube[48] = cube[23]
    cube[45] = cube[26]
    
    cube[20] = topThreeTemp[2]
    cube[23] = topThreeTemp[1]
    cube[26] = topThreeTemp[0]
    
    rotatedFace = rotFaceCCW(cube[27:36])
    
    for i in range(9):
        cube[i+27] = rotatedFace[i]
        
    return cube
    
def rotTopCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[20], cube[19], cube[18]]
    
    cube[18] = cube[27]
    cube[19] = cube[28]
    cube[20] = cube[29]
    
    cube[27] = cube[0]
    cube[28] = cube[1]
    cube[29] = cube[2]
    
    cube[0] = cube[9]
    cube[1] = cube[10]
    cube[2] = cube[11]
    
    cube[11] = topThreeTemp[0]
    cube[10] = topThreeTemp[1]
    cube[9] = topThreeTemp[2]
    
    
    rotatedFace = rotFaceCW(cube[36:45])
    
    for i in range(9):
        cube[i+36] = rotatedFace[i]
        
    return cube
    
def rotTopCCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[20], cube[19], cube[18]]
    
    cube[18] = cube[9]
    cube[19] = cube[10]
    cube[20] = cube[11]
    
    cube[11] = cube[2]
    cube[10] = cube[1]
    cube[9] = cube[0]
    
    cube[0] = cube[27]
    cube[1] = cube[28]
    cube[2] = cube[29]
    
    cube[27] = topThreeTemp[2]
    cube[28] = topThreeTemp[1]
    cube[29] = topThreeTemp[0]
    
    rotatedFace = rotFaceCCW(cube[36:45])
    
    for i in range(9):
        cube[i+36] = rotatedFace[i]
        
    return cube
    
def rotUnderCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[6], cube[7], cube[8]]
    
    cube[6] = cube[33]
    cube[7] = cube[34]
    cube[8] = cube[35]
    
    cube[35] = cube[26]
    cube[34] = cube[25]
    cube[33] = cube[24]
    
    cube[26] = cube[17]
    cube[25] = cube[16]
    cube[24] = cube[15]
    
    cube[15] = topThreeTemp[0]
    cube[16] = topThreeTemp[1]
    cube[17] = topThreeTemp[2]
    
    rotatedFace = rotFaceCW(cube[45:54])
    
    for i in range(9):
        cube[i+45] = rotatedFace[i]
        
    return cube
    
def rotUnderCCW(cubeIn):
    cube = cubeIn

    topThreeTemp = [cube[6], cube[7], cube[8]]
    
    cube[6] = cube[15]
    cube[7] = cube[16]
    cube[8] = cube[17]
    
    cube[15] = cube[24]
    cube[16] = cube[25]
    cube[17] = cube[26]
    
    cube[26] = cube[35]
    cube[25] = cube[34]
    cube[24] = cube[33]
    
    cube[33] = topThreeTemp[2]
    cube[34] = topThreeTemp[1]
    cube[35] = topThreeTemp[0]
    
    rotatedFace = rotFaceCCW(cube[45:54])
    
    for i in range(9):
        cube[i+45] = rotatedFace[i]
        
    return cube

def rotFaceCW(faceIn):
    face = []
    face.append(faceIn[6])
    face.append(faceIn[3])
    face.append(faceIn[0])
    face.append(faceIn[7])
    face.append(faceIn[4])
    face.append(faceIn[1])
    face.append(faceIn[8])
    face.append(faceIn[5])
    face.append(faceIn[2])
    return face

def rotFaceCCW(faceIn):
    face = []
    face.append(faceIn[2])
    face.append(faceIn[5])
    face.append(faceIn[8])
    face.append(faceIn[1])
    face.append(faceIn[4])
    face.append(faceIn[7])
    face.append(faceIn[0])
    face.append(faceIn[3])
    face.append(faceIn[6])
    return face