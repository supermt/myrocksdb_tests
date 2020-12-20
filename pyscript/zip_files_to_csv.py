from macros import *
from functions import *


def read_seg(input_file, zip_file_name, start=0, line_count=10, table_name="papers"):
    data_array = []
    for i in range(line_count):
        line = input_file.readline()
        if i % REPORT_GAP:
            print("Read %d records" % i)
        if line == None:
            break
        else:
            data = json.loads(line.decode('utf-8'))
            data_array.append(data)

    output_file = table_name+"."+str(start) + "_" + str(line_count)

    return data_array, output_file


if __name__ == "__main__":
    input_zip_file = DATA_DIR_PREFIX+"/mag_papers_0.zip"
    paper_zip = zipfile.ZipFile(input_zip_file)
    # print(zip.namelist())
    file_list = paper_zip.namelist()
    fd = paper_zip.open(file_list[0])
    data_array, output_file_name = read_seg(
        fd, input_zip_file, 0, SEGMENT_SIZE)

    df = pd.DataFrame(data_array)
    # print(df.iloc[0])
    paper_table_columns = ["id", "title",
                           "n_citation", "doc_type", "publisher"]
    # print(df[])

    csv_file = produce_df(data_array, DATA_DIR_PREFIX + output_file_name,
                          "w", columns=paper_table_columns)

    mysqlimport_command = "mysqlimport -u root -h 127.0.0.1 db2 %s --columns=%s --ignore" % (output_file_name, "".join(
        [x+"," for x in paper_table_columns])[:-1])

    print(mysqlimport_command)
    # result_file_path = produce_df(data_array,output_file_name,"w")

    pass
