# basic python analysis

# 'generic import' of math module
import math
math.sqrt(25)

# import a function from math
from math import sqrt
sqrt(25)

# import multiple functions at once from math
from math import cos, floor
import os
os.getcwd() # in R, getwd()
os.chdir("C:\Programming\python\mutivariate") # in R, setwd("C:\Programming\python\mutivariate")

# comments in line
"""
Comments in sentences
Brian Heinold, A Practical Introduction to Python Programming, 2012.
Edouard Duchesnay, Tommy Löfstedt. Statistics and Machine Learning in Python, 2018.
"""

# Numbers
10**3           # 1,000
10 / 4          # 2.5
10 / float(4)   # 2.5
5 % 4           # modulo 1 - remainder
10 // 4         # floor division 2

# Boolean operations
# comparisons (these return True)
5 > 3
5 >= 3
5 != 3
5 == 5
# boolean operations (these return True)
5 > 3 and 6 > 3 5 > 3 or 5 < 3 not False

# determine the type of an object
type(2)	    # returns 'int'
type(2.0)	# returns 'float'
type('two')	# returns 'str'
type(True)	# returns 'bool'
type(None)	# returns 'NoneType'

# check if an object is of a given type
isinstance(2.0, int)  	      # returns False
isinstance(2.0, (int, float)) # returns True

# convert an object to a given type
float(2)
int(2.9)
str(2.9)

# zero, None, and empty containers are converted to False
bool(0)
bool(None)
bool('')	# empty string
bool([])	# empty list
bool({})	# empty dictionary

# determine the type of an object
type(2)	    # returns 'int'
type(2.0)	# returns 'float'
type('two')	# returns 'str'
type(True)	# returns 'bool'
type(None)	# returns 'NoneType'

# check if an object is of a given type
isinstance(2.0, int)  	      # returns False
isinstance(2.0, (int, float)) # returns True

# convert an object to a given type
float(2)
int(2.9)
str(2.9)

# zero, None, and empty containers are converted to False
bool(0)
bool(None)
bool('')	# empty string
bool([])	# empty list
bool({})	# empty dictionary

# empty list
empty = []
# empty = list()
empty.append(23)
empty.append(45)
empty

# list slicing [start:end:stride]
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]    # element 0
weekdays[0:3]  # elements 0, 1, 2
weekdays[:3]   # elements 0, 1, 2
weekdays[3:]   # elements 3, 4
weekdays[-1]   # last element (element 4)
weekdays[::2]  # every 2nd element (0, 2, 4)
weekdays[::-1] # backwards (4, 3, 2, 1, 0)
