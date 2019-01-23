'''
Created on Oct 13, 2018

@author: justin
'''

# return true if all edges are unique
def compareAllEdges(cube=[]):
    edges = createEdges(cube)
    for i in range(len(edges) - 1):
        for j in range(i + 1, len(edges)):
            if compareEdges(edges[i], edges[j]):
                return False
    return True

def createEdges(cube=[]):
    edge1 = [cube[1], cube[43]]
    edge2 = [cube[41], cube[10]]
    edge3 = [cube[37], cube[19]]
    edge4 = [cube[28], cube[39]]
    edge5 = [cube[3], cube[32]]
    edge6 = [cube[5], cube[12]]
    edge7 = [cube[14], cube[21]]
    edge8 = [cube[30], cube[23]]
    edge9 = [cube[7], cube[46]]
    edge10 = [cube[16], cube[50]]
    edge11 = [cube[25], cube[52]]
    edge12 = [cube[34], cube[48]]
    
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12]

    return edges

#return true if edges are equal
def compareEdges(edge1=[], edge2=[]):
    edge1Dict = {}
    edge2Dict = {}
    
    for element in edge1:
        if not element in edge1Dict:
            edge1Dict[element] = 0
        edge1Dict[element] += 1
        
    for element in edge2:
        if not element in edge2Dict:
            edge2Dict[element] = 0
        edge2Dict[element] += 1
    
    sameEdge = cmp(edge1Dict, edge2Dict)
    if sameEdge == 0:
        return True
    return False











