import  csv
import  sys
import  os.path
import  matplotlib.pyplot as plt
from func import open_file
from func import read_file
from func import train_model


file_name = ''
open_file()
data = read_file()

# print(data)

theta0, theta1 = train_model(data)
# print(theta0, theta1)

