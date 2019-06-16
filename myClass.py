class Player:
    name = None
    height = None
    weight = None

    def count_bmi (self):
        bmi = self.weight / (self.height * self.height)
        return bmi

    
   