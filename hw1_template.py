__author__ = "TODO"
__date__ = "TODO"
__assignment = "SER*94: Homework 1 Programming"


def smooth(dat, cutoff=4):
    """
    Applies smoothing to a list containing integer data using Pascal's Triangle technique from HW PDF.
    :param dat: the original numerical data to smooth.
    :param cutoff: the minimum required value for something to count as a max.
    :return: a tuple containing: smoothed, smoothed_stable, maximums, maximum difference
    """

    # TODO

    return None, None, [], None


if __name__ == '__main__':
    # feel free to change anything here, this code block will not be graded.

    # sample input
    data = [6, 3, 3, 5, 3, 5, 4, 5, 4, 3, 2, 2, 2, 2, 3, 4, 4, 6, 5, 5, 7, 7, 5, 7, 7, 7, 6, 5, 5, 5]

    smooth_result = smooth(data)

    print(smooth_result[0])
    print(smooth_result[1])
    print("".join(smooth_result[2]))
    print(smooth_result[3])
