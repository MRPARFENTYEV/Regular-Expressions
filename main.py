import re
import pandas
from pprint import pprint
import csv

no_changes = []
list_of_words = []
with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    for raw in csv.reader(f, delimiter=","):
        raw_1 = raw[0:3]
        raw_2 = raw[3:-1]
        glued = ' '.join(raw_1[0:3]).rstrip()
        list_of_words.append(glued.split(' ') + raw_2)

print(list_of_words)
with open("phonebook.csv", "w",encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_of_words)

'''Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.'''
'''Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.'''
'''Объединить все дублирующиеся записи о человеке в одну.'''
