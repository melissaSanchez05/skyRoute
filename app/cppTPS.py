class cppTPS_Transaction:

    def doTransaction(self) -> None:
            pass
    def undoTransaction(self) -> None:
        pass
    def __str__(self) -> str:
        pass

class cppTPS:
    def __init__(self):
        self.performingDo = False
        self.performingUndo = False
        self.mostRecentTransactions  = -1
        self.transactions : list[cppTPS_Transaction]= []
   
    def isPerformingDo(self) -> bool:
        return self.performingDo
        
    def isPerformingUndo(self) -> bool:
        return self.performingUndo
    
    def hasTransactionRedo(self) -> bool:
        return (self.mostRecentTransactions <  (len(self.transactions) - 1))
    
    def hasTransactionUndo(self) -> bool:
        return (self.mostRecentTransactions >= 0)
    
    def getSize(self) -> int :
        return len(self.transactions)
    
    def getRedoSize(self) -> int:
        return (self.getSize - (self.mostRecentTransactions - 1))
    
    def getUndoSize(self) -> int:
        return self.mostRecentTransactions + 1
    
    def addTransaction(self, transaction : cppTPS_Transaction) -> None:
        if self.mostRecentTransactions < 0 or (self.mostRecentTransactions < (len(self.transactions) - 1)):
            
            while self.mostRecentTransactions > 0:
                self.transactions.pop()
                self.mostRecentTransactions-=1
        else:
            self.mostRecentTransactions+=1
            self.transactions.append(transaction)
    
    def doTransaction(self) -> None:
        if self.hasTransactionRedo() :
            self.performingDo = True
            transaction = cppTPS_Transaction()
            transaction.doTransaction()
            self.mostRecentTransactions+=1
            self.performingDo = False

    
    def undoTransaction(self) -> None:
        if self.hasTransactionUndo() :
            self.performingUndo = True
            transaction = cppTPS_Transaction()
            transaction.undoTransaction()
            self.mostRecentTransactions-=1
            self.performingUndo = False

    def clearAllTransactions(self): #fix this method?
        for transaction in self.transactions:
            self.transactions.remove(transaction)
        self.transactions.clear()
        self.mostRecentTransactions = -1
    
    def __str__ (self) -> str: #fix this method
      text = "__Number of transactions: " + str(self.getSize) + "\n"
      text+= "__Current index on stack: " + str(self.mostRecentTransactions) + "\n"
      text+= "_Current transaction stack: \n"
      for i in range(self.mostRecentTransactions + 1):
          pyTPS = self.transactions[i]
          text+= "----" + pyTPS.__str__() + "\n"
      
      return text
        