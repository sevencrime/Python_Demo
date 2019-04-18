#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

'''
# 中文处理  
def _format_addr(s):  
    name, addr = parseaddr(s)  
    return formataddr((Header(name, 'utf-8').encode(), addr))  
'''

my_sender='17620446727@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='zqy09@saintway.cn, onedi@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量

'''
    发送邮件给多个收件人:
    1,用split(',')分割字符串My_user
    2,msg['To']=formataddr(["多个收件人",",".join(my_users)]) 后面改为",".join(my_users)
    3,server.sendmail(my_sender, my_users, msg.as_string()) 中间收件人参数改为多个邮箱地址
'''

my_users = my_user.split(',') #使用","分割字符串


html = """
<html>
    <body>
        <p> Here is the <a href="http://www.baidu.com"> you wanted. </p>
        <p>邮件演示: </p>
        <img src = "cid: image1"/>
    </body>
</html>

"""

def mail():
    ret=True
    try:

        # MIMEText()只能用一个,用多个的话,只会选择最下面的那个
        # msg=MIMEText('填写邮件内容:妈的,终于成功了','plain','utf-8')     #MIMEText(text,'plain','utf-8') 'plain'代表发送的是text

        # 发送html
        msg = MIMEText(html, 'html', 'utf-8')

        '''
        # 添加附件
        sendfile = open(r'F:\\Python_Demo\\python\\框架\\data.xlsx','rb').read()
        msg = MIMEText(sendfile, 'base64', 'utf-8')
        # msg["Content-Type"] = 'application/octet-stream'
        msg["Content-Type"] = 'multipart/form-data'
        # Content-disposition就是当用户想把请求所得内容存为一个文件的提供一个默认的文件名
        msg["Content-disposition"] = 'attachment; filename="222.xlsx"'
        '''
        
        #发送图片
        sendimagefile = open(r'C:\\Users\\Administrator\\Desktop\\测试apk\\image\\123.jpg', 'rb').read()
        msg = MIMEText(sendimagefile, 'base64', 'utf-8')
        # msg["Content-disposition"] = 'attachment; filename="222.jpg"'   #定义附件的名字
        msg.add_header('Content-ID','<image1>')
        


        msg['From']=formataddr(["发件人邮箱昵称",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人邮箱昵称",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['To']=formataddr(["多个收件人",",".join(my_users)])  #发送邮件给多个收件人
        msg['Subject']="邮件标题" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        # server.set_debuglevel(1)  # 用于显示邮件发送的执行步骤 
        server.login(my_sender ,'xxx')    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception as e:   #如果try中的语句没有执行，则会执行下面的ret=False
        print(e)
        ret=False
    return ret
ret=mail()
if ret:
    print("邮件发送成功") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("邮件发送失败filed")  #如果发送失败则会返回filed