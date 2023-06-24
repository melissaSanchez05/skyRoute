from typing import TypeVar
import sys

class WeighedEdge:

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
    
T = TypeVar('T')
INF = sys.float_info.max

class WeightedGraph:
    totalDistance = 0
    def __init__(self)->None:
        self.nodes = {} #dict -> map (key, value pair)
        self.edges = {}
        self.totalDistance = 0
    
    def getKeys(self):
        return list(self.nodes.keys())

    def nodeExist(self, testNode : str) -> bool:
        return testNode in self.nodes.keys()

    def addNode(self, node : str, data : T):
        self.nodes[node] = data
        
    def getNodeData(self,node : str)-> T:
        self.nodes.get(node)

    def getEdgeId(self,node1 : str ,node2 : str)-> str:
        return (node1 + "-" + node2)
    
    def addEdge(self,node1 : str ,node2 : str ,weight : float)-> None:
        edgeId = self.getEdgeId(node1,node2)
        self.edges[edgeId] = WeighedEdge(node1,node2,weight)

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
    
    def findPath(self, node1: str, node2: str) -> []:
        if self.nodeExist(node1) and self.nodeExist(node2):
            path = []
            milage = {}
            prevNode = {}
            unvisitedNodes = []
            for keyId in self.nodes.keys():
                prevNode[keyId] = ""
                milage[keyId] = INF
                unvisitedNodes.append(keyId)
            
            milage[keyId] = 0

            while len(unvisitedNodes) != 0:
                curretnNode = ""
                minMilage = INF

                for node in unvisitedNodes:
                    if milage[node] < minMilage:
                        minMilage = milage[node]
                        curretnNode = node
                    
                if curretnNode = node2:
                    backTrackNode = node2
                    self.totalDistance = minMilage

                    while len(backTrackNode) != 0:
                        path.insert(0, backTrackNode)
                        backTrackNode = prevNode[backTrackNode]

                    return path
                
                if len(curretnNode) == 0:
                    path.insert(0,curretnNode)
                    self.totalDistance = 0
                    return []
                
                unvisitedNodes = [i for i in unvisitedNodes if i != curretnNode]

                neighborNodes = self.getNeigbors(curretnNode)

                for neighborNode in neighborNodes:
                    if neighborNode.getNode2() in unvisitedNodes:
                        currentNeighborNode = neighborNode.getNode2()
                        currentNeighborMilage = neighborNode.getWeight()
                        totalMilage = milage[curretnNode] + currentNeighborMilage

                        if totalMilage < milage[currentNeighborNode]:
                            milage[currentNeighborNode] = totalMilage
                            prevNode[currentNeighborNode] = curretnNode


            return []
                



        return []

        
            
    

            
            
    
            
            

      