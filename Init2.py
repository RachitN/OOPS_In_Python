class Enemy:
    def __init__(self,x):
        self.energy=x

    def get_energy(self):
        print(self.energy)

rachit = Enemy(5)
neha = Enemy(18)
rachit.get_energy()
neha.get_energy()

