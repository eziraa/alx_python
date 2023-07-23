def update_dictionary(a_dictionary, key, value):
    is_updated = False
    for key1, value in a_dictionary:
        if (key == key1):
            dict(a_dictionary).update(key, value)
            is_updated = True
    if (not is_updated):
        dict(a_dictionary(key, value))
