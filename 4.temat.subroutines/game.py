import mymath

player_guess=mymath.read_number()
rand_numb=mymath.generate_number()
if(player_guess==rand_numb): print("YOU WON")
else: print ("YOU LOST")