#Import modules
import random
#Problem 1
def est_grade(grade):
    #Intialize variables
    problem_score = [10,15,20,20]
    comment_score = 0
    total_score = 0
    grade_received = 0
    #Finding the total marks given, to calculate the mark for code design and comment
    for mark in problem_score:
        total_score += mark
    comment_score = 100 - total_score
    problem_score.append(comment_score)
    #Calculate actual total point students did
    index = 0
    for point in problem_score:
        #If reached the end of the list, exit the for loop
        if index == (len(grade)):
            break
        point = point * grade[index]
        grade_received += point
        index += 1
    #Round the mark so students can have HD with 79.5
    grade_received = round(grade_received)
    #Test cases
    grade_level = ""
    if 80 <= grade_received <= 100:
        grade_level = "HD"
    if 70 <= grade_received < 80:
        grade_level = "DI"
    if 60 <= grade_received < 70:
        grade_level = "CR"
    if 50 <= grade_received < 60:
        grade_level = "PA"
    if grade_received < 50:
        grade_level = "NN"
    #Return student grade
    return grade_level
#Problem 2
def midway_reverse(string):
    #Check if the string length is even
    if len(string) % 2 == 0:
        #Calculate the index of the middle point
        middle_point = int(len(string)/2)
        #Divide the string into 2 sub-strings, separated in the middle point
        string_1 = string[:middle_point]
        string_2 = string[middle_point:]
        #Reversed the two sub strings
        string_1 = string_1[::-1]
        string_2 = string_2[::-1]
        #Concatenate two sub-strings
        new_s = string_1 + string_2
    #String length is odd
    else:
        #Calculate the index of the middle point
        middle_point = int(len(string)/2)
        #Divide the string into 2 sub-strings, separated in the middle point
        #Holder is used to hold the data of the mid-point
        holder = string[middle_point]
        string_1 = string[:middle_point]
        string_2 = string[middle_point+1:]
        #Concate reversed sub-strings
        new_s = string_1[::-1] + str(holder) + string_2[::-1]
    return new_s
#Problem 3
def shopping_cal(lst,dct):
    #Calculate the quantity of each purchased items and store in a new dictionary
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    #Calculate the price of each items after sale off applies and store in a new dictionary
    actual_price_dict = {}
    for key in dct:
        price_list = dct[key]
        price = price_list[0] * (1-price_list[1])
        actual_price_dict.update({key:price})
    #Calculate the price spent on each items based on sale off price and quantity purchased
    total_spent = 0
    price_spent_on_single_item = {}
    for key in count_dict:
        if key in actual_price_dict:
            price = count_dict[key] * actual_price_dict[key]
            total_spent += price
            price_spent_on_single_item.update({key:price})
    #Find max spent items, its key_id and store in a list
    max_spent = 0
    spent_most_on_item_id = []
    key_name = ""
    for key in price_spent_on_single_item:
        if price_spent_on_single_item[key] > max_spent:
            max_spent = price_spent_on_single_item[key]
            key_name = key
    spent_most_on_item_id.append((key_name,max_spent))
    return total_spent,spent_most_on_item_id
#Problem 4
def encrypt(s):
    #Initiate a list to store broken string to add special characters inside
    list_s = []
    #Special character list
    list_special = [',','.','/']
    for word in s:
        list_s.append(word)
    list_s_encrypted = []
    #Break the string down and add new characters
    for word in list_s:
        word = word + random.choice(list_special)
        list_s_encrypted.append(word)
    #Encrypt the string further with non-senses
    encrypted_s = ",,,Q/#WE$R,,,M@N,," + s + ",23,KJ$L,"
    return encrypted_s
def decrypt(encrypted_s):
    #Initiate DNA Bases
    DNA = "ATUGC"
    #Complementary bases
    Complementary = "TAACG"
    #Origianl DNA string initiated
    ori_DNA = ""
    complementary_s = ""
    encrypted_s = encrypted_s.upper()
    #Select only A,T,U,G,C characters from the encrypted string from left to right
    for char in encrypted_s:
        if char in DNA:
            ori_DNA += char
    #Complementary the DNA Bases
    for char in ori_DNA:
        if char == 'A':
            complementary_s += "T"
        if char == 'T' or char == 'U':
            complementary_s += "A"
        if char == 'C':
            complementary_s += "G"
        if char == 'G':
            complementary_s += "C"
    #Return
    return ori_DNA, complementary_s

print(midway_reverse("4321765"))