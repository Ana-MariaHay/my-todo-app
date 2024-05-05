def avg(item_list):
    avg = sum(item_list) / len(item_list)
    return avg


items = input("Items to average separated by ,: ")
items = items.split(",")
items_l = [float(i) for i in items]

print(avg(items_l))