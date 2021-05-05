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
    try:
        f = open(file_name, 'r')
        dict_csv = csv.reader(f, delimiter = ",")
        # print(dict_csv)
        for line in dict_csv:
            data.append(line)

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