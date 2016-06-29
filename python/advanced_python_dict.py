import pandas as pd 
import numpy as np

# To load the CSV data into dataframe
df = pd.read_csv('faculty.csv')


formatted_name = df['name'].str.split().str[-1]
formatted_name.tolist() 

title_formatted = [x.strip().replace(' of Biostatistics', '').replace(' is Biostatistics', '') for x in df[' title']]
df['title_formatted']=title_formatted

df['surname']=formatted_name.tolist() 
df1=df[['surname',' degree', 'title_formatted', ' email']]

s=df1.values.tolist()
keys= df1['surname'].tolist()

# create a dictionary with empty list
faculty_dict = dict.fromkeys(keys, [])

###### PART III Q6: 
for k in faculty_dict.keys():
    for i in range(len(s)):
        if k == s[i][0]:
            faculty_dict[k] = faculty_dict[k] + [(s[i][1:])]

for k in faculty_dict.keys()[:3]:
    print k
    print faculty_dict[k]
    
    
##### PART III Q7: 
formatted_firstname = df['name'].str.split().str[0].tolist()

df['first name']=formatted_firstname 

keys= df['first name'].tolist()
df2=df[['first name','surname',' degree', 'title_formatted', ' email']]
s2=df2.values.tolist()


# create a dictionary with empty list
keys2= zip(df2['first name'].tolist(), df2['surname'].tolist())
professor_dict = dict.fromkeys(keys2, [])

for (i,j) in professor_dict.keys():
    for k in range(len(s2)):
        if i == s2[k][0] and j == s2[k][1]:
            professor_dict[(i,j)] = (s[k][1:])


for k in sorted(professor_dict.keys())[:3]:
    print k
    print professor_dict[k]
    

# PART III Q8: 

print sorted(professor_dict.keys(), key=lambda x:x[1])
    
    
    
