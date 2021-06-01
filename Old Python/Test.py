import urllib.request 
datas = urllib.request.urlopen("https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt")
data_list = []
data_dict = {}
special_character = '''~`!@#$%^&*()_=+,.?/:;'[]1234567890"'''
for data in datas:
    word = data.decode("utf-8")
    word_list = word.split()
    data_list.append(word_list)

for line in data_list:
    for item in line:
        item = item.lower()
        for char in item:
            if char in special_character:
                item = item.replace(char,'')
        items = item.split("--")
        for item in items:
            if item == '':
                continue
            if data_dict.get(item) == None:
                data_dict.update({item:1})
            else:
                value = data_dict.get(item)
                value += 1
                data_dict.update({item:value})

sort_data_list = sorted(data_dict.items())
outfile = open("alice_words.txt","w")
outfile.write("__________________________\n")
writing = "| Word           |Count    \n"
outfile.write(writing)
index = writing.index("Count")
for k,v in sort_data_list:
    outfile.write("| " + str(k) + (" " * (index-len(k)-3)) + "|" + str(v) + "\n")
outfile.close()
sort_data_dict = dict(sort_data_list)
print("{} occurs {} times in the book".format('Alice',sort_data_dict.get('alice')))
max_length = 0
key = ""
for k,v in sort_data_list:
    if len(k) > max_length:
        max_length = len(k)
        key = k
    else:
        max_length = max_length
        key = key 
print("Key " + str(key) + " has max length with " + str(max_length) + " characters")