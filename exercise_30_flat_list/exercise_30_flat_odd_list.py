def flatten_odd(mylist):
    return [int(str(one_el))
            for one_list in mylist
            for one_el in one_list
            if str(one_el).isdigit() and int(one_el) % 2 == 1]
