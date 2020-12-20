from macros import *
from functions import *

# logic


input_file = open(DATA_DIR_PREFIX + FILENAME, "r")
output_file_name = DATA_DIR_PREFIX + \
    FILENAME.replace("zip", "csv").replace("txt", "csv")

if os.path.exists(output_file_name):
    print("File exists")
    exit(1)

data_array = []
line = input_file.readline()
while line != "":
    data = json.loads(line)
    line = input_file.readline()
    data_array.append(data)


result_file_path = produce_df(data_array, output_file_name)

mysqlimport_command = "mysqlimport -u root -h 127.0.0.1 db2 %s --columns=%s --ignore" % (output_file_name, "".join(
    [x+"," for x in table_column_order[output_file_name.split("/")[-1].split(".")[0]]])[:-1] )


