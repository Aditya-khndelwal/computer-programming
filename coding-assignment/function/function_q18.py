#Q18 = Create a function flatten_list that takes a nested list and returns a flat list.

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
result = flatten_list([[1,2,3],2,4,[4,5,6]])
print(result)
