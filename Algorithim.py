def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return target_value
    raise ValueError("{0} not in list".format(target_value))