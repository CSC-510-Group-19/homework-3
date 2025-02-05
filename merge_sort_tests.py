import hw2_debugging

def test_merge_empty():
    arr = []
    assert hw2_debugging.merge_sort(arr) == []
    
def test_merge_sorted():
    arr = [1,2,3,4,5]
    assert hw2_debugging.merge_sort(arr) == [1,2,3,4,5]
    
def test_merge_reverse():
    arr = [5,4,3,2,1]
    assert hw2_debugging.merge_sort(arr) == [1,2,3,4,5]
    
def test_merge_rand():
    arr = [2,5,4,1,3]
    assert hw2_debugging.merge_sort(arr) == [1,2,3,4,5]
    
def test_merge_rand_even():
    arr = [2,5,4,6,1,3]
    assert hw2_debugging.merge_sort(arr) == [1,2,3,4,5,6]