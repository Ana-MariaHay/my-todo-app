def get_nr_items(items_str):
    items_list = items_str.split(",")

    len_items_list = len(items_list)
    print(items_list)

    return len_items_list


this_str = "john, lisa, teresa"
ans = get_nr_items(this_str)
print(ans)
