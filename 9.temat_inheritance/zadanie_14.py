class areas():

    @staticmethod
    def circle(radius):
        return radius**2*3.14153
    def rectangle(a,b):
        return a*b
    def triangle(a,h):
        return (a*h)/2
print(areas.circle(3))
print(areas.rectangle(4,7))
print(areas.triangle(6,2))