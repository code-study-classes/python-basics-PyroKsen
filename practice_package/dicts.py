def count_char_occurrences(text):
    occurrences = {}
    for char in text:
        if char.isalpha():  
            char_lower = char.lower()
            if char_lower in occurrences:
                occurrences[char_lower] += 1
            else:
                occurrences[char_lower] = 1
    
    return occurrences


def merge_dicts(dict1, dict2, conflict_resolver):
    pass


def invert_dictionary(original_dict):
    pass


def dict_to_table(data_dict, columns):
    pass
    


def deep_update(base_dict, update_dict):
    pass