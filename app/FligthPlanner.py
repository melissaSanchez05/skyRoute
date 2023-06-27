import asyncio
from Airport import Airport
from WeightedGraph import WeightedGraph
from cppTPS import cppTPS, cppTPS_Transaction


class AddStop_Transaction(cppTPS_Transaction):

    def __init__(self, initStops, initcode):
        super().__init__()
        self.code = initcode
        self.tripStops = initStops
    
    def doTransaction(self) -> None:
        self.tripStops.append(self.code)

    def undoTransaction(self) -> None:
        self.tripStops.pop()
    
    def __str__(self) -> str:
        return "Adding a stop"



stops  = []
inputStops  = []
inputStack  = 0
AirportGraph  = WeightedGraph()
totalTripMilage = []
tps = cppTPS()

def main():
    initAllAirports()
    keepGoing = True
    while keepGoing:
        displayAirports()
        displayCurrentTrip()
        displayMenu()
        keepGoing = processUserInput()
    print("GOODBYE")



def displayMenu()-> str:
    menu = "ENTER A SELECTION \n"
    menu+= "S) Add a Stop to your Trip \n"
    menu+="U) Undo \n"
    menu+="R) Redo \n"
    menu+="E) Empty Trip \n"
    menu+="Q) Quit \n"
    menu+="-"
    print(menu)
def initAllAirports():
    AirportGraph.addNode("AUS",  Airport("AUS", 30, 18, 97, 42))
    AirportGraph.addNode("AVL",  Airport("AVL", 36, 00, 82, 32))
    AirportGraph.addNode("BGR",  Airport("BGR", 44, 48, 68, 40))
    AirportGraph.addNode("BOS",  Airport("BOS", 42, 22, 71, 2))
    AirportGraph.addNode("BUF",  Airport("BUF", 42, 56, 78, 44))
    AirportGraph.addNode("BVT",  Airport("BVT", 44, 28, 73, 9))
    AirportGraph.addNode("CLE",  Airport("CLE", 41, 24, 81, 81))
    AirportGraph.addNode("COD",  Airport("COD", 44, 33, 109, 4))
    AirportGraph.addNode("DCA",  Airport("DCA", 38, 51, 77, 2))
    AirportGraph.addNode("DEN",  Airport("DEN", 39, 45, 104, 52))
    AirportGraph.addNode("DFW",  Airport("DFW", 32, 51, 96, 51))
    AirportGraph.addNode("ELP",  Airport("ELP", 31, 48, 106, 24))
    AirportGraph.addNode("HOU",  Airport("HOU", 29, 59, 95, 22))
    AirportGraph.addNode("IND",  Airport("IND", 39, 44, 86, 17))
    AirportGraph.addNode("JAX",  Airport("JAX", 30, 30, 81, 42))
    AirportGraph.addNode("LAX",  Airport("LAX", 33, 56, 118, 24))
    AirportGraph.addNode("LGA",  Airport("LGA", 40, 47, 73, 58))
    AirportGraph.addNode("LIT",  Airport("LIT", 34, 44, 92, 14))
    AirportGraph.addNode("MCI",  Airport("MCI", 39, 7, 94, 35))
    AirportGraph.addNode("MIA",  Airport("MIA", 25, 48, 80, 16))
    AirportGraph.addNode("MKE",  Airport("MKE", 42, 87, 87, 74))
    AirportGraph.addNode("MOT",  Airport("MOT", 48, 25, 101, 21))
    AirportGraph.addNode("MSY",  Airport("MSY", 29, 59, 90, 15))
    AirportGraph.addNode("OMA",  Airport("OMA", 41, 30, 95, 80))
    AirportGraph.addNode("PHX",  Airport("PHX", 33, 26, 112, 1))
    AirportGraph.addNode("PWM",  Airport("PWM", 43, 39, 70, 19))
    AirportGraph.addNode("SFO",  Airport("SFO", 37, 46, 122, 26))
    AirportGraph.addNode("SEA",  Airport("SEA", 47, 39, 122, 18))
    AirportGraph.addNode("SLC",  Airport("SLC", 40, 46, 111, 58))
    AirportGraph.addNode("VGT",  Airport("VGT", 36, 5, 115, 10))

    initEdge("AUS", "DFW")
    initEdge("AVL", "IND")
    initEdge("BOS", "PWM")
    initEdge("BUF", "CLE")
    initEdge("BVT", "BGR")
    initEdge("CLE", "IND")
    initEdge("CLE", "MKE")
    initEdge("COD", "MOT")
    initEdge("COD", "SEA")
    initEdge("COD", "DEN")
    initEdge("DCA", "AVL")
    initEdge("DCA", "JAX")
    initEdge("DEN", "DFW")
    initEdge("DEN", "ELP")
    initEdge("DFW", "HOU")
    initEdge("ELP", "PHX")
    initEdge("HOU", "LIT")
    initEdge("IND", "MKE")
    initEdge("JAX", "AVL")
    initEdge("LAX", "MIA")
    initEdge("LAX", "SFO")
    initEdge("LAX", "VGT")
    initEdge("LGA", "IND")
    initEdge("LGA", "DCA")
    initEdge("LGA", "BOS")
    initEdge("LGA", "MIA")
    initEdge("MCI", "DEN")
    initEdge("MCI", "DFW")
    initEdge("MCI", "IND")
    initEdge("MCI", "OMA")
    initEdge("MIA", "BOS")
    initEdge("MIA", "JAX")
    initEdge("MIA", "MSY")
    initEdge("MKE", "MOT")
    initEdge("MOT", "SEA")
    initEdge("MOT", "DEN")
    initEdge("MOT", "IND")
    initEdge("MSY", "JAX")
    initEdge("MSY", "IND")
    initEdge("OMA", "DEN")
    initEdge("OMA", "MOT")
    initEdge("OMA", "IND")
    initEdge("PHX", "LAX")
    initEdge("PWM", "BVT")
    initEdge("PWM", "BGR")
    initEdge("SFO", "VGT")
    initEdge("SFO", "DEN")
    initEdge("SFO", "SEA")
    initEdge("SLC", "SFO")
    initEdge("SLC", "DEN")
    initEdge("SLC", "SEA")
    initEdge("VGT", "PHX")


def initEdge(node1, node2):
    a1 : Airport = AirportGraph.getNodeData(node1)   
    a2 = AirportGraph.getNodeData(node2) 
    dis= Airport.calculateDistance(a1,a2)
    AirportGraph.addEdge(node1,node2,dis)
    AirportGraph.addEdge(node2,node1,dis)

def displayAirports():

    print("AIRPORTS YOU CAN TRAVEL TO AND FROM: \n")
    codes = AirportGraph.getKeys()
    for i in range(len(codes)):
        if (i % 10) == 0:
            print("\t", end="")
        print(str(codes[i]), end="")
        if i < (len(codes) - 1):
            print(", ",end="")
        if (i % 10) == 9:
            print()
    print("\n\n")
def processUserInput()-> bool:
    global inputStack
    global totalTripMilage
    global AirportGraph
    global inputStops
    global tps

    entry = input("Enter Selection: ")
    if entry == "S":
        
        airportId = input("Enter the airport ID: ")
        if not AirportGraph.nodeExist(airportId):
            print("Invalid airport ID entered")
            return True
        if (len(inputStops)>0) and (inputStops[-1] == airportId):
            print("Airport ID used")
            return True
        if not AirportGraph.hasNeighborNode(airportId):
            print("Airport destination has no connecting flights")
            return True
        if inputStack > 0:
            while inputStack > 0:
                inputStops.pop()
                totalTripMilage.pop()
                inputStack-=1
            inputStack = 0

        transaction = AddStop_Transaction(inputStops,airportId)
        inputStops.append(airportId)
        tps.addTransaction(transaction)

    elif entry == "U":
        if ((len(inputStops) - inputStack) > 0):
            tps.undoTransaction()
            inputStack+=1
        else:
            print("There are not transaction to undo.")
    elif entry == "R":
        if inputStack > 0:
            tps.doTransaction()
            inputStack-=1
        else:
            print("There are not transaction to redo.")
            print("printing redo from tps: " + str(tps.hasTransactionRedo()))
    elif entry == "E":
        tps.clearAllTransactions()
        inputStops.clear()
        inputStack = 0
    elif entry == "Q":
        return False
    else:
        print("Selection incorrect. Please try again. \n")

    totalTripMilage.clear()
    return True
            
def displayCurrentTrip():
    global inputStack
    global totalTripMilage
    global AirportGraph
    global inputStops



    print("Trip Stops: ")
    if (len(inputStops) - inputStack) > 0:

        for i in range(len(inputStops) - inputStack):
            print(str(i + 1 ) +". " + inputStops[i])
    print()
    print("Trip legs: ")
    if (len(inputStops) - inputStack) > 1:
        counter = 1
        dash = 0

        for i in range(len(inputStops) - inputStack - 1):
            route = AirportGraph.findPath(inputStops[i], inputStops[i + 1])
            print(str(counter) + ". ", end="")

            for stop in route:
                print(stop, end="")
                if (len(route) - 1) > dash:
                    print("-", end="")
                    dash+=1
            print(" ( " + str(AirportGraph.getDistance()) + " Miles)")
            totalTripMilage.append(AirportGraph.getDistance())
            counter+=1
            dash = 0
    print()           
    print("Total distance: ", end="")
    tripDistance = 0
    for miles in totalTripMilage:
        tripDistance+=miles
    
    print(str(tripDistance) + " Miles")
    print()

if __name__ == "__main__":
    main()