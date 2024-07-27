class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Введенного этажа не существует")
        else:
            print("Этажи, пройденные вами:")
            for i in range(1, new_floor + 1):
                print(i)


build = House("Библиотека", 13)
build.go_to(13)