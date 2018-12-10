#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-25 21:05:46
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import pymysql
import types

db = pymysql.connect("localhost","root","123456","fiction");

cursor = db.cursor()

# cursor.execute("drop table if exists user")  
# sql="""CREATE TABLE IF NOT EXISTS `user` ( 
#       `id` int(11) NOT NULL AUTO_INCREMENT, 
#       `name` varchar(255) NOT NULL, 
#       `age` int(11) NOT NULL, 
#       PRIMARY KEY (`id`) 
#     ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""  

# cursor.execute(sql)

# sql="INSERT INTO `user` (`name`, `age`) VALUES ('test1', 1);" 





cursor.execute("INSERT INTO `user` (`name`, `age`) VALUES (%s, %s);" ['amy',10]);
db.commit()


db.close()
cursor.close()



