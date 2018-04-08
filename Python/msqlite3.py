#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('./pysqlite3.db')

cmnd = conn.cursor()

try:
    cmnd.execute('''
    CREATE TABLE stocks(styles text, score real, times real)
    ''')
except:
    print "already created table... I challnge insert."


cmnd.execute('''
INSERT INTO stocks VALUES ('3,21,21,28_0.5,1,0.25,0.75', 2, 2)
''')

conn.commit()

conn.close
