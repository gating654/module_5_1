class House:
    def __init__(self, name, nof):
        self.name = name
        self.number_of_floors = int(nof)

    def go_to(self, new_floor):
        for i in range(1, int(new_floor)+1):
            if 1 < new_floor > self.number_of_floors:
                return print("Такого этажа не существует")
            print(i)

h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)
h1.go_to(5)
h2.go_to(10)

