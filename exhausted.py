# -*- coding: utf-8 -*-
import psutil
import pymongo

print psutil.cpu_percent(percpu=True)

print psutil.virtual_memory()

# 必要な物、ソケット通信、標準入力ハンドラ。実行状態調査。ファイルロック。


for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline', 'cpu_percent', 'num_threads', 'username', 'memory_percent'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(pinfo)

# mongodb へのアクセスを確立
client = pymongo.MongoClient('127.0.0.1', 27017)

# データベースを作成 (名前: my_database)
db = client.my_database

# コレクションを作成 (名前: my_collection)
co = db.my_collection

# なんか適当に保存
co.insert_one({"test": 3})

# 全部とってくる
for data in co.find():
    print data