class Positions(Enum):  
    JUNIOR = 10  
    MIDDLE = 15
    SENIOR = 20  
  
  
class Programmer:  
    def __init__(self, name: str, position: Positions, hour_price: int) -> None:
        self.__name = name  
        self.__position = position  
        self.__hour_price = hour_price
  
    def work(self, time: int) -> int:
        self.__time += time  
  
    def rise(self) -> str:
        if self.__position.name == 'JUNIOR':  
            self.__position = Positions.MIDDLE  
  
        elif self.__position.name == 'MIDDLE':  
            self.__position = Positions.SENIOR  
  
        else:  
            self.__hour_price += 2 

    def give_salary(self) -> int:
        self.__time = 0
        salary = self.__hour_price // self.__time
        return salary

    def info(self) -> str:  
        return f'{self.__name}: {self.__time} ч. {self.__give_salary()} тгр.'

