import numpy as np
nums = np.arange(16).reshape(4, 4)
print("Original Array")
print(nums)
header = 'C1 C2 C3 C4'
np.savetxt("Array.txt", nums, fmt='%d', header=header)
loaded_nums = np.loadtxt("Array.txt", skiprows=1)
print("\nLoaded Array")
print(loaded_nums)
