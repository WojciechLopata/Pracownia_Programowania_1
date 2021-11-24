import json
film={
    "autor":"1",
    "wydawca":2.0,
    "wydanie":"lol",
    "nudne":True,
    "kto_pytal":None,
    }
file=open("Favorite.json","w")
json.dump(film,file,indent=4)

file.close()
    
    

    
    