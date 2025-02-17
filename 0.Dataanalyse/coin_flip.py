import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

def coin_flip():
    if random.randint(0, 1):
        return "Plat"
    return "Krone"

arr = np.empty(10_000)
arr = np.vectorize(lambda x: coin_flip())(arr)
print(arr)

unique, counts = np.unique(arr, return_counts=True)
frequency = dict(zip(unique, counts))

print()
print("Sandsynlighed for:")
print(f"  Plat: {frequency["Plat"] / len(arr) * 100}%")
print(f"  Krone: {frequency["Krone"] / len(arr) * 100}%")
print()

def get_frequency(a, name):
    unique, counts = np.unique(a, return_counts=True)
    frequency = dict(zip(unique, counts))
    return frequency[name]

probabilities = np.vectorize(lambda x: get_frequency(arr[:x], "Plat") / x)(np.arange(2, len(arr)))
print(probabilities)

fig, ax = plt.subplots()
ax.plot(np.arange(2, len(arr)), probabilities)
plt.show()

