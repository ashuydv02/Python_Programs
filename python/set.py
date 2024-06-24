set1 = {"apple", "banana", "cherry"}
print("Set 1:", set1)

set1.add("orange")
print("After adding 'orange':", set1)

set1.remove("banana")
print("After removing 'banana':", set1)

print("'apple' in set1:", 'apple' in set1)

print("Iterating through set1:")
for item in set1:
    print(item)

set2 = {"apple", "grape", "orange"}
print("Set 2:", set2)

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):", difference_set)

set3 = {x for x in range(10) if x % 2 == 0}
print("Set 3 (even numbers up to 10):", set3)
