import numpy as np
## Option 1
x = np.arange(1,11)

print (x * x)


###Option 2
import numpy as np
x = np.arange(1,11)
y = np.arange(1,11).reshape(10,1)
z = x * y

print (z[x == y])
