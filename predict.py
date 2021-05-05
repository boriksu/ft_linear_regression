from func import read_theta
from func import read_mileage


thetas = read_theta()
mileage = read_mileage()

print ("estimatePrice(", mileage, ") = ", thetas[0] + thetas[1] * mileage)