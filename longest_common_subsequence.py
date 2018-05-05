# using a single array (in-place DP)
def get_length_max_subsequence(string1, string2):
    count_val = [0 for i in range(len(string2))]

    for i in range(len(string1)):
        print(count_val)
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                if j !=  0:
                    count_val[j] = max(count_val[j], count_val[j-1]) +1
                else:
                    count_val[j] = count_val[j] + 1
            else:
                count_val[j] = max(count_val[j], count_val[j-1])

    return count_val
