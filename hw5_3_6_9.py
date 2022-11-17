from functools import reduce
# 3)
# Imagine you have a dictionary with the attributes of a person
dict1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
dict2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl


def retrieve_age_eafp(person):
    try:
        return 2022 - person["birth"]
    except Exception as e:
        print(str(type(e).__name__), str(e))


def retrieve_age_lbyl(person):
    if "birth" in person.keys():
        return 2022 - person["birth"]
    else:
        print("some keys are missing")


print(retrieve_age_eafp(dict1))
retrieve_age_eafp(dict2)
print(retrieve_age_lbyl(dict1))
retrieve_age_lbyl(dict2)

################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
list_of_strings = ["Simba and Nala are lions.",
                   "I laugh in the face of danger.",
                   "Hakuna matata",
                   "Timon, Pumba and Simba are friends, \
                    but Simba could eat the other two."]


"""def count_words(word):

    def currying_function(string):
        return string.lower().count(word.lower())

    return currying_function"""


def count_simba(list_of_strings, word):

    #word_in_string = list(map(count_words(word), list_of_strings))
    word_in_string = list(
                        map(lambda string: string.lower().count(word.lower()),
                            list_of_strings)
                            )
    total_count = reduce(lambda x, y: x + y, word_in_string)

    return total_count


word = "Simba"
total_times_in_strings = count_simba(list_of_strings, word)
print("Total times \"{}\" is in list of \
strings: {}".format(word, total_times_in_strings))




#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

list_ex_9 = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]


def sum_general_int_list(list_numbers, total):

    for position in list_numbers:
        if type(position).__name__ == "list":
            total = sum_general_int_list(position, total)
        else:
            total += position
    return total


total = 0
total_sum = sum_general_int_list(list_ex_9, total)
print("total value: {}".format(total_sum))
