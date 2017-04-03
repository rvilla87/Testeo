import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = np_weight / np_height ** 2

print("Lista python: " + str(height))
print("Array numpy " + str(np.array(height)))
print("BMI: " + str(bmi))
print("BMI superior a 26: " + str(bmi[bmi > 26]))

a = np.arange(15).reshape(3, 5)  # crea la array con 3 dimensiones de 5 elementos cada uno
print("Array numpy de 2 dimensiones" + str(a))
np.array([[0,  1,  2,  3,  4], [5,  6,  7,  8,  9], [10, 11, 12, 13, 14]])

print("ndim: " + str(a.ndim) + ", shape: " + str(a.shape) + ", size: " + str(a.size) + ", dtype: "
      + str(a.dtype) + ", itemsize: " + str(a.itemsize))


