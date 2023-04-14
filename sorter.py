def sort(input):

    sorted = []

    while len(input) != 0:
        smallest = [None,None]
        for index,i in enumerate(input):
            if smallest[0] is not None and i<smallest[0]: 
                smallest = [i, index]  
            else:
                if smallest[0] is not None:
                    pass
                else:
                    smallest = [i, index]  
                
        input.pop(smallest[1])
        sorted.append(smallest[0])

        
    return sorted





    