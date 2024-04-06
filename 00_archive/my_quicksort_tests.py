from my_quicksort import myQuicksort
import random   

def unit_tests():
    flag = "unit test passed"
    edge_cases = (
        [],
        [1],
        [-1],
        [-1,0],
        [-1,-1],
        [0,0],
        [100000000000, 0, -1]
    )
    normal_cases = (
        [1, 3, 2],
        [1, 2, 3],
        [5, 4, 3, 2, 1]
    )

    for arr in edge_cases:
        if sorted(arr) != myQuicksort(arr):
            flag = f"unit test failed at {arr}, need = {sorted(arr)}, my ans = {myQuicksort(arr)}"
            return flag 
    for arr in normal_cases:
        if sorted(arr) != myQuicksort(arr):
            flag = f"unit test failed at {arr}, need = {sorted(arr)}, my ans = {myQuicksort(arr)}"
            return flag 
    
    return flag

def stress_tests():
    flag = "stress test passed"
    len_stress = 1000

    for _ in range(len_stress):
        arr = [random.randint(-1000, 1000) for _ in range(len_stress)]
        
        if sorted(arr) != myQuicksort(arr):
            flag = f"stress test failed at {arr}, need = {sorted(arr)}, my ans = {myQuicksort(arr)}"
            return flag 
    
    return flag
    

def time_test():
    import timeit
    len_tests = 10
    my_time = std_time = 0
    
    setup_code = '''
from my_quicksort import myQuicksort
import random
arrs = [[random.randint(-999, 999) for _ in range(1000)] for _ in range(1000)]
'''
    
    my_time = timeit.timeit(stmt='for arr in arrs: myQuicksort(arr)', setup=setup_code, number=len_tests) / len_tests
    std_time = timeit.timeit(stmt='for arr in arrs: sorted(arr)', setup=setup_code, number=len_tests) / len_tests
    
    return f"my foo avg time == {my_time}, std foo avg time == {std_time}"

if __name__ == "__main__":
    from timeit import default_timer
    import colorama

    timer = default_timer()
    print(unit_tests(),(default_timer() - timer))
    timer = default_timer()
    print(stress_tests(),(default_timer() - timer))
    timer = default_timer()
    print(time_test(), "\ntime_test time ==", (default_timer() - timer))