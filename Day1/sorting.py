def sorting(list):
    n_list = list.copy()
    sorted = False
    holder1 = 0
    holder2 = 0
    i = 0

    while(sorted == False):
        if n_list[i] <= n_list[i+1]:
            if i == (len(n_list)-2):
                sorted = True
            i += 1
        elif n_list[i] > n_list[i+1]:
            holder1 = n_list[i]
            holder2 = n_list[i+1]
            n_list[i+1] = holder1
            n_list[i] = holder2
            i = 0

    return n_list