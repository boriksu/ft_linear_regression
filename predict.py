from func import read_theta
from func import read_mileage
from func import estimate_price


thetas = read_theta()
mileage = read_mileage()

print ("estimatePrice(", mileage, ") = ", estimate_price(thetas[0], thetas[1], mileage))