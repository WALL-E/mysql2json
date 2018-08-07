# MySQL2JSON
Dump data from mysql to json

## Compatibility

* Python 3.6+

## INSTALL

```
pip3 install mysqlclient
``` 

## RUN

```
./mysql2json.py  --host=127.0.0.1 --port=3306 --user=root --password=123456 --db=qos --table=app_symbol --field=name,created_at
```

## TODO

- [x] 命令行参数
