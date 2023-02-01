def fair_sharer(values, num_iterations, share=0.1):
    
    a = 0
    
    while a < num_iterations:
        
        #Aktzell höchster Wert
        highest_value = max(values)
        
        #Indizes
        index = values.index(highest_value)
        
        #Linker Nachbar
        left = values[index - 1]
        left_value = left + highest_value * share
        values[left] = left_value
        
        
        #Rechter Nachbar
        right = values[index + 1]
        right_value = right + highest_value * share
        values[right] = right_value
        
        highest_value = highest_value * 0.2
        
        a = a + 1
    
    
    return left

