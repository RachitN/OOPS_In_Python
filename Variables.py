class Boy:

    gender ='Male' #class variables

    def __init__(self,name):
        self.name= name  #instance variables

r = Boy('Rachit')
print(r.gender)
print(r.name)