from asyncio.windows_events import NULL
import math
from random import random
import numpy as np
import json


with open('my_data.json') as my_data:
  data = json.load(my_data)
  #input_output is the n times n Leontief matrix where each row corresponds to a firm and an associated branded good
  #Row 0 is for labor hours, row 1 is for the standard token and the rest for the goods
  input_output = data['input_output'] 
  #Standard token vector, also known as price vector, dynamic
  price = data['price']
  #Markup vector, also known as market share vector
  markup = data['markup']
  standard_work_time = data['standard_work_time']
  end_time = data['end_time']


n = len(input_output)


productivity = [1/input_output[0][j] for j in range (n)]

#Inverse Leontief
inv_input_output = np.linalg.inv(input_output)


zeroArray = [0 for j in range(n)]
oneArray = [1 for j in range(n)]



