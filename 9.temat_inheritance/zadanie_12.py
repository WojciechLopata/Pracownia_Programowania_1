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
            
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)
