def max_gold(mine):

    # to figure out if there are anymore paths
    max_length_horizontal = len(mine[0])
    max_length_vertical = len(mine)

    curr_max = 0

    for i in range(len(mine)):


        temp_val = get_max(i,0, max_length_vertical, max_length_horizontal, mine)

        if curr_max < temp_val:
            curr_max = temp_val

    return curr_max


mapping_dict = {}

def get_max(i,j, ending_vertical, ending_horizontal, mine):

    if i < 0 or i >= ending_vertical:
        return 0

    if j >= ending_horizontal:
        return 0

    stored_value = mapping_dict.get("{}_{}".format(i,j))

    if stored_value:
        return stored_value

    curr_val = mine[i][j] + max(get_max(i-1, j+1, ending_vertical, ending_horizontal, mine), \
                                get_max(i, j+1, ending_vertical, ending_horizontal, mine), \
                                get_max(i+1, j+1, ending_vertical, ending_horizontal, mine))

    mapping_dict["{}_{}".format(i,j)] = curr_val

    return curr_val


curr_mine = [[1, 3, 3],
             [2, 1, 4],
             [0, 6, 4]];


print(max_gold(curr_mine))

mapping_dict = {}

curr_mine2 = [[1, 3, 1, 5],
              [2, 2, 4, 1],
              [5, 0, 2, 3],
              [0, 6, 1, 2]];
print(max_gold(curr_mine2))
