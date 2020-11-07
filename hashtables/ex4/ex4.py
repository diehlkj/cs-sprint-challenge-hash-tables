def has_negatives(a):
    result = []
    the_positives_and_the_negatives = {}
    
    for num in a:
        if num < 0:
            the_positives_and_the_negatives[num] = 0
    for num in a:
        if num > 0 and num - num * 2 in the_positives_and_the_negatives:
            result.append(num)
            

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
