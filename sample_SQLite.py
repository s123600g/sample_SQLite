# Python 2.7
''' 載入(import)套件(libery) '''
from __future__ import print_function
import os
import sqlite3  # SQLite會用到的套件

''' 取得當前的程式專案所在路徑 '''
''' 透過import os的套件內的libery getcwd() '''
getCurrentPath = os.getcwd()

''' 設定SQLite 檔案名稱 '''
SQLite_name = "data.db"
'''設定SQLite資料表名稱 '''
SQLite_table = "data"

''' 連結SQLite '''
dbconn = sqlite3.connect(SQLite_name)
curs = dbconn.cursor()  # 執行SQL查詢語法會用到，用來擷取執行結果資料值

'''
SQL 語法syntax

查詢
SELECT '資料表欄位名稱' FROM '資料表名稱' WHERE '條件'

新增
INSERT INTO '資料表名稱'('放置資料表欄位名稱') VALUES('資料值','資料值'.......)
* >>('放置資料表欄位名稱')<< 可省略不寫，如果沒有要只特別對特定欄位做更動的話

更新
UPDATE '資料表名稱' SET '資料表欄位名稱'='資料值' WHERE '條件式'

刪除
DELETE FROM '資料表名稱' WHERE '資料表欄位名稱' = '資料值'
* 如果沒有WHERE，整個資料表資料都會清空，不會只特定刪除滿足條件的資料列

'''


def start():
    ''' SELECT 查詢 '''
    SQL_select_syntax = '''
    SELECT * FROM {}
    '''.format(SQLite_table)

    SQL_select_syntax2 = '''
    SELECT {},{},{} FROM {}
    '''.format('name', 'number', 'age', SQLite_table)

    SQL_select_syntax3 = '''
    SELECT {},{},{} FROM {} WHERE {} = '{}'
    '''.format('name', 'number', 'age', SQLite_table, 'number', '2')

    ''' INSERT INTO 新增'''
    SQL_insert_syntax = '''
    INSERT INTO {}
    VALUES('{}','{}','{}')
    '''.format(SQLite_table, 'Mary', '6', '35')

    ''' UPDATE 更新'''
    SQL_update_syntax = '''
    UPDATE {}
    SET {} ='{}'
    WHERE {} ='{}'

    '''.format(SQLite_table, 'age', '15', 'number', '3')

    ''' DELETE 刪除'''
    SQL_delete_syntax = '''
    DELETE FROM {}
    WHERE {} = '{}'
    '''.format(SQLite_table, 'number', '6')

# 執行查詢 SQL
    SQL_run = curs.execute(SQL_select_syntax)
    # SQL_run = curs.execute(SQL_select_syntax2)
    # SQL_run = curs.execute(SQL_select_syntax3)

    SQL_result = curs.fetchall()
    print (SQL_result)

    if len(SQL_result) > 0:

        print (SQL_result)

    else:
        print ('Run SQL Error')

# 執行 新增 更新 刪除 SQL
    # SQL_run = curs.execute(SQL_insert_syntax)
#     SQL_run = curs.execute(SQL_update_syntax)
#     SQL_run = curs.execute(SQL_delete_syntax)

    if SQL_run:
        print ('Run SQL 成功.')

        ''' 將更動結果寫進資料庫，寫進去就無法再回頭 '''
        dbconn.commit()

    else:
        print ('Run SQL 失敗')

    ''' 關閉資料庫連接'''
    dbconn.close()


'''
呼叫函式, start沒有回傳值不需要做承接動作，可以用來當作程式開始進入點
程式實作呼叫都可以在start()此函式內完成，也可以不用函式直接實作程式

'''
start()
