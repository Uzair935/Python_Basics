"""def frequency_counter():
    text = "This is to only do a test for a test to this"
    text = text.lower()
    word_freq = {}
    words = text.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return(word_freq)

print(frequency_counter())"""


"""def combine_list():
    list1 = [0,1,2,3]
    list2 = ["Cocunut","Pineapple","Strawberry","Apple"]
    my_dict = dict(zip(list1,list2))

    return my_dict

print(combine_list())"""


def find_max():
    my_dictionary = {3:"Ali",1:"Umer",7:"Saad",2:"Fahad"}
    max_value = max(my_dictionary.keys())

    print("The maximum key value in the dictionary is: ",max_value)

find_max()