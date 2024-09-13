'''
数据库操作与断言课程跟课练习
'''
import pymysql

def get_conn():
    connect = pymysql.Connect(host='',
        port=22,
        user='',
        password='',
        database='',
        charset=''
    )
    return connect

def execute_sql(sql):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    record = cursor.fetchone() # 获取到执行的结果，一条信息
    conn.close()
    return record

if __name__ == '__main__':
    print(execute_sql(''))