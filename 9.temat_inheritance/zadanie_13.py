import random
class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    def print_in_row(array):
        dlug=len(array)
        licz=0
        for c in array:
            licz+=1
            if(dlug==licz):print(c)
            else:print(c,end=".")
    def make_array(number_of_array_elements,
                    value_of_array_elements):
        lista=[]
        for element in range(number_of_array_elements):
            lista.append(value_of_array_elements)
        print(lista)
    def random_array(ile,od,do):
        lista=[]
        for element in range(ile):
            lista.append(random.randint(od,do))
        return lista
    def in_range(array,od,do):
        licz=0
        for element in array:
            if(element<=do and element>=od):licz+=1
        print (licz)
            
    
            
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)
Arrays.make_array(10,4)
Arrays.in_range(Arrays.random_array(20,-7,8),-1,1)


