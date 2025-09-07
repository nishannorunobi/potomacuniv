
# mutable_vs_immutable.py

import time

def mutable_example():
    # Using a list (mutable data type)
    a = [1] * (10**6)  # Initial list with 1 million elements
    for _ in range(10**7): # 10 million append operation
        a.append(1)  # Append operation modifies the list in place
    return a

def immutable_example():
    # Using an integer (immutable data type)
    a = 0  # Start with integer value 0
    for _ in range(10**7): # 10 million immutable operation
        a += 1  # Addition operation creates a new integer each time
    return a

def test_operations():
    start_time = time.perf_counter()
    mutable_result = mutable_example()
    mutable_time = time.perf_counter() - start_time
    mutable_time_ns = mutable_time * 10**9  # Convert to nanoseconds

    start_time = time.perf_counter()
    immutable_result = immutable_example()
    immutable_time = time.perf_counter() - start_time
    immutable_time_ns = immutable_time * 10**9  # Convert to nanoseconds

    print(f"Mutable Example Time: {mutable_time_ns:.2f} nano seconds")
    print(f"Immutable Example Time: {immutable_time_ns:.2f} nano seconds")
    
if __name__ == "__main__":
    test_operations()
