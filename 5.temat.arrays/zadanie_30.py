import random
def rand_elem(array):
    return array[random.randint(0,(len(array)-1))]
array=[1,3,6,8,"test"]
for i in range(0,15):
    print(rand_elem(array))