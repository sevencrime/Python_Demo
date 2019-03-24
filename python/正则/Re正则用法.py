'''
正则表达式，又称规则表达式，在代码中常简写为regex、regexp或RE，是计算机科学的一个概念。
正则表通常被用来检索、替换那些符合某个模式(规则)的文本。
正则表达式是对字符串（包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为“元字符”））操作的一种逻辑公式，
就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。
正则表达式是一种文本模式，模式描述在搜索文本时要匹配的一个或多个字符串。
'''

'''
首先要清楚，字符串提供的方法是完全匹配
正则表达式则会给我们提供模糊匹配，通过re模块调用
'''
# a = 'Hobbyer is a student!'
# print(a.find('bby'))        # 查找
# chg = a.replace('is','are')     # 替换元素
# print(chg)
# print(a.split('u'))     # 分割
'''
博客园 Infi_chu
'''

import re       # 调用re模块
# print(re.findall('b\b{2}l','Hobbyer is a student!'))      # findall（规则，字符串，修改匹配规则），完全比配

'''
正则元字符(11个)：
.   ^   $   *   +   ?   {}   []   |   ()   \
'''
# #  . 是通配符
a1 = 'hello world'
# print(re.findall('w..l',a1))    # . 只能匹配任意一位，任意一个字符，多了就会不识别
# print(re.findall('w..l','w\norld'))     # . 不能匹配换行符，除了换行符都可以匹配一位
# print(re.split('[a,c]','ddabcffadacd'))     # 有顺序的分割，中间同时出现ac所以会出现空
# print(re.sub('e.l','wc',a1))        # 替换
#
a3 = re.compile('\.com')    # 多次用的方法，提高效率
a3_out = a3.findall('www.example.com.cn')
print(a3_out)
'''
博客园 Infi_chu
'''
# #  ^
# print(re.findall('w...d',a1))
# print(re.findall('^w...d',a1))      # 从最开始匹配，如果有则出现，没有则匹配不到
#
# #  $
# print(re.findall('h...o$',a1))      # 只在结尾匹配
# print(re.findall('w...d$',a1))
#
# #  * 重复前面字符，大于等于零次
# print(re.findall('b.*u','http://www.baidu.com'))    # 重复匹配，好几个点可用一个*表示
# print(re.findall('.*',a1))       # 输出结果后方的''，是另外的情况（空情况，匹配0）
'''
博客园 Infi_chu
'''
# #  + 重复匹配，大于等于1次
# print(re.findall('.+',a1))       # 输出结果必须有，则不会出现空的情况
#
# #  ?  匹配范围零次或1次
# print(re.findall('w?r','wwrr'))     # 可以匹配0-1个字符
#
# #  {} 匹配任意次数
# print(re.findall('w{5}r','wwwrrwwwwwrr'))       # 匹配5个w和1个r
# print(re.findall('w{1,5}r','wwwrrwwwwwrrwr'))    # 匹配1-5次
'''
博客园 Infi_chu
'''
# #  []  是字符集
# print(re.findall('w[c,e]r','wer'))      # []中可以添加任意字符或字符串，多选1
# print(re.findall('w[a-z]','wff'))       # 范围a-z
# print(re.findall('[a,*]','ww'))          # * 不在是之前的功能，在[]之中只是普通的*号，但是（\ ^ -）例外
# print(re.findall('[a-z,0-9,A-Z]','afsasdSFA54asS'))
# print(re.findall('[^c]','acs'))         # ^ 在[]是取反的意思
# print(re.findall('[^a,b]','abcdefg'))  # 非a非b
'''
博客园 Infi_chu
'''
# \
'''
反斜杠后边跟元字符，使其去除特殊功能，
反斜杠后边跟普通字符，使其具有特殊功能
\d  匹配十进制数
\D  匹配任何非数字字符
\s  匹配任何空白字符
\S  匹配任何非空白字符
\w  匹配任何字母字符
\W  匹配任何非字母字符
\b  匹配一个单词和空格间的位置
'''
# print(re.findall('\d{2}','asdw5d31asdw1a3d5s48w4d3a1w')) # 匹配两位数字
# print(re.findall('\swww','fg www')) # 匹配空白字符
# print(re.findall(r's\b','s is a s$udent'))  # \b匹配了特殊字符
# print(re.findall(r's\b','s is a student'))
# c1 = re.search('wc','wsdwcasdwcaff')      # search 只匹配找到的第一个
# print(c1)
# print(c1.group())       # 直接输出匹配内容，但是search没有匹配成功，调用group会报错
# print(re.findall('\\\\c','afekK:\c'))      # 这里注意Python解释器中的转义，交给re模块之后又有转义，所以需要4个
# # print(re.search(r'\bbasd','basd'))         # r表示原生字符串，不需要转义
'''
博客园 Infi_chu
'''
# #  ()  分组
# print(re.search('(wc)+','fswfefwcdwc'))     # 分组
# print(re.search('(wc)+','fswfefwcwc'))
'''
博客园 Infi_chu
'''
# # |  或
# print(re.search('(wc)|ff','ffwca'))     # 或
'''
较高级的用法
'''
# print(re.search('(?P<id>\d{3}z)/(?P<name>\w{3})','weeew34ttt123/ooo'))       # ?P<>起名的格式，名字放在<>中，后面为匹配规则
# print(re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo').group())
# print(re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo').group('id'))
# print(re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo').group('name'))

'''
方法总结
正则表达式的方法：
findall()：返回所有的结果，返回到1个列表当中
search()：返回一个对象（object），返回匹配到的第一个对象，对象可以调用group()方法返回匹配内容
match()：只在字符串开始的时候匹配,返回第一个匹配到的对象
split()：分割点
sub()：替换
compile()：可以用来规定规则
'''

