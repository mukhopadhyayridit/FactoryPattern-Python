from abc import ABC, abstractmethod

class Food(ABC):
    pass
    
    
class Chocolate(Food):
    def __init__(self):
        print("the chocolate is made")
        

class Biscuit(Food):
    def __init__(self):
        print("the biscuit is made")
        
class Factory:
    def makefood(self,type):
        if(type == "ch"):
            return Chocolate()
        if(type == "bi"):
            return Biscuit()
        
        
fact = Factory()
chocolate = fact.makefood("ch")
biscuit = fact.makefood("bi")

        
        
    
    

