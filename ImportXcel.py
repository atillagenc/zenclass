# Import pandas
import pandas as pd
import json

class Correspondence:
    def __init__(self, datetime, line):
        self.user = 1
        self.date = datetime
        self.utterance = line


class Conversation:

    def __init__(self, identifier):
        self.id = identifier
        self.correspondence = []

    def add_correspondence(self, datetime, line):
        self.correspondence.append(Correspondence(datetime, line))





# Assign spreadsheet filename to `file`
file = '/Users/agenc/Downloads/Whole conversations.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse(xl.sheet_names[0])

conversations = []
conversation = Conversation(None)
conversations.append(conversation)

for r in range(3):
    #line = ""
    #for c in range(df1.shape[1]):
    #    line += str(df1.iloc[r][c]) + "\t"
    #print(line)
    if not conversation.id:
        conversation.id = df1.iloc[r][1]
    if conversation.id != df1.iloc[r][1]:
        conversation = Conversation(df1.iloc[r][1])
        conversations.append(conversation)
    conversation.add_correspondence(df1.iloc[r][3], df1.iloc[r][5])

with open("data_file.json", "w") as write_file:
    json.dump(conversations, write_file)



