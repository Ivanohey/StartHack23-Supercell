import pandas as pd
import numpy as np

message1 = pd.read_csv('data_sets/chat_messages_1.csv', low_memory= False)
message2 = pd.read_csv('data_sets/chat_messages_2.csv', low_memory= False)

messages = pd.merge(message1, message2, on='account_id')
messages = messages.groupby('account_id')[''].mean()