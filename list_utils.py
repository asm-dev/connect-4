# These functions help us:
# 1. Find ONE instance of an element in a list, in any position
# 2. Find N instances of an element in a list, in any position
# 3. Find N connected (meaning an element followed by that same element) in a list 

def find_one(list, needle):
    """
    Returns True if it finds needle in the list. Otherwise, it returns False
    """
    return find_n(list, needle, 1)

def find_n(list, needle, n):

    if n > 0:
        # We start the counter of occurences/instances
        # We create an index
        index = 0
        count = 0
        # While I haven't found that element N times and I haven't finished the list...
        while count < n and index < len(list):
            # If the needle is found the counter is updated 
            if needle == list[index]:
                count = count + 1
            # No matter if the needle has been found or not, we update our index
            index = index + 1
        
        # We return the result of comparing N with our counter 
        return count >= n
    else:
        return False

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


