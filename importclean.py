import pandas as pd

data = pd.read_csv('shot_logs.csv', low_memory=False)#reads the csv with all the usg rate data
type(data)
data

#getting column names
print(data.columns)

#dropping columns I don't need
dataCleanse = data.drop(['LOCATION','W','FINAL_MARGIN','PERIOD','GAME_CLOCK','SHOT_CLOCK',
                        'DRIBBLES','TOUCH_TIME','CLOSEST_DEFENDER','CLOSEST_DEFENDER_PLAYER_ID',
                         'CLOSE_DEF_DIST'], axis = 1)
dataCleanse

#sort by player names 
dataCleanse.sort_values(by=['player_name'])
