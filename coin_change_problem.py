def get_num_change(num_list, value):
    count_val = [ 0 for i in  range(0, value+1)]

    # intialize intial to 1
    count_val[0] = 1

    for currency_val in num_list:
        for i in range(value+1):

            if i == 0:
                continue

            if currency_val > i:
                continue

            count_val[i] = count_val[i-currency_val] + count_val[i]

    return count_val[-1]
