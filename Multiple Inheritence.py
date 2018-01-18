class mario():

    def move(self):
        print('I am moving')

class shroom():

    def eat_shroom(self):
        print('Now I am Big')

class Bigmario(mario,shroom):
    pass

obj = Bigmario()
obj.move()
obj.eat_shroom()
