# -*- coding: utf-8 -*-
import psutil
import pymongo
import os
from datetime import datetime
import time
import sys

# print psutil.cpu_percent(percpu=True)

# print psutil.virtual_memory()

# 必要な物、ソケット通信、標準入力ハンドラ。実行状態調査。ファイルロック。


def data_collect():

    # mongodb へのアクセスを確立
    client = pymongo.MongoClient('127.0.0.1', 27017)

    # データベースを作成 (名前: my_database)
    db = client.job_database

    # コレクションを作成 (名前: my_collection)
    co = db.job_collection

    while True:

        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline', 'environ', 'cpu_percent', 'num_threads', 'username', 'memory_percent'])
            except psutil.NoSuchProcess:
                pass
            else:
                pinfo["hostname"] = os.uname()
                pinfo["date"] = date
                co.insert_one(pinfo)

        time.sleep(30)

# なんか適当に保存

    # 全部とってくる
#    for data in co.find():
#        print data


def fork():
    pid = os.fork()

    if pid > 0:
        f = open('/var/run/exhaustedd.pid', 'w')
        f.write(str(pid) + "\n")
        f.close()
        sys.exit()

    if pid == 0:
        data_collect()


if __name__ == '__main__':
    fork()