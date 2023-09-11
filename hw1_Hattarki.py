__author__ = "Rhishabh Suhas Hattarki"
__date__ = "11 Sept 2023"
__assignment = "SER594: Homework 1 Programming"


def smooth(dat, cutoff=4):
    """
    Applies smoothing to a list containing integer data using Pascal's Triangle technique from HW PDF.
    :param dat: the original numerical data to smooth.
    :param cutoff: the minimum required value for something to count as a max.
    :return: a tuple containing: smoothed, smoothed_stable, maximums, maximum difference
    """
    dat_len = len(dat)
    pascal = [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    smoothed = []
    smoothed_stable = []
    maximums = ['-'] * dat_len
    max_diff = 0

    for idx in range(dat_len):
        cur_smoothed_val = 0
        denominator = 0

        for idx_offset, pascal_idx in zip(range(-5, 6), range(11)):
            cur_idx = idx + idx_offset

            if 0 <= cur_idx < dat_len:
                cur_smoothed_val += pascal[pascal_idx] * dat[cur_idx]
                denominator += pascal[pascal_idx]
        
        cur_smoothed_val /= denominator
        abs_diff = abs(cur_smoothed_val - dat[idx])
        if abs_diff > max_diff:
            max_diff = abs_diff
        smoothed.append(cur_smoothed_val)
        smoothed_stable.append(round(cur_smoothed_val * 10))
    
    i = 0
    while i < dat_len:
        # first element
        if i == 0:
            if (i + 1 < dat_len and smoothed_stable[i+1] < smoothed_stable[i]) or (i == dat_len - 1):
                if dat[i] >= cutoff:
                    print('1')
                    maximums[i] = 'X'
        # last element 
        elif i == dat_len - 1:
            if smoothed_stable[i] > smoothed_stable[i-1] and dat[i] >= cutoff:
                print('2')
                maximums[i] = 'X'
        # any middle element
        else:
            # easy peak
            if smoothed_stable[i-1] < smoothed_stable[i] > smoothed_stable[i+1] and dat[i] >= cutoff:
                print('3')
                maximums[i] = 'X'
            # plateau
            elif smoothed_stable[i] == smoothed_stable[i+1]:
                plateau_start = i
                while i+1 < dat_len-1 and smoothed_stable[i+1] == smoothed_stable[i]:
                    i += 1
                if i+1 < dat_len-1 and smoothed_stable[i+1] > smoothed_stable[i]:
                    i += 1
                    continue
                mid = plateau_start + (i - plateau_start) // 2
                if dat[mid] >= cutoff:
                    print('4')
                    maximums[mid] = 'X'
                
        i += 1


    return smoothed, smoothed_stable, maximums, max_diff


if __name__ == '__main__':
    # feel free to change anything here, this code block will not be graded.

    # sample input
    data = [6, 3, 3, 5, 3, 5, 4, 5, 4, 3, 2, 2, 2, 2, 3, 4, 4, 6, 5, 5, 7, 7, 5, 7, 7, 7, 6, 5, 5, 5]

    smooth_result = smooth(data)

    print(smooth_result[0])
    print(smooth_result[1])
    print("".join(smooth_result[2]))
    print(smooth_result[3])
