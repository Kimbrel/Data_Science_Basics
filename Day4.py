#Day4

# Question 1

import pandas as pd

print(pd.__version__)

#------------------------------------------------------------

# Question 2

import numpy as np 
import pandas as pd 
  
 
array = np.array([10, 20, 30, 40, 50]) 

series = pd.Series(array)  

#----------------------------------------------------------------

# Question 3

import numpy as np 
import pandas as pd 
  
array = np.array([10, 20, 30, 40, 50]) 
series = pd.Series(array)
a = series.to_frame()

#------------------------------------------------------------------

# Question 4
import seaborn as sb
sb.get_dataset_names()

data = sb.load_dataset('mpg')
#-------------------------------------------------------------------

# Question 5
Answer: usa

#---------------------------------------------------------------------
#Question 6

import seaborn as sb
import pandas as pd
import numpy as np

new_data = []
data = sb.load_dataset('mpg')
ex_data = data['origin']
for x in ex_data:
    if x == 'usa':
        new_data.append(x)
new_data = pd.Series(new_data)
new_data = new_data.to_frame()
print(new_data)

#----------------------------------------------------------------------
