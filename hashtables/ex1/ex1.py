def get_indices_of_item_weights(weights, length, limit):
    correct_weights = []
    theDict = {}
    
    for i in range(0, length - 1):
        #        weight  :  index
        theDict[weights[i]] = i
        
    for weight in weights:
        if limit - weight in theDict:
            if len(correct_weights) != 0 and weights[correct_weights[0]] < weight:
                correct_weights.insert(0, theDict[weight])
                # print("calc", correct_weights, "weight", weight, "\n\n")
            else:
                correct_weights.append(theDict[weight]) # index
                # print("calc", correct_weights, "weight", weight)
    
    if len(correct_weights) != 0:
        print(correct_weights)
        return correct_weights
    else:
        return None
