class House:
    def __init__(self):
        self.numberOfFloors = [0]

    def set_new_number_of_floors(self, floors):
        print('Этаж:', floors)
        for floors in self.numberOfFloors:
            print('Следующий этаж:', floors)


house = House()
house.set_new_number_of_floors(floors=2)
