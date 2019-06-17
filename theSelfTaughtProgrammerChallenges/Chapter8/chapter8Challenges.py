import statistics
import cubed

# Call a different function from the statistics module.
numbers = [2.3, 3.4, 4.5]
result1 = statistics.variance(numbers)
print(result1)


# Import and call the function from another module.
result2 = cubed.cube(2)
print(result2)
