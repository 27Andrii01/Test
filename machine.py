"""Machine"""
    
class TextMachine:
    def __init__(self, text1:tuple, text2:tuple) -> None:
        """
        Module is a class constructor
        """
        self.text1 = text1
        self.text2 = text2

    def is_empty(self):
        if len(self.text1) == 0 and len(self.text2) == 0:
            return True
        return False

    def texts_count(self):
        """
        Module return first elements from two tuples
        """
        return (self.text1[0], self.text2[0])
    

    def still_owe(self):
        """
        Module return second elements from two tuples
        """
        return (self.text1[1], self.text2[1])

    def insert_money(self, user_input: tuple):
        """"""
        change = 0
        if user_input[0] < 0:
            return 'You cant take money from machine!'
        if user_input[1] == 'short':
            txt  =  f'Still owe ₴{(self.still_owe()[0] - user_input[0])/100}'
            change += user_input[0]
            return tuple(txt, change)


    def stock_machine(self):
        pass

    def railway_station_machine(self):
        pass
    
    def __str__(self) -> str:
        """
        Module
        """
        return f"Text Machine:<{self.text1[0]} texts; ₴{self.text1[1]/100} each>; <{self.text2[0]} texts; ₴{self.text2[1]/100} each>"
    

class VendingMachine(TextMachine):
    def __init__(self, text1: tuple, text2: tuple) -> None:
        super().__init__(text1, text2)
