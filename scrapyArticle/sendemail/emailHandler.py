#邮件服务封装

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#邮箱信息
MAIL_CONFIG = {
    'user':'xxxxx', #邮箱账号
    'password':'xxxx',  #邮箱授权码
    'to_add':'xxx',  #要发送的邮箱地址
    'mail_title':'scrapy_标题'  #邮件标题
}

class EmailHandler(object):

    def __init__(self,user,password,type = 1):
        """
        :param user:str 发送人邮箱地址（用户名）
        :param password:str 发送人在QQ或163申请的授权码
        :param type:int 0 为QQ邮箱 1 为163邮箱
        """
        self.__QQ = {'smtp':'smtp.qq.com','port':465}
        self.__163 = {'smtp':'smtp.163.com','port':25}
        self.user = user
        self.password = password
        if type == 0:
           self.server=smtplib.SMTP_SSL (self.__QQ['smtp'],self.__QQ['port'])
           self.server.login (self.user,self.password)
        elif type == 1:
           self.server=smtplib.SMTP_SSL (self.__163['smtp'],self.__163['port'])
           self.server.login (self.user,self.password)

    def send_mail(self,To,subject,content):
        """
        :param To:str 接收人邮箱地址
        :param subject:str 邮件标题
        :param content:str 邮件内容
        :return:bool True 成功 False 失败
        """
        try:
            msg = MIMEText(content,'plain','utf-8')
            msg['From'] = formataddr(['spider邮件报警系统',self.user])
            msg['To'] = formataddr(['',To])
            msg['Subject'] = subject

            self.server.sendmail(self.user,To,msg.as_string())
            print("【%s】邮件发送成功"%subject)
            return True
        except Exception as f:
            print("【%s】邮件发送失败,请检查信息"%subject)
            return False