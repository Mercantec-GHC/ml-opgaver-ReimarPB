import numpy as np

feature = np.arange(6, 21)
print(feature)
label = np.vectorize(lambda n: 3 * n + 4)(feature)
print(label)

noise = np.random.randint(low=-2, high=3, size=(len(feature)))
print(noise)
label = np.add(label, noise)
print(label)

