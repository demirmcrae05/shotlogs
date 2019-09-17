#get the shots for one player
aaronBrooks = dataCleanse[dataCleanse.player_name=='aaron brooks']

aaronBrooks

#Sort by shot value to separate shooing
aaronBrooks.sort_values(by = ['GAME_ID','PTS_TYPE','SHOT_DIST'])

#go through and find all the makes and misses
makes = 0
misses = 0
for shot in aaronBrooks.SHOT_RESULT:
    #print(shot)
    if shot == "made":
        makes+=1
    else:
        misses+=1

print(makes)
print(misses)

#trying to see how many 2 shot combos we can get
#(make,make) (make,miss), (miss,make), (miss,miss)

#make,make
abShots = list(aaronBrooks.SHOT_RESULT)
#print(abShots)
place = 1
counter = 0
makeMake = 0
makeMiss = 0
missMake = 0
missMiss = 0
while place < len(abShots):
    if abShots[place-1] == "made" and abShots[place] == "made":
        makeMake+=1
        counter+=1
    elif abShots[place-1] == "made" and abShots[place] == "missed":
        makeMiss+=1
        counter+=1
    elif abShots[place-1] == "missed" and abShots[place] == "made":
        missMake+=1
        counter+=1
    else:
        missMiss+=1
        counter+=1
    place+=1

print(makeMake)
print(makeMiss)
print(missMake)
print(missMiss)
print(counter)
print("% of make after a make =", makeMake/counter)
print("% of miss after a make =", makeMiss/counter)
print("% of make after a miss =", missMake/counter)
print("% of miss after a miss =", missMiss/counter)
        
    



