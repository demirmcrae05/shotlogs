#Importing the CSV in as a DataFrame
import pandas as pd
import numpy as np

shotLogs = pd.read_csv('shot_logs.csv', low_memory=False)#reads the csv with all the shot log data

#dropping columns I don't need
shotLogsClean= shotLogs.drop(['LOCATION','W','FINAL_MARGIN','PERIOD','GAME_CLOCK','SHOT_CLOCK',
                        'DRIBBLES','TOUCH_TIME','CLOSEST_DEFENDER','CLOSEST_DEFENDER_PLAYER_ID',
                         'CLOSE_DEF_DIST'], axis = 1)
                         
#function finding the percentages needed
def streak(player: str):
    playerShots = shotLogsClean[shotLogsClean.player_name==player]
    shots = list(playerShots.SHOT_RESULT)
    place = 1
    counter = 0
    makeMake = 0
    switch = 0
    missMiss = 0
    while place < len(shots):
        if shots[place-1] == "made" and shots[place] == "made":
            makeMake+=1
            counter+=1
        elif shots[place-1] == "made" and shots[place] == "missed" or shots[place-1] == "missed" and shots[place] == "made":
            switch+=1
            counter+=1
        else:
            missMiss+=1
            counter+=1
        place+=1
    #print(player)
    #print("Amount of makes after a made shot:" , makeMake)
    #print("Amount of switched results:" ,switch)
    #print("Amount of misses after a missed shot:" ,missMiss)
    #print("Out of:",counter)
    #print("% of make after a make =", makeMake/counter)
    #print("% of switched results =", switch/counter)
    #print("% of miss after a miss =", missMiss/counter)
    #print("----------------------")
    #print()
    
    return makeMake/counter, switch/counter, missMiss/counter
#returns a tuple

#streakDict = {}
#print(byPlayer.keys())
#creating two lists in order to put them into a dataframe
streakList = []
inner = []
for key in byPlayer.keys():
    #print(key)
    #print(byPlayer[key][0])
    inner.append(byPlayer[key][0])
    inner.append(byPlayer[key][2])
    streakList.append(inner)
    inner=[]
    
    
  #print(streakList)
df2 = pd.DataFrame(streakList)
df2.columns = ['Make | Make','Miss | Miss']
df2.index = byPlayer.keys()
df2.head()
df2.sort_values(by = "Make | Make", ascending = False)


names = []
for name in byPlayer.keys():
    correcter = list(name)
    #print(correcter)
    corrected = ''
    correcter[0]=correcter[0].upper()
    corrected = corrected + correcter[0]
    #print(correcter)
    ind = 1
    for i in range(ind, len(correcter)):
        if correcter[i-1] == ' ':
            correcter[i] = correcter[i].upper()
            corrected = corrected + correcter[i]
            #print(corrected)
        else:
            corrected+=correcter[i]
            ind+=1
    names.append(corrected)
    
#print(names)
df2.index = names
df2.head()
df2.sort_values(by = "Make | Make", ascending = False)
