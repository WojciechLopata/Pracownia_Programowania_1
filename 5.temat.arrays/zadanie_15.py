colors=["red","blue","yellow"]
f = open("Colors_1.txt", "w")
for color in colors:
    f.write(color)
    f.write("\n")
#f.writelines(colors)
f.close()
