from hash_table import HashTable
import pandas as pd
import string
from math import sin
import numpy as np
#
#
# # df = pd.read_csv("files/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv")
# #
# #
# # nyc_weather = HashTable()
# # nyc_weather_list = []
# # for date, temp in zip(df['date'], df['temperature(F)']):
# #     nyc_weather[date] = temp
# #     nyc_weather_list.append(temp)
# #
# #
# # print("Average Temp:", sum(nyc_weather_list)/len(nyc_weather_list))
# # print("Max Temp:", max(nyc_weather_list))
# # print("Temp on Jan 9:", nyc_weather["Jan 9"][1])
# # print("Temp on Jan 4:", nyc_weather["Jan 4"][1])
#
# with open("files/data_structures/4_HashTable_2_Collisions/Solution/poem.txt", mode="r") as file:
#     text = file.read()
#     poem = ""
#     for letter in text:
#         poem += letter
#
# poem = poem.translate(str.maketrans('','',string.punctuation))
# poem = poem.replace("\n", ' ').split(" ")
# poem_words = {}
# for word in poem:
#     poem_words[word.lower()] = 0
#
# for word in poem:
#     new_word = word.lower()
#     if new_word in poem_words.keys():
#         poem_words[new_word] += 1
#
# print(poem_words)
#
