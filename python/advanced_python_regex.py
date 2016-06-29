import pandas as pd 
import numpy as np

# To load the CSV data into dataframe
df = pd.read_csv('faculty.csv')

# PART 1 Q1:
degree_formatted = [x.strip().replace('.', '').split() for x in df[' degree']]
set(reduce(lambda x,y: x+y,degree_formatted))

# PART 1 Q2: 
title_formatted = [x.strip().replace(' of Biostatistics', '') for x in df[' title']]
set(title_formatted)

# PART 1 Q3: 
email = df[' email']
print list(email)

# PART 1 Q4: 
email_domain = [x[x.find('@'):] for x in df[' email']]
set(email_domain)
