def sort(input):
    originalinput = len(input)
    sorted = []

    while len(sorted) != originalinput:
        print(f"{len(sorted)};{originalinput}")
        smallest = None
        for index,i in enumerate(input):
            
            if smallest is None:
                smallest = [i, index]


            elif i<smallest[0]:

                smallest = [i, index]

            else:
                pass
        print(str(smallest) + "abc")
        input.pop(smallest[1])
        sorted.append(smallest[0])

        
    return sorted

        



    