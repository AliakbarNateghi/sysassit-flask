def compare_json(json1, json2):
    differing_keys = []

    dict1 = json1
    dict2 = json2

    all_keys = set(dict1.keys())

    all_keys = list(all_keys)
    
    for key in dict1.keys():
        if key in dict2.keys():
            # Compare the values of the common keys
            if dict1[key] != dict2[key]:
                differing_keys.append(key)
        else:
            differing_keys.append(key)

    # Remove the common elements with equal values
    for key in [key for key in all_keys if key not in differing_keys]:
        if dict1[key] == dict2[key]:
            del dict1[key]
            del dict2[key]

    return dict1, dict2
