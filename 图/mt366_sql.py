import pymysql

class mt366_sql:
    def __init__(self):
        self.__conn=pymysql.connect(user='rain',password='101WANGyu10',host='47.95.6.24',port=3306,db='mt366',use_unicode=True, charset="utf8")
        self.__cur = self.__conn.cursor()

    def insert_imageUrl(self,imageUrl):
        try:
            self.__cur.execute("insert into image_urls (url) values (%s)",imageUrl)
            self.__conn.commit()
        except:
            print(imageUrl+"插入失败！")

    def insert_visitedUrls(self,url,des):
        self.__del_unvisitedUrls(url)
        self.__cur.execute("insert into visited_urls (url,description) values (%s,%s)",(url,des))
        self.__conn.commit()

    def insert_unvisitedUrls(self,url):
        self.__cur.execute("insert into unvisited_urls (url) values (%s)",url)
        self.__conn.commit()

    #判断网址是否存在数据库中
    def url_exist(self,url):
        self.__cur.execute("select * from visited_urls where url = %s",url)
        if self.__cur.rowcount == 1:
            return False
        self.__cur.execute("select * from unvisited_urls where url = %s",url)
        if self.__cur.rowcount == 1:
            return False
        return True

    def __del_unvisitedUrls(self,url):
        self.__cur.execute("delete from unvisited_urls where url = %s",url)
        self.__conn.commit()

    #从未访问网址中获取一个网址
    def get_unvisiteUrl(self):
        self.__cur.execute("select * from unvisited_urls limit 1")
        if self.__cur.rowcount == 0:
            return False
        result = self.__cur.fetchall()[0][0]

        return result

    def get_urlCount(self):
        self.__cur.execute("select * from unvisited_urls")
        unvisited=self.__cur.rowcount
        self.__cur.execute("select * from visited_urls")
        visited = self.__cur.rowcount
        self.__cur.execute("select * from image_urls")
        image = self.__cur.rowcount
        return unvisited,visited,image
