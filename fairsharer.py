def fair_sharer(values, num_iterations, share=0.1):
    
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field."""

    
    for x in range(num_iterations):
        
        #Highest number and the index from the list
        highest_value = max(values)
        highest_index = values.index(highest_value)
        
        #If the last element is the highest number, it is distributed to the first number 
        if highest_index == len(values)-1:
            values[highest_index - 1] = values[highest_index - 1] + highest_value * share
            values[0] = values[0] + highest_value * share

            values[highest_index] = highest_value - 2 * (highest_value * share)
            
        #Otherwise the left and right neighbor get the share
        else:
            values[highest_index - 1] = values[highest_index - 1] + highest_value * share
            values[highest_index + 1] = values[highest_index + 1] + highest_value * share

            values[highest_index] = highest_value - 2 * (highest_value * share)
            
        values_new = values

    return values_new
