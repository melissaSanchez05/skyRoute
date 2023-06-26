from typing import TypeVar
import sys

class WighedEdge:

    def __init__(self, initNode1 : str , initNode2 : str , initWeight : float):
        self.node1 = initNode1
        self.node2 = initNode2
        self.weight = initWeight

    def getNode1(self):
        return self.node1
    
    def getNode2(self):
        return self.node2
    
    def getWeight(self):
        return self.weight
    


class WeightedGraph:
    def __init__(self)->None:
        self.nodes = {} #dict -> map (key, value pair)
        self.edges = {}
        self.totalDistance = 0
    
    def getKeys(self):
        return list(self.nodes.keys())
    def getValues(self):
        return list(self.nodes.values())

    def nodeExist(self, testNode : str) -> bool:
        return testNode in self.nodes.keys()

    def addNode(self, node, data):
        self.nodes[node] = data
        
    def getNodeData(self,node):
        return self.nodes[node]

    def getEdgeId(self,node1 ,node2)-> str:
        return (node1 + "-" + node2)
    
    def addEdge(self,node1 : str ,node2 : str ,weight : float)-> None:
        edgeId = self.getEdgeId(node1,node2)
        self.edges[edgeId] = WighedEdge(node1,node2,weight)

    def removeEdge(self,node1 : str ,node2 : str)-> None:
        edgeId = self.getEdgeId(node1,node2)
        #self.edges.pop(edgeId)
        del self.edges[edgeId]

    def hasNeighbor(self,node1 : str ,node2  :str )-> bool:
        edgeId = self.getEdgeId(node1,node2)
        return edgeId in self.edges.keys()
    
    def hasNeighborNode(self,node1 : str )-> bool:
        for edge in self.edges.values():
            if edge.getNode1() == node1:
                return True
        return False
    def getNeighborWeight(self, node1: str, node2: str)-> float:
        if self.hasNeighbor(node1,node2):
            edgeId = self.getEdgeId(node1,node2)
            return self.edges[edgeId].getWeight()
        
        return 0
    
    def getNeigbors(self,currentNode:str):
        currentNodeNeighbors = []
        for value in self.edges.values():
            if value.getNode1() == currentNode:
                currentNodeNeighbors.append(value)      
        return currentNodeNeighbors
    
    def getDistance(self)-> float:
        return self.totalDistance
    
    def findPath(self, node1, node2):
        if self.nodeExist(node1) and self.nodeExist(node2):
            path = []
            milage = {}
            prevNode = {}
            unvisitedNodes = []
            for keyId in self.nodes.keys():
                prevNode[keyId] = ""
                milage[keyId] = float('inf')
                unvisitedNodes.append(keyId)
            
            milage[node1] = 0.0

            while len(unvisitedNodes) != 0:
                curretNode = ""
                minMilage = float('inf')

                for node in unvisitedNodes:
                    if milage[node] < minMilage:
                        minMilage = milage[node]
                        curretNode = node
                    
                if curretNode == node2:
                    backTrackNode = node2
                    self.totalDistance = minMilage

                    while len(backTrackNode) != 0:
                        path.insert(0, backTrackNode)
                        backTrackNode = prevNode[backTrackNode]
                    return path
                
                #if len(curretnNode) == 0:
                if curretNode == "":
                    #path.insert(0,curretnNode)
                    self.totalDistance = 0
                    return []
                
                unvisitedNodes = [key for key in unvisitedNodes if key != curretNode]

                neighborNodes = self.getNeigbors(curretNode)

                for neighborNode in neighborNodes:
                    if neighborNode.getNode2() in unvisitedNodes:
                        currentNeighborNode = neighborNode.getNode2()
                        currentNeighborMilage = neighborNode.getWeight()
                        totalMilage = milage[curretNode] + currentNeighborMilage

                        if totalMilage < milage[currentNeighborNode]:
                            milage[currentNeighborNode] = totalMilage
                            prevNode[currentNeighborNode] = curretNode


            return []
        else:
            return []

        
            
    

            
            
    
            
            

      