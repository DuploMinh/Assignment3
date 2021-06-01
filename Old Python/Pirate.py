#1
def keys():
    infile = open("eng2pirate.txt","r")
    keys = []
    for line in infile:
        words = line.split()
        keys.append(words[0])
    infile.close()
    return keys
def values():
    infile = open("eng2pirate.txt","r")
    values = []
    for line in infile:
        value = ""
        words = line.split()
        for word in words:
            if word == words[0]:
                continue
            value += word + " "
        values.append(value)
    infile.close()
    return values 
def dictionary(key, value):
    i = 0
    pirate_dict = {} 
    while i != len(key):
        pirate_dict.update({key[i]:value[i]})
        i += 1
    return pirate_dict
def mess_translate(dict):
    mess = input("Please enter your message in English: ")
    mess_list = mess.split()
    i = 0 
    new_mess = ""
    flag = False
    while i != len(mess_list):
        for item in mess_list:
            for key in pirate_dict.keys():
                if item == key:
                    new_mess += pirate_dict.get(key) + ""
                    flag = True
                    break
            if flag == False:
                new_mess += item
                i += 1
            else: 
                flag = False 
                i += 1
    print(new_mess)
pirate_dict = dictionary(keys(),values())
mess_translate(pirate_dict)