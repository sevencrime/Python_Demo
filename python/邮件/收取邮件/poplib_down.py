#coding:utf-8

import poplib
from email.parser import Parser
import base64
import email

def cmps(s):
    # base64用decode_header解码
    scode = email.header.decode_header(s)
    try:
        return scode[0][0].decode('utf-8')
    except AttributeError:
        return s


def get_details(msg):
    # 处理邮件头
    fromstr = msg.get('From')
    from_name, from_url = email.utils.parseaddr(fromstr)
    # print(from_name, from_url)
    name = cmps(from_name)
    print(name)

    tosrt= msg.get('To')
    # print("To:", tosrt)
    # print(email.header.decode_header(tosrt)[0][0].decode('utf-8'))
    to = cmps(tosrt)
    print(to)

    subjectstr = msg.get('Subject')
    # print("Subject:", subjectstr)
    # sub = email.header.decode_header(subjectstr)[0][0]
    # print(sub.decode('utf-8'))
    sub = cmps(subjectstr)
    print(sub)



pop_server = "imap.sina.cn"  #pop服务器
username = "15089514626@sina.cn"    
password = "shengqile"

server = poplib.POP3(pop_server)    #链接服务器
# server.set_debuglevel(1)    #可选项,打印客户端和服务端的交互信息
print(server.getwelcome().decode('utf-8'))  #打印服务器的欢迎信息,验证是否连接成功

# 身份验证
server.user(username)
server.pass_(password)

print(server.stat())    #star()返回邮件总数和总大小

# server.list():
resp, mails, octets = server.list()
print("响应信息： ", resp)
print("所有邮件简要信息： ", mails)
print("list方法返回数据大小（字节）： ", octets)

print("邮件总数为:", len(mails))
up_index = len(mails)
# up_resp, up_mail, up_octets = server.retr(up_index)
up_resp, up_mail, up_octets = server.retr(up_index)

msg_content = b'\r\n'.join(up_mail).decode('utf-8')
# print(msg_content)

# mail-parser将原始电子邮件作为参数，并生成解析对象
msg = Parser().parsestr(text=msg_content)
# print(msg)
print(type(msg))

get_details(msg)


for par in msg.walk():
    # print(par,"Ssssss")
    if not par.is_multipart():
        print("111111111111111111111111111")
        annex = par.get_param("name")   #获取附件名
        if annex:
            h = email.header.Header(annex)
            dh = email.header.decode_header(h)
            fname = dh[0][0]
            print("附件名:", fname)
            data = par.get_payload(decode=True)
            print(data,"333333333333333333333333333")

        else:
            print("elseesleelse")
            data = par.get_payload(decode=True)
            # print(data,"4444444444444444444444444")
            print(data.decode('utf-8'), "55555555555555555555555")






server.close()  #关闭服务










