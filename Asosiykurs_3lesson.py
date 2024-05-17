# part 1 finish
# def stutter(string):
#     join_word = string[:2] + "... " + string[:2] + "... "
#     join_word += string + "?"
#     return join_word
#
#
# print(stutter("incredible"))
# print(stutter("enthusiastic"))
# print(stutter("outstanding"))

# part 2 finish
# def relation_to_luke(name):
#     relations = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother in law",
#         "R2D2": "droid"
#     }
#
#     if name in relations:
#         return f"Luke I am your {relations[name]}"
#     return "Unknown relation to Luke."
#
# print(relation_to_luke("Darth Vader"))
# print(relation_to_luke("Leia"))
# print(relation_to_luke("Han"))

# part 3 finish
# def mood_today(today):
#     mood = input("mood: ")
#     if mood == "":
#         print("Today i'm feeling neutral")
#     else:
#         print(f"Today i'm feeling {mood}!")
# print(mood_today("happy"))
# print(mood_today("sad"))
# print(mood_today(""))

# part 4 finish
# def count_vowels(word):
#     m = "aeiou"
#     count = 0
#     for s in word:
#         if s in m:
#             count += 1
#     return count
#
# print(count_vowels("Celebration"))
# print(count_vowels("Palm"))
# print(count_vowels("Prediction"))


# text = "pYtHon"# --> tekis qilibchiqaradi
#
# # convert all characters to lowercase
# lowercased_string = text.casefold()
#
# print(lowercased_string)
#
# # Output: python
#
# sentence = "Python is awesome"
#
# # returns the centered padded string of length 24
# new_string = sentence.center(24, '*')
#
# print(new_string)
#
# # Output: ***Python is awesome****

# title = 'Python Programming'
#
# # change encoding to utf-8
# print(title.encode())
#
# # Output: b'Python Programming'

# message = 'Python is '
#
# # check if the message ends with fun
# print(message.endswith('fun'))
#
# # Output: True

# part 5
# def correct_sign(num):
#     for x in num:
#         if len(x) < 11:
#             return True
#         else:
#             return False
#
# print(correct_sign("3 < 7 < 11"))
# print(correct_sign("13 > 44 > 33 > 1"))
# print(correct_sign("1 < 2 < 6 < 9 > 3"))

# part 6 finish
# def replace_vowels(sent, sent1):
#     m = "aeiou"
#     for letter in sent:
#         if letter in m:
#             sent = sent.replace(letter, sent1)
#     return sent
#
# print(replace_vowels("the aardvark", "#"))  # Natijada: "th# ##rdv#rk"
# print(replace_vowels("minnie mouse", "?"))
# print(replace_vowels("shakespeare", "*"))

# part 7 finish
# input1 = input("write: ")
# def counterpartcharcode(input1):
#     upper = 65
#     lower = 97
#     if input1.isupper():
#         return lower
#     elif input1.islower():
#         return upper
# print(counterpartcharcode(input1))

# part 8
# def card_hide(num):
#     num2 = " "
#     i = 0
#     if len(num) == 16:
#         belgi = "*"
#         n = num[:-4]
#         return num.replace(n,belgi)
#
# print(card_hide("1234123456785678")) # out put ************5678

# part 9
# def XO(string):
#     m = "ooxx"
#     for x in string:
#         if x in m:
#             return True
#
# print(XO("ooxx"))
# print(XO("xooxx"))
# print(XO("ooxXm"))

# part 10 finish
# def reverce(gaps):
#     lst = []
#     lst.extend(gaps)
#     lst.reverse()
#     gops = str(lst)
#     if gops in gops.upper():
#         return gops.lower()
#     elif gops in gops.lower():
#         return gops.upper()
#
# print(reverce("Hello world"))
# print(reverce("reverse"))
# print(reverce("radar"))

# part 11 finish
# def index_of_caps(string):
#     lst = []
#     for x in string:
#         if x.isupper():
#             lst.append(string.index(x))
#     return lst
# print(index_of_caps("eDaBiT"))
# print(index_of_caps("eQuINoX"))
# print(index_of_caps("determine"))
# print(index_of_caps("STRIKE")) # --> [1,2,3,4,5,6]
# print(index_of_caps("sUn")) # --> [1]

# part 12 finish
# def double_char(soz):
#     soz1 = ""
#     for x in soz:
#         soz1 += 2*x
#     return soz1
# print(double_char("String"))
# print(double_char("Hello world"))
# print(double_char("1234!_"))

# part 13 finish
# def count_characters(lst):
#     result = 0
#     for x in lst:
#         for i in x:
#             result += 1
#     return result
# print(count_characters(["###","###","###"]))
# print(count_characters(["22222222","22222222"]))
# print(count_characters(["------------------"]))
# print(count_characters([]))
# print(count_characters(["",""]))

# part 14
# def hamming_distance(str1,str2):
#     lst = []
#     for x in str1:
#         if len(str1) == len(str2):
#             if x in str2:
#                 lst.append(str1.count(x))
#     return len(str1) - sum(lst)
#
# print(hamming_distance('abcde','bcdef'))
# print(hamming_distance('strong','strung'))
# print(hamming_distance('cut','cut'))


# def name_shuffle(name):
#     lst = []
#     for x in name:
#         lst.append(x)
#         n = lst.reverse()
#         print(lst)
# name_shuffle("Donalt Trump")