# 3.a
 
def clean_dict_value(d, bad_val):
    """
    Removes all key-value pairs from a dictionary where the value is equal to bad_val.
    OUT OF PLACE - creates a new dictionary.
    :param d: dictionary to clean
    :param bad_val: value to remove
    :return: new dictionary without key-value pairs where value is equal to bad_val
    """
    # using dictionary comprehension
    # return {key: vertiba for key, vertiba in d.items() if vertiba != bad_val}
    # let's do this without dictionary comprehension
    # so again BOTH are correct solutions
    new_dict = {}
    for key, value in d.items():
        if value != bad_val:
            new_dict[key] = value
    return new_dict


# testing 
print(clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5))
og_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 5, 'e': 6}

clean_dict = clean_dict_value(og_dict, 5)
print("Original dictionary:", og_dict)
print("Cleaned dictionary:", clean_dict)

# let's see inplace approach
def clean_dict_value_in_place(d, bad_val):
    # we use list comprehension to get all keys that have bad_val as value
    # keys_to_remove = [key for key, value in d.items() if value == bad_val]
    # same as above but without list comprehension
    keys_to_remove = []
    for key, value in d.items():
        if value == bad_val:
            keys_to_remove.append(key)
    # now we know all keys that have bad values        
    for key in keys_to_remove:
        del d[key] # no chance of error since we know that the key exists
    # we could return d but it is not necessary as we are changing the original dictionary
    return d # we have no obligation to use the return value

# testing
print("Original dictionary:", og_dict)
clean_dict_value_in_place(og_dict, 6)
print("Cleaned dictionary in place:", og_dict) # we can see that the original dictionary is changed

# 3.b
 
def clean_dict_values(d: dict[any, any], bad_val_list: list[any]) -> dict[any, any]:
    """
    Removes all key-value pairs from a dictionary where the value is equal to any of the values in bad_val_list.
    OUT OF PLACE - creates a new dictionary.
    :param d: dictionary to clean
    :param bad_val_list: list of values to remove
    :return: new dictionary without key-value pairs where value is equal to any of the values in bad_val_list
    """
    # we could check first if d is a dictionary and bad_val_list is a list
    # if we do not get the right types we simply return an empty dictionary and print an error message
    # in real life we might want to raise an exception or log to a file - later on files
    if not isinstance(d, dict):
        print("Error: d is not a dictionary") # better would be to log this to a file
        return {} # we could return None but {} is less likely to break the code
    
    if not isinstance(bad_val_list, list):
        print("Error: bad_val_list is not a list")
        return {}

    # list comprehension solution
    # return {key: vertiba for key, vertiba in d.items() if vertiba not in bad_val_list}
    # again we can do the same thing without list comprehension
    new_dict = {}
    for key, value in d.items():
        if value not in bad_val_list:
            new_dict[key] = value
    return new_dict


# testing
og_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 5, 'e': 6, 'f': 7}
print("Original dictionary:", og_dict)
clean_dict = clean_dict_values(og_dict, [5, 6]) 
print("Original dictionary:", og_dict)
print("Cleaned dictionary:", clean_dict)

# let's see inplace approach
def clean_dict_values_in_place(d: dict[any, any], bad_val_list: list[any]) -> dict[any, any]:
    """
    Removes all key-value pairs from a dictionary where the value is equal to any of the values in bad_val_list.
    IN PLACE - modifies the original dictionary.
    :param d: dictionary to clean
    :param bad_val_list: list of values to remove
    :return: modified dictionary without key-value pairs where value is equal to any of the values in bad_val_list
    """
    # we could check first if d is a dictionary and bad_val_list is a list
    # if we do not get the right types we simply return an empty dictionary and print an error message
    # in real life we might want to raise an exception or log to a file - later on files
    if not isinstance(d, dict):
        print("Error: d is not a dictionary") # better would be to log this to a file
        return {} # we could return None but {} is less likely to break the code
    
    if not isinstance(bad_val_list, list):
        print("Error: bad_val_list is not a list")
        return {}

    # we use list comprehension to get all keys that have bad values
    # keys_to_remove = [key for key, value in d.items() if value in bad_val_list]
    # same as above but without list comprehension
    keys_to_remove = []
    for key, value in d.items():
        if value in bad_val_list:
            keys_to_remove.append(key)
    # now we know all keys that have bad values        
    for key in keys_to_remove:
        del d[key] # no chance of error since we know that the key exists
    # we could return d but it is not necessary as we are changing the original dictionary
    return d # we have no obligation to use the return value