# with open("weather_wl.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_wl.csv") as dataFile:
#     data = csv.reader(dataFile)
#     temperatures = []
#     for row in data:
#         #print(row) #this + 2 above lines make it more like a table
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))    
#     print(temperatures)

import pandas as pd
# print(pd.__version__)

# data = pd.read_csv("weather_wl.csv")
# # print(data)

# # dataDict = data.to_dict()
# # print(dataDict)

# # tempList = data["temp"].to_list()
# # print(len(tempList))

# # tempNum = [23, 27, 18, 3, 1, 28, 25]
# # avgTemp = sum(tempNum)/len(tempNum)
# # print(f"The average temperature over this week is {avgTemp} degrees.")

# # to get the mean of the column "temp"
# # print(data["temp"].mean())
# # #shorter way to do this!!

# # # to get the max value of the column "temp"
# # print(data["temp"].max())

# # #each column title is now an attribute of the database, so...
# # print(data.weather)
# # print(data.day)
# # print(data.temp)

# # print(data[data.day == "Monday"]) # take data from where it is Monday

# # print(data.idxmax["day"]) # nope!!
# # print(data[data.temp == data.temp.max()]) # you are looking at where temp is max, and pulling THAT out

# monday = data[data.day == "monday"] # pull out the data from the row for monday
# # print(monday.weather) #get ONLY the weather out of that monday data


# # data.temp == ((data.temp)*(9/5))+32
# # print(data[data.temp]) # no!!

# monTemp = monday.temp.iloc[0] # iloc retroeves first row since 0 is first index
# monTempF = monTemp * (9/5) + 32
# print(f"Monday's temperature was {monTempF} degrees F.")

# ### lesson example ###

# dataDict = {
#     "students": ["Mila", "Monkey", "Maia"],
#     "scores": [96, 95, 92]
# }

# ourData = pd.DataFrame(dataDict)
# print(ourData) # makes a little table!! no effort needed!!
# data.to_csv("trio_of_grades") #creates a .csv file within this CSVWithPandas folder!!

#------PRACTICE WITH SQUIRRELS------#

#------step 1: read the csv file
squirrelStats = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") # to read file
# print(squirrelStats["Primary Fur Color"]) # take data from the Primary Fur Color column
# make sure to write the correct file name!!! otherwise it won't look at the csv file lol

#------step 2: define a variable for the column you need to access within the data table
mainColor = squirrelStats["Primary Fur Color"]

#------step 3: make a dictionary with keys and values
# each option in the column you want is part of one group of values
# use value_counts(), which is a method (not attribute) applied to your defined variable, for the second group of values

squirrelDict = {
     "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    #  "Frequency": [(squirrelStats.counts["Gray"]), (squirrelStats.counts["Cinnamon"])] # nope :/
    "Frequency": [
            mainColor.value_counts().get("Gray", 0), # count number of grays
            mainColor.value_counts().get("Cinnamon", 0), # count number of cinnamons  
            mainColor.value_counts().get("Black", 0) # count number of blacks
    ]
 }

print(squirrelDict)

#------step 4: make a nice little table
# print the variable you define for the new DataFrame, NOT the dictionary parameter WITHIN the DataFrame
# then for csv conversion, use the name of this new variable to save your NEW dataframe table as csv
squirrelNums = pd.DataFrame(squirrelDict)
print(squirrelNums) 
squirrelNums.to_csv("squirrel_fur_colors")

#------PRACTICE WITH US STATES MAP------#

