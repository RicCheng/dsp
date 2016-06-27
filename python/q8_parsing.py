# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
file = open('football.csv', 'r')
reader = csv.reader(file)
data = list(reader)

team_count = len(data)-1
team_data = [data[i+1][0] for i in range(team_count)]
diff = [abs(int(data[i+1][5])-int(data[i+1][6])) for i in range(team_count)]

index = diff.index(min(diff))
print team_data[index]