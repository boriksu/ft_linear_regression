import  csv
import  sys
import  os.path
import  matplotlib.pyplot as plt


def open_file():
    global file_name
    if len(sys.argv) == 1:  ## or sys.argv[1][0] == "-" :
        file_name = input("Enter file name: ")
    else :
        file_name = sys.argv[1]

def read_file():
    global file_name
    global data
    try:
        f = open(file_name, 'r')
        dict_csv = csv.reader(f, delimiter = ",")
        for line in dict_csv:
            data.append(line)

    except:
        sys.exit("Error with " + file_name)

    # finally:
    #     report.close()


file_name = ''
data = []
open_file()
read_file()
print(data)