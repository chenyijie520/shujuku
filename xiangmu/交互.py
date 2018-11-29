import pymysql
conn =pymysql.connect('localhost','root','cyj5201314',database='xiangmu',charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
def close():
    cursor.close()
    conn.close()
def show_move():
    sql='''
        select * from move_cyj order by liulan desc limit 20;
    '''
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print('数据更新失败')
        conn.rollback()
def chuan_user():
    sql='''
        select * from move_cyj order by liulan desc limit 20;
    '''
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print('数据更新失败')
        conn.rollback()
def select_all_data():
    sql = """
    SELECT * FROM userinfo_cyj WHERE name_cyj=%s
    """
    try:
        res = mycursor.execute(sql,['cyj'])
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
    close()
    show_move()
    chuan_user()
    select_all_data()
    


if __name__ == '__main__':
    main()