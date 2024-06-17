# Flatten a nested dictionary into a single dictionary.
def flattening(var):
    flatten_dictionary = {}
    for item in var:
        if isinstance(var[item],dict):
            for key, value in flattening(var[item]).items():
                flatten_dictionary[str(item) + "." + str(key)] = value
        else:
            flatten_dictionary[item] = var[item]
    return flatten_dictionary


dictionary = {
    "numbers": {1: "one", 2: "two", 8: {"v": 6}, "float_num": {3: 3.0, 4: 4.0}},
    "alphabets": {"a": "A", "b": "B"},
}
print(flattening(dictionary))
