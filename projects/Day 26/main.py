# import csv
#
# with open('file1.txt') as fp1:
#     f1 =[int(line[0]) for line in csv.reader(fp1)]
#     print(f1)
#
# with open('file2.txt') as fp2:
#     f2 =[int(line[0]) for line in csv.reader(fp2)]
#     print(f2)
#
# result = [val for val in f1 if val in f2 ]
# print(result)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = { word:len(word) for word in sentence.split() }
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# key: str
# val: int
# weather_f = {key: (val * 9 / 5) + 32 for key, val in weather_c.items()}
#
# print(weather_f)


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

# TODO 1. Create a dictionary in this format:
data = {
    val['letter'].lower(): val['code']
    for (index, val) in
    pandas.read_csv('nato_phonetic_alphabet.csv'
                    ).iterrows()
}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word: ').lower()
print([ data[letter] for letter in user_input])