class House:
    def __init__(self, floors):
        self.numberOfFloors = 0
        self.newfloor = floors

    def floor(self):
        print(f'Я нахожусь на {self.numberOfFloors} этаже')

    def setNewNumberOfFloors(self):
        self.newfloor += 1
        print(f'Теперь я на {self.newfloor} этаже')

etazh = House(0)
etazh.floor()
etazh.setNewNumberOfFloors()
