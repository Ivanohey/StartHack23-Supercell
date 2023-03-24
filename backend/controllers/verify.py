import random
from pymysql.err import IntegrityError
import json
from datetime import datetime
import pandas as pd
import csv

#Method to get the first row of the client list
def getRandomUser():
    file = pd.read_csv("./ressources/applicants.csv", nrows=1)
    subset = file.loc[0, ['account_id', 'session_count', 'risk', 'level']]
    #result = subset.to_json
    response = {'account_id': subset['account_id'], 
                'session_count': subset['session_count'], 
                'risk':subset['risk'],
                'level': subset['level']}
    result = str(response)
    return result

     
     
    