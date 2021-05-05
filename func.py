import  csv
import  sys
import  os.path

def open_file():
    global file_name
    if len(sys.argv) == 1:  ## or sys.argv[1][0] == "-" :
        file_name = input("Enter file name: ")
    else :
        file_name = sys.argv[1]

def read_file():
    global file_name
    data = []
    i = 0
    try:
        f = open(file_name, 'r')
        dict_csv = csv.reader(f, delimiter = ",")
        # print(dict_csv)
        for line in dict_csv:
            if i == 0:
                i += 1
                continue

            data.append([float(line[0]) / 1000,float(line[1]) / 1000])

    except:
        sys.exit("Error with " + file_name)

    return data
    # finally:
    #     report.close()

def read_mileage():
    mileage = input("Please enter a mileage: ")
    try:
        mileage = float(mileage)

    except:
        sys.exit("Error with mileage: please enter a number.")
    return (mileage)


def read_theta():
    thetas = []
    try:
        f = open("theta_file.txt", 'r')
        # print(f.readline())
        line = f.readline().split()
        print(line)
        # thetas = float(theta) for theta in line
        if len(line) != 2:
            sys.exit("Error thetas")
        # print(thetas)
        thetas.append(float(line[0]))
        thetas.append(float(line[1]))
        print(thetas)

    except:
        sys.exit("Error with theta_file")
    return (thetas)
    # finally:
    #     report.close()

def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage

def define_thetas(data,theta0, theta1):
    temp0 = 0.0
    temp1 = 0.0
    LearningRate=0.0001
    for i in range(len(data) - 1):
        if i == 0:
            print(estimate_price(theta0, theta1, data[i][0]),  data[i][0], data[i][1])
        temp0 += estimate_price(theta0, theta1, data[i][0]) - data[i][1]
        temp1 += (estimate_price(theta0, theta1, data[i][0]) - data[i][1]) * data[i][0]

    print(temp0 , temp1 )
    temp0 = LearningRate * temp0 / float(len(data))
    temp1 = LearningRate * temp1 / float(len(data))

    # print(temp0, temp1)
    return temp0, temp1

def train_model(data):
    theta0 = 0.0
    theta1 = 0.0
    N = 0

    while True:
        prev_theta0, prev_theta1 = theta0, theta1
        theta0, theta1 = define_thetas(data, prev_theta0, prev_theta1)
        delta_theta0 = prev_theta0 - theta0
        delta_theta1 = prev_theta1 - theta1

        N += 1
        print(N,theta0, theta1, prev_theta0, prev_theta1 )
        break
        # if abs(delta_theta0) < float(0.000001) and abs(delta_theta1) < float(0.000001):
        #     # print(N)
        #     return theta0, theta1
        #     # break

        
    return theta0, theta1
