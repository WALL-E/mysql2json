#!/usr/bin/env python3.6
#coding:utf-8

import argparse
import datetime

import MySQLdb
import json

class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%dT%H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 


def load_data(args):
    db = MySQLdb.connect(host=args.host, port=args.port, user=args.user, password=args.password, db=args.db, charset=args.charset)
    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    try:
        sql = "select %s from %s" % (args.field, args.table)
        cursor.execute(sql)
        results = cursor.fetchall()
    except MySQLdb.OperationalError as e:
        print("error:", e)
        return None
    except MySQLdb.ProgrammingError as e:
        print("error:", e)
        return None
    db.close()

    return results
   

def main():
    parser = argparse.ArgumentParser(description='Dump data from mysql to json')
    parser.add_argument('--host', type=str, default="127.0.0.1", help='Connect to host')
    parser.add_argument('--port', type=int, default=3306, help='Port number to use for connection')
    parser.add_argument('--user', type=str, default="root", help='User for login')
    parser.add_argument('--password', default="123456", type=str, help='Password to use when connecting to server')
    parser.add_argument('--db', default="qos", type=str, help='Database to use')
    parser.add_argument('--table', default="app_symbol", type=str, help='Table to use')
    parser.add_argument('--field', type=str, default="*", help='Filed to select')
    parser.add_argument('--charset', type=str, default="utf8", help='the connection character set will be changed to this character set')
    args = parser.parse_args()
    data = load_data(args)
    if data:
        json_data = json.dumps(data, ensure_ascii=False, cls=DateEncoder)
        print(json_data)

if __name__ == '__main__':
    main()
