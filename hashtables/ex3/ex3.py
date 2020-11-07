def intersection(arrays):
    result = []
    counts = {}
    
    for num in arrays[0]:
        counts[num] = 0
        
    for array in arrays:
        for num in array:
            if num in counts:
                counts[num] += 1
                
    for num in counts:
        if counts[num] == len(arrays):
            result.append(num)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
