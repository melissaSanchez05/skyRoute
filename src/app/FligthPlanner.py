from Airport import Airport
from tps.cppTPS import cppTPS
from tps.cppTPS_Transaction import cppTPS_Transaction
from graph.WeightedGraph import WeightedGraph

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


class FlightPlanner():
    def __init__(self):
        self.stops = []
        self.inputStops = []
        self.inputStack = 0
        self.graph = {}
        self.totalTripMilage = []
        tps = cppTPS()

    def displayMenu():
        menu = "ENTER A SELECTION \n"
        menu+= "S) Add a Stop to your Trip \n"
        menu+="U) Undo \n"
        menu+="E) Empty Trip \n"
        menu+="Q) Quit \n"
        mernu+="-"
        return menu
    def initAllAirports():
        pass
    def displayAirports():
        pass
    def processUserInput(self):
        entry = input()
        if entry == "S":
            
            airportId = input("\nEnter the airport ID: \n")
            if not self.graph.nodeExist(airportId):
                print("Invalid airport ID entered \n")
                return True
            if self.inputStops[-1] == airportId:
                print("Airport ID used\n")
                return True
            if not self.graph.hasNeigborNode(airportId):
                print("Airport destination has no connecting flights \n")
                return True
            
            while self.inputStack > 0:
                self.inputStops.pop()
                self.totalTripMilage.pop()
                self.inputStack-=1
            self.inputStack = 0

            transaction = AddStop_Transaction(airportId)
            self.inputStops.append(airportId)
            self.tps.addTransaction(transaction)

        elif entry == "U":
            if (len(self.inputStops) - self.inputStack) > 0:
                self.tps.undoTransaction()
                self.inputStack-=1
            else:
                print("There are not transaction to undo.\n")
        elif entry == "R":
            if self.tps.hasTransactionRedo():
                self.tps.doTransaction()
                self.inputStack-=1
            else:
                 print("There are not transaction to redo.\n")
        elif entry == "E":
            self.tps.clearAllTransactions()
            self.inputStops.clear()
            self.inputStack = 0
        elif entry == "Q":
            return False
        else:
            print("Selection incorrect.\n")

        self.totalTripMilage.clear()
        return True
                
    def displayCurrentTrip(self):
        print("Trip Stops: \n")
        if (len(self.inputStops) - self.inputStack) > 0:

            for i in range(self.inputStack, len(self.inputStops)):
                print(str(i + 1 ) +". " + self.inputStack[i])

        print("\n")
        print("Trip legs: \n")
        if (len(self.inputStops) - self.inputStack) > 1:
            counter = 1
            dash = 0

            for i in range(self.inputStack, len(self.inputStops) - 1):
                route = self.graph.findPath(self.inputStops[i], self.inputStops[i + 1])
                print(str(counter) + ". ")

                for stop in route:
                    print(stop)
                    if (len(route) - 1) > dash:
                        print("-")
                        dash+=1
                print(" ( " + str(self.graph.getDistance()) + " Miles\n")
                self.totalTripMilage.append(self.graph.getDistance())
                counter+=1
                dash = 0
                    
        print("Total distance: \n")
        tripDistance = 0
        for miles in self.totalTripMilage:
            tripDistance+=miles
        
        print(str(tripDistance) + " Miles\n")

    def main():
        pass

    if __name__ == "__main__":
        main()
