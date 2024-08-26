class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        num_floors = 0
        floors_ = 1
        if floors_ > new_floor or new_floor > self.number_of_floors:
            print('Такого этажа не существует.')
        else:
            while num_floors < new_floor:
                num_floors += 1
                print(num_floors)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h3 = House('Дом', 9)
h3.go_to(9)