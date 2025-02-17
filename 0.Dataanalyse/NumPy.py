import numpy as np

feature = np.arange(6, 21)
print(feature)
label = np.vectorize(lambda n: 3 * n + 4)(feature)
print(label)

noise = np.random.random(len(feature)) * 4 - 2
print(noise)
label = np.add(label, noise)
print(label)

