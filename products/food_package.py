#Write your code here

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
    def pack(self):
        return "Food Wrap Paper"
    def material(self):
        return "Aluminium"

class Bottle(FoodPackage):  
   def pack(self):
        return "Bottle"
    def material(self):
        return "Plastic"
      
class Glass(FoodPackage):  
   def pack(self):
        return "Glass"
    def material(self):
        return "Cardboard"

class Box(FoodPackage):  
   def pack(self):
        return "Box"
    def material(self):
        return "Cardboard"
