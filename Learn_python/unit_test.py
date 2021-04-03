def average(l):
    if not l:
        return None
    return sum(l)/len(l)
def result():
    assert 3.0 ==average([1,2,3,4,5])

#terminal a giye :pytest (file name.py)