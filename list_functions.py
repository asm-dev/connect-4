def find_streak(list, element, size):
    """
    Returns True if in list there are size or more connected (one after another) elements.
    It returns False if there are not size or more connected elements or if size <= 0
    """
    if size > 0:
        # We start our index, counter and our streak indicator
        index = 0
        count = 0
        streak = False

        # While we haven't found size elements conneced elements and the list hasn't ended
        while count < size and index < len(list):
            
            if list[index] == element:
                # If I found the element, I activate the streak indicator and increment the counter
                streak = True
                count = count + 1
            else:
                # If it isn't there, I deactivate the streak indicator and reset the counter
                streak = False
                count = 0
            
            # We move forward to the next element
            index = index + 1
        
        # We return the comparison between counter and size result, AS LONG AS WE'RE ON A STRIKE 
        if streak == True:
            return count >= size
        else:
            return False

    else:
        return False


