import pandas as pd 
import numpy as np

# To load the CSV data into dataframe
df = pd.read_csv('faculty.csv')

email =  df[' email']
email.to_csv('emails.csv', index = False)