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
        totalMilage = 0
        tps = cppTPS()

    def displayMenu():
        pass
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
            self.tps.undoTransaction()
            self.inputStack-=1
        elif entry == "R":
            if self.tps.hasTransactionRedo():
                self.tps.doTransaction()
                self.inputStack-=1
        elif entry == "E":
                
    def displayCurrentTrip():
        pass

    def main():
        pass

    if __name__ == "__main__":
        main()
