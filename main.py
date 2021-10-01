"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
partners Jared and Bharat
"""
# no imports needed.
#`pip3 install pytest`
#import tabulate

def foo(x):

    ### TODO
    if x<=1:
        return x
    else:
        ra,rb= foo(x-1), foo(x-2)
        return ra+rb
    pass

def longest_run(mylist, key):
    ### TODO
    a= 0
    b= 0
    for num in mylist:
        if num== key:
            b+= 1
        else:
            if a< b:
                a= b
            b= 0
    return max(a, b)
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))



def longest_run_recursive(mylist, key):
    ### TODO
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    Result1 = longest_run_recursive(mylist[:len(mylist) // 2], key)
    Result2 = longest_run_recursive(mylist[len(mylist) // 2:], key)
    is_entire_range = Result1.is_entire_range and Result2.is_entire_range
    left_side = Result1.left_size + (1 if Result1.is_entire_range else 0) * Result2.left_size
    right_side = Result2.right_size + (1 if Result2.is_entire_range else 0) * Result1.right_size
    longest_size = max(Result1.longest_size, Result2.longest_size, Result1.right_size + Result2.left_size)
    return Result(left_side, right_side, longest_size, is_entire_range)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

if __name__== '__main__':
	test_longest_run()
