film_titles=["Matrix","dune","James bond","toy story","Forrest gump"]
file=open("Films.txt","w")
for title in film_titles:
    file.write(title)
    file.write("\n")
file.close()