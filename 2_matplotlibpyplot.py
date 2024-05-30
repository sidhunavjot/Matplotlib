import matplotlib.pyplot as plt
import numpy as np

# plotting x and y
# plot() function is used to draw points or markers in a diagram

# there are 2 parameters in for specifying points in in the diagram i.e. x-axis and y-axis

x = np.array([1,8])
y = np.array([3, 10])
plt.plot(x,y)
plt.show()

# plotting without line

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8])
y = np.array([3, 10])
plt.plot(x,y,'o')
plt.show()


# plotting many points

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,3,9,8])
y = np.array([3,4,6,9, 10])
plt.plot(x,y,'o')
plt.show()

# plotting line with multiple plots

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,3,9,8])
y = np.array([3,4,6,9, 10])
plt.plot(x,y)
plt.show()

# default x-points
# if we do not provide x-axis values then default values like 0,1,2,3.... will be aloted compared with y-axis

import matplotlib.pyplot as plt
import numpy as np


y = np.array([3,4,6,9, 10])
plt.plot(y)
plt.show()