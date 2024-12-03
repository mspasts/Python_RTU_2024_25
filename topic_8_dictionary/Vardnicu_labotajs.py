def replace_dict_value(d, bad_val, good_val):
    """    
    Replaces all instances of bad_val in dictionary d with good_val.
    IN PLACE
    """
    for key in d:
        if d[key] == bad_val:
            d[key] = good_val
    return d # technically this is not needed since original dictionary is changed
print(replace_dict_value({'a': 5, 'b': 6, 'c': 5}, 5, 10))

# is this IN PLACE or OUT OF PLACE? IN PLACE

# so how could we make this OUT OF PLACE?
# one simple modification would be to create a new dictionary and copy all the key-value pairs from the original dictionary to the new one

def replace_dict_value_out_of_place(d, bad_val, good_val):
    """    
    Replaces all instances of bad_val in dictionary d with good_val.
    OUT OF PLACE
    """
    # in this version we BUILT UP a new dictionary
    new_d = {}
    # so we go through original dictionary
    # and copy all key-value pairs to the new dictionary unless the value is bad_val
    for key in d:
        if d[key] == bad_val:
            new_d[key] = good_val # add new entry with good_val
        else:
            new_d[key] = d[key] # otherwise add new entry with the original value
    return new_d

some_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 5, 'e': 6}
new_dict = replace_dict_value_out_of_place(some_dict, 5, 10)
print("ORIGINAL:", some_dict)
print("NEW:", new_dict)
# so the original dictionary is unchanged
# if I used the original function the original dictionary would have been changed
some_dict_alias = replace_dict_value(some_dict, 5, 18)

print("ORIGINAL:", some_dict)
print("ALIAS:", some_dict_alias)
# so the original dictionary is changed
# let's print the new dictionary from the OUT OF PLACE function
print("NEW:", new_dict)

# we could create a dual use function with in_place flag

def replace_dict_value(d, bad_val, good_val, in_place=True):
    """    
    Replaces all instances of bad_val in dictionary d with good_val.
    IN PLACE or OUT OF PLACE depending on in_place flag
    """
    # if not in place we create a copy of the dictionary
    # that means we will not change the original dictionary
    # this is OUT OF PLACE
    if not in_place:
        d = d.copy() # so inside now d is a copy of the original dictionary original dictionary is unchanged

    for key in d:
        if d[key] == bad_val:
            d[key] = good_val

    return d # so now either original or a copy is returned