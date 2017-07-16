#-*- conding: utf-8-*-
import MySQLdb
import json
import collections

if __name__=="__main__":
    connector = MySQLdb.connect(host="localhost",db="raspberrypi",user="raspberrypi",passwd="teikyo",charset="utf8")
    cursor = connector.cursor()

    f = open('test.json','r')
    json_dict = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

    for index in json_dict:
        print json_dict[index]
        sql = "insert into pens (val) values("+ str(json_dict[index]) +")"
        cursor.execute(sql)

    connector.commit()
    cursor.close()
    connector.close()
