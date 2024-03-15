#File: mathematics/numbers/ series.py

def Sum(*, sumlist = []):
    """ Return the sum of values in list"""
    total = sum(sumlist)
    return total

def average(*,sumlist = []):
    """ Returns the average of list of numbers """
    total = sum(sumlist)
    mean = total/len(sumlist)
    return mean

