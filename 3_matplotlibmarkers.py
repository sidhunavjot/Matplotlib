# markers  : you can use to emphesis each point on graph


import matplotlib.pyplot as plt
import numpy as np


y = np.array([3,4,6,9, 10])
plt.plot(y, marker = 'o')
plt.show()

# format strings "fmt" - marker | line | color

import matplotlib.pyplot as plt
import numpy as np


y = np.array([3,4,6,9, 10])
plt.plot(y,  'o:r')
plt.show()

# line references

# : dotted line
# - solid line
# -- dash line
# -. dash/dotted line

#  color reference
# r red
# g green
# b blue
# c cyan
# m magenta
# y yellow
# k black
# w white

# marker size - ms
# marker edge color - mec

import matplotlib.pyplot as plt
import numpy as np


y = np.array([3,4,6,9, 10])
plt.plot(y,  marker = 'o', ms = 20, mec = 'c')
plt.show()

# marker face color - mfc

import matplotlib.pyplot as plt
import numpy as np


y = np.array([3,4,6,9, 10])
plt.plot(y,  marker = 'o', ms = 20, mfc = 'c')
plt.show()



