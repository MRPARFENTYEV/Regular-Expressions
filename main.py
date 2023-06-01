import re
import csv

list_of_words = []
formatted_num = []
empty_string = ""

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    for raw in csv.reader(f, delimiter=","):
        """empty_string+=" ".join(word for word in raw)
        pattern = '(\+?\d{1})[ ]?[(]?[-]?(\d{3})[-]?[)]?[ ]?(\d{3})[-]?(\d{2})[-]?(\d{2})[ ]?([(])?[д]?[о]?[б]?[.]?[ ]?([0-9]?[0-9]?[0-9]?[0-9]?)([)]?)'
        sub_num_11 = '+7(\2)\3-\4-\5'
        sub_num_15 = '+7(\2)\3-\4-\5 \7\8'
        print(empty_string)"""

        raw_1 = raw[0:3]
        raw_2 = raw[3:-1]

        phones = raw_2[-1]
        glued = ' '.join(raw_1[0:3]).rstrip()
        list_of_words.append(glued.split(' ') + raw_2)

pattern = re.compile(
    '(\+?\d{1})[ ]?[(]?[-]?(\d{3})[-]?[)]?[ ]?(\d{3})[-]?(\d{2})[-]?(\d{2})[ ]?([(]?)([д]?[о]?[б]?[.]?)[ ]?([0-9]?[0-9]?[0-9]?[0-9]?)([)])?')
sub_num_11 = r'+7(\2)\3-\4-\5'
sub_num_15 = r'+7(\2)\3-\4-\5 \7\8'

for index, person in enumerate(list_of_words[1:], start=1):
    if "доб." in person[-1]:
        # print(person[-1])
        res2 = re.sub(pattern, sub_num_15, person[-1])

        list_of_words[index][-1] = res2

    elif person[-1]:
        res1 = re.sub(pattern, sub_num_11, person[-1])
        list_of_words[index][-1] = res1

similar = []
for el in list_of_words[-2]:
    if el not in similar:
        similar.append(el)
for elem in list_of_words[-1]:
    if elem not in similar:
        similar.append(elem)

del list_of_words[-1]
del list_of_words[-1]
list_of_words.append(similar)

if __name__ == '__main__':
    with open("list_of_words.csv", "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list_of_words)
