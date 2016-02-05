# -*- coding: utf-8 -*-
import psutil

print psutil.cpu_percent(percpu=True)

print psutil.virtual_memory()

# 必要な物、ソケット通信、標準入力ハンドラ。実行状態調査。ファイルロック。