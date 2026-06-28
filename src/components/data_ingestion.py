#for reading the data 
'''
1. components Folder
Purpose

This folder contains the core ML building blocks. Each file performs one major task in the ML lifecycle.

Think of it as:

"How is the model built?"'''



'''b) data_ingestion.py
Purpose

Responsible for collecting and loading data.

Typical tasks:

Read CSV
Read Excel
Read Database
Split train and test data
Save processed datasets

Example:

df = pd.read_csv("data.csv")

train_set, test_set = train_test_split(df)

In simple words:

Gets the data into your project.'''

