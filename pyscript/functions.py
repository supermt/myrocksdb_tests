from macros import *

# functions


def produce_df(data_array, output_file_name, append_or_write="w",columns=[]):
    df = pd.DataFrame(data_array)
    if len(columns) == 0:
        df = df[table_column_order[output_file_name.split(
            "/")[-1].split(".")[0]]]
    else:
        df = df[columns]

    # remove nan
    df = df.fillna("")
    df = df.astype(str)
    df.to_csv(output_file_name, header=False,
              index=False, sep="\t", mode=append_or_write)

    return os.path.abspath(output_file_name)
