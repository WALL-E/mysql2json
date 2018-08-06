#!/usr/bin/env python3.6

import MySQLdb
import json

def load_data():
    db = MySQLdb.connect("127.0.0.1", "root", "123456", "qos", charset='utf8' )
    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    sql = "select name,base_currency,quote_currency,price_decimal,amount_decimal from app_symbol"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()

    return results
   

def main():
    data = load_data()
    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)

if __name__ == '__main__':
    main()
