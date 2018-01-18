class parent():

    def print_last_name(self):
        print('nagwani')

class child(parent):

    def print_first_name(self):
        print('Rachit')
    def print_last_name(self):  #overriding
         print('Nagwani')

rex = child()
rex.print_first_name()
rex.print_last_name()