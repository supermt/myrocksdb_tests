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