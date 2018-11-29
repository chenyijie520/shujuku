# 1.复习：
# 步骤：
# １．首先创建连接
# ２．创建游标，去执行ｓｑｌ语句
# ３．目的：ｓｑｌ语句
# ４．使用游标执行ｓｑｌ语句
# ５．提交
# ６．关闭
import pymysql

1.
conn = pymysql.connect('localhost','root','ljh1314','week2homework',charset='utf8')

2.#返回的查询结果数据为元组（元组套元组）
# mycursor = conn.cursor()

#返回的查询结果数据为字典（列表套字典）
mycursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#增
def insert_data():
    #方式sql注入：
    sql = """
    INSERT INTO register (token,name,password,email,gender,age)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    try:
        mycursor.execute(sql,[
            'bxjjasvsckasjbc','ljh','sdsjbckdsjbx',
            'abc@qq.com',0,18
            ])
        #提交
        conn.commit()
        #拿到最后插入的那一条自增长的值
        print(mycursor.lastrowid)
    except:
        conn.rollback()

    #关闭
    mycursor.close()
    conn.close()

#删除
def delete_data():
    sql = """
    DELETE FROM register WHERE num=%s
    """

    try:
        mycursor.execute(sql,[2])
        conn.commit()
    except:
        conn.rollback()

    #关闭：
    mycursor.close()
    conn.close()

#跟新(改)
def update_data():
    sql = """
    UPDATE register SET name=%s WHERE num=%s
    """
    try:
        mycursor.execute(sql,['ljh3',3])
        conn.commit()
    except:
        conn.rollback()

    #
    mycursor.close()
    conn.close()

def select_one_data():
    sql = """
    SELECT * FROM register WHERE name=%s
    """

    try:
        res = mycursor.execute(sql,['ljh3'])
        # res 返回受影响的行数
        print(res)
        #获取一条数据
        print(mycursor.fetchone())
        conn.commit()
    except:
        conn.rollback()

    mycursor.close()
    conn.close()

#select name from　register where name='lijuhao' and password='6508a0f9a8db073ebe8d5c397930fce8'

def select_all_data():
    sql = """
    SELECT * FROM register WHERE name=%s
    """
    try:
        res = mycursor.execute(sql,['ljh'])
        # res 返回受影响的行数
        print(res)
        #获取一条数据
        print(mycursor.fetchall())
        conn.commit()
    except:
        conn.rollback()

    mycursor.close()
    conn.close()


def main():
    #insert_data()
    #delete_data()
    # update_data()
    #select_one_data()
    select_all_data()

    

if __name__ == '__main__':
    main()

