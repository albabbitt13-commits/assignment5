# Problem 1: Find Most Frequent Element
def most_frequent(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) because we still need to look at each number once.
- Worst-case: O(n) when all numbers are different.
- Average-case: O(n).
- Space complexity: O(n) because we store counts in a dictionary.
- Why this approach? A dictionary makes counting fast and simple.
- Could it be optimized? Not really, because every value must be checked at least once.
"""


# Problem 2: Remove Duplicates While Preserving Order
def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
2. Time and Space Analysis:
- Best-case: O(n).
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) for the set and result list.
- Why this approach? A set lets us check duplicates quickly while keeping order in a list.
- Could it be optimized? This is already efficient for this problem.
"""


# Problem 3: Return All Pairs That Sum to Target
def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n).
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) because of the set and output list.
- Why this approach? Using a set avoids nested loops.
- Could it be optimized? This is much faster than checking every pair.
"""


#Problem 4: Simulate List Resizing (Amortized Cost)
def add_n_items(n):
    capacity = 2
    size = 0
    arr = [None] * capacity

    for i in range(n):
        if size == capacity:
            print("Resizing from", capacity, "to", capacity * 2)
            new_arr = [None] * (capacity * 2)
            for j in range(capacity):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity *= 2

        arr[size] = i
        size += 1

"""
4: Time and Space Analysis::
- Resizes happen when the list reaches capacity.
- Worst-case for a single append is O(n) due to copying.
- Amortized time per append is O(1).
- Space complexity: O(n).
- Why does doubling reduce the cost overall? Because resizes happen less often.
"""


#Problem 5: Compute Running Totals
def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

"""
5. Time and Space Analysis:
- Best-case: O(n).
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) because a new list is created.
- It avoids recalculating sums repeatedly.
- This is already the most efficient approach.
"""


# ---- Test cases ----
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(find_pairs([1, 2, 3, 4], 5))
add_n_items(6)
print(running_total([1, 2, 3, 4]))
