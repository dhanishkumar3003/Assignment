from abc import ABC,abstractmethod
class Car(ABC):
    
    @abstractmethod
    def horn(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def startEngine(self):
        pass
    
    @abstractmethod
    def stopEngine(self):
        pass
    
class RollsRoyce(Car):
    def horn(self):
        print("kee kee")
    
    def drive(self):
        print("vrrrm")

    def startEngine(self):
        print("drr")
    
    def stopEngine(self):
        print("krr")
car1=RollsRoyce()
car1.startEngine()
car1.drive()
car1.horn()
car1.stopEngine()