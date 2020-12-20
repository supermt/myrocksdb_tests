# compile the modified rocksdb

Download and compile the Rocksdb
```
git clone https://github.com/MariaDB/server.git mariadb
cd mariadb
git submodule init
git submodule update
cmake .
make -j10
```

this will take about 10 to 20 mins. 

# create the mysql.cnf profile with following content for your mysqld server

```
[mysqld]

datadir=../mysql-test/var/install.db
plugin-dir=../storage/rocksdb
language=./share/english

plugin-load=ha_rocksdb
default-storage-engine=rocksdb
```

# run the following shell to set up and run mysqld

```
cd mysql-test; 
./mtr alias
cp -r var/install.db ~/data1
cd ../sql
./mysqld --defaults-file=~/mysql.cnf
```
# use following command to connect to your server

`mysql -h 127.0.0.1 -P 3306 -u root` and use `show plugins` to check the rocksdb engine

# Tese Case

Please read through the markdown file [here](https://github.com/facebook/mysql-5.6/wiki/Data-Loading) to have a better understanding about it.

## `Load data infile` case from MySQL

## `Bulk Loading`, Migration from InnoDB

## `UDB Architecture`, multi client insertion with replica

# Known Shortage of MyRocks

They provide some known issues [here](https://github.com/facebook/mysql-5.6/wiki/MyRocks-limitations)

- Functional defection
  1. Online DDL is not supported (Not important)
  2. EXCHANGE PARTITION does not work in MyRocks yet
  3. Transportable Tablespace, Foreign Key, Spatial Index, and Fulltext Index are not supported
  4. No gap lock (or range lock)
- Data format limitation
  1. binary collation should be on char/varchar indexed column
- Query performance
  1. Slow `Order by DESC/ASC` would be slow. 

# Other references

They provides a paper at [VLDB](http://www.vldb.org/pvldb/vol13/p3217-matsunobu.pdf) and a slide [here](https://www.slideshare.net/matsunobu/myrocks-deep-dive/58)

# Other datasets

Time series datasets:
  - [bitcoin heist ransomware address](https://archive.ics.uci.edu/ml/datasets/BitcoinHeistRansomwareAddressDataset)
LOG dataset projects:
  - [log hub](https://github.com/logpai/loghub)
