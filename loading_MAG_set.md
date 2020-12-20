# Loading the Microsoft Academic Graph dataset

The data set is open accessed in this [link](https://www.microsoft.com/en-us/research/project/open-academic-graph/)

# Create the data tables

## DDL set and import commands

1. mag_venues

create the table
```sql
# Venue Schema
CREATE TABLE venues ( id CHAR(24)  PRIMARY KEY, DisplayName TEXT, NormalizedName text,JournalId VARCHAR(20), ConferenceId VARCHAR(10))ENGINE=RocksDB DEFAULT COLLATE=latin1_bin;
```

```bash
mysqlimport -u root -h 127.0.0.1 db2 /path/to/mag_venues.csv --columns=id,DisplayName,NormalizedName,JournalId,ConferenceId --ignore
```

2. paper_tables

```sql
CREATE TABLE papers ( id CHAR(24)  PRIMARY KEY, title TEXT, n_citation text,doc_type VARCHAR(20), publisher TEXT)ENGINE=RocksDB DEFAULT COLLATE=utf8_general_ci;
```

> In some cases, if you try to load toooooo many rows, it will cause the problem  `mysqlimport: Error: 1296, Got error 10 'Operation aborted: Failed to acquire lock due to rocksdb_max_row_locks limit' from ROCKSDB, when using table: papers`

to solve this problem, you can 
1. rather reduce the number of import batch (for now 100000 is good)
2. ~~or you can increase the option `rocksdb_max_row_locks` by command `set rocksdb_max_row_locks = 1000000000`~~

# Other information

> How to check the disk usage of your tables;
>> `select table_schema, sum((data_length+index_length)/1024/1024) AS MB from information_schema.tables group by 1;`

> How to check the storage and data placement of your table indices;
>> `select d.table_schema, d.table_name, d.index_name, d.index_number,f.sst_name, f.NUM_ROWS, f.ENTRY_DELETES, f.ENTRY_SINGLEDELETES,f.ENTRY_MERGES, f.ENTRY_OTHERS from information_schema.ROCKSDB_DDL d, information_schema.rocksdb_index_file_map as f;`

### Data formatting

Since MySQL forked by Facebook is in version `5.6`, lower than X protocol implemented version `5.7`, we can't use the plugin x protocol

We have to transform the data into `csv` format by this [script](pyscript/Json_to_csv.py) 



## Data loading by mysqlimport client

`mysqlimport -u root -h 127.0.0.1 db_name textfile`



## For `linking relations` tables

The following files shows the linking relation, in json schema, shows the id linking relation between AMiner and MAG
- venue_linking_pairs
- paper_linking_pairs
- author_linking_pairs

These part is not very useful, for we may use only one of the data collection, and these ids really don't have any realworld meaning.

