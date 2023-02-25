student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

user = input("Input a word: ")
phonetic = [nato_dict[letter.upper()] for letter in user]
print(phonetic)