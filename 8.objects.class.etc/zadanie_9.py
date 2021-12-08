class University():

    # object constructor (__init__ method)
    def __init__(self,name,fullname):
        self.name=name
        self.fullname=fullname
        # object states/attributes (fields)

    # object bahaviors (methods)
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,fullname):
        self.fullname=fullname
    def set_name(self,name):
        self.name=name
    def print_name(self):
        print(self.name)
    def print_city(self):
        print(self.city)

studia=University("Cue","University of economics in Cracow")
University.print_name(studia)
University.print_fullname(studia)
University.set_name(studia,"AGH" )
University.set_fullname(studia,"Akademia górniczo hutnicza")
University.print_name(studia)
University.print_fullname(studia)



