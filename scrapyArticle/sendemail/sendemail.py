from scrapyArticle.sendemail.emailHandler import EmailHandler
from pydispatch import dispatcher
err_spider = object()

def __init__(self):
        #初始化邮件发送次数
        self.mail_count = 0
        dispatcher.connect(self.send_mail, signal=err_spider)
        super(xxx, self).__init__()

def send_mail(self, error):
        "当spider出现error时发送邮件到邮箱"
        if self.mail_count < 1:
            mailmanager = EmailHandler(mail_conf.get('user', ''), mail_conf.get('password', ''))
            mailmanager.send_mail(mail_conf.get('to_add', ''), mail_conf.get('mail_title', ''), 'spider出现错误请及时查看\r%s' % error)
            self.mail_count += 1