class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'
        self.city = "Cracow"
        self.fullname="university of economics in Cracow"

    # object bahaviors (methods)
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,fullname):
        pass
        
    
    def set_name(self,name):
        self.name=name
    def print_name(self):
        print(self.name)
    def print_city(self):
        print(self.city)

a=University()
print(a.name)
a.name="UJ"
University.print_name(a)
University.print_city(a)
University.set_name(a,"MIT")
University.print_name(a)


