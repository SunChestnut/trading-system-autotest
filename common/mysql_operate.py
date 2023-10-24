"""
@Author SunYL
@Time 2023/10/24 14:32
"""

import pymysql

from common.yaml_config import GetConf


class MySqlOperate:

    def __init__(self):
        mysql_config = GetConf().get_mysql_config()
        self.host = mysql_config["host"]
        self.db = mysql_config["db"]
        self.port = mysql_config["port"]
        self.user = mysql_config["user"]
        self.password = mysql_config["password"]
        self.conn = None  # 连接
        self.cursor = None  # 游标

    def __conn_mysql(self):
        try:
            self.conn = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.db,
                                        port=self.port, charset="utf8mb4")
        except Exception as e:
            print(e)
            return False
        self.cursor = self.conn.cursor()
        return True

    def __close_mysql(self):
        self.cursor.close()
        self.conn.close()

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        self.__conn_mysql()
        self.cursor.execute(sql)
        query_data = self.cursor.fetchall()
        # 若 query_data 为空的 tuple，则将其值置为 None。为何这样设计❓
        # if query_data == ():
        #     query_data = None
        #     print("The query result is empty")
        self.__close_mysql()
        return query_data

    def insert_update_sql(self, sql):
        self.__conn_mysql()
        self.cursor.execute(sql)
        self.__commit()
        self.__close_mysql()


if __name__ == '__main__':
    res = MySqlOperate().query(
        "select balance from wallet where user_id = (select id from user WHERE user = '周杰伦');")
    print(type(res))
    print(res)
    print(res[0])
    print(res[0][0])
