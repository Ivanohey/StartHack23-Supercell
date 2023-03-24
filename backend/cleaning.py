#This is the backend server that will serve the ML model
import pandas as pd
import numpy as np

def dataCleaning():

    print("Loading datasets")
    message1 = pd.read_csv('ressources/chat_messages_1.csv', low_memory= False)
    message2 = pd.read_csv('ressources/chat_messages_2.csv', low_memory= False)
    accounts = pd.read_csv('ressources/accounts.csv', low_memory= False)

    messages = pd.concat([message1, message2])
    messages.head()
    messages = messages[["account_id", "timestamp", "risk", "is_family_friendly"]]

    friends = messages[["account_id", "timestamp","is_family_friendly"]]
    friends = friends[friends["is_family_friendly"].str.contains("looking over at Russetstrike") == False]
    friends = friends[friends["is_family_friendly"].str.contains("smell my pits") == False]
    friends = friends[friends["is_family_friendly"].str.contains("south park") == False]
    friends["is_family_friendly"] = pd.to_numeric(friends["is_family_friendly"], downcast="float")

    #friends = friends[friends["is_family_friendly"].str.contains("smell my pits") == False]

    messages_fin = messages

    messages_fin = messages_fin[messages_fin["risk"].str.contains(' I have no life outside of picking on people beneath me"""') == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains("we as gay people") == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains("yes") == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains("no") == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains("get ready for this") == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains("get 15 every time in tourney") == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains('"""Hi') == False]
    messages_fin = messages_fin[messages_fin["risk"].str.contains('"search ""watchseries"" to watch any movie or show you want') == False]
    messages_fin['response'] = messages_fin['risk'].astype(float).apply(lambda x: 1 if x>=5 else 0)
    response = messages_fin[["account_id", "response"]]

    inspect = messages_fin.risk.unique()
    inspect2 = messages_fin['risk'].dtype
    messages_fin["risk"] = pd.to_numeric(messages_fin["risk"], downcast="float")

    #final data set
    print("Generating applicants data set")
    messages_fin = messages_fin.groupby('account_id')['risk'].mean()
    messages_fin = messages_fin.to_frame()

    applicants = pd.merge(accounts, messages_fin, how="left", on=["account_id"])
    applicants = pd.merge(applicants, friends, how="right", on=["account_id"])
    applicants = pd.merge(applicants, response, how="left", on=["account_id"])

    applicants = applicants[["account_id", "timestamp", "is_family_friendly", "session_count", "level", "risk", "response"]]
    applicants = applicants.drop_duplicates()
    applicants = applicants.dropna()
    applicants = applicants.reset_index()

    applicants.to_csv('ressources/applicants.csv', encoding='utf-8')
