# -*- coding: utf-8 -*-

import scrapy
import json

from pip._vendor import requests


class scrapyd(scrapy.Spider):  # 需要继承scrapy.Spider类
    name = "guokr"  # 定义蜘蛛名

    start_urls = ['https://www.guokr.com/scientific/']

    def parse(self, response):
        '''
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？
        '''

        self.log(response.xpath("//h3//@href").extract())
        self.log(response.xpath("//h3//a//text()").extract())


        self.log(response.xpath("//h1//text()").extract())

        urls = response.xpath("//h3//@href").extract()
        for url in urls:
            yield response.follow(url, callback=self.parse)  # it will filter duplication automatically

        # page = response.url.split("/")[-2]  # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        # filename = 'mingyan-%s.html' % page  # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        # with open(filename, 'wb') as f:  # python文件操作，不多说了；
        #     f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        # self.log('保存文件: %s' % filename)  # 打个日志

    def closed(self, reason):  # 爬取结束的时候发送消息
        self.log('=====>>>>>: start dingtalk rebot')  # 打个日志
        url = 'https://oapi.dingtalk.com/robot/send?access_token='
        params = {"msgtype": "text","text": {"content": "我就是我,  @1730139xxxx 是不一样的烟火"},"at": {"atMobiles": ["1730139xxxx"], "isAtAll": "false"}}
        requests.post(url, data=json.dumps(params), headers={'Content-Type': 'application/json'})
        self.log('=====>>>>>: finish dingtalk rebot')  # 打个日志

        '''self.log('=====>>>>>: start sendmail')  # 打个日志
        from scrapy.mail import MailSender
        # mailer = MailSender.from_settings(settings)# 出错了，没找到原因
        mailer = MailSender(smtphost="smtp.qq.com",  # 发送邮件的服务器
                            mailfrom="xxx@qq.com",  # 邮件发送者
                            smtpuser="xxx",  # 用户名
                            smtppass="xxxxxx",  # 发送邮箱的密码不是你注册时的密码，而是授权码！！！切记！
                            smtpport=465,  # 端口号
                            smtpssl=True
                            )
        body = u""" 
        发送的邮件内容sdfasdfasdfasdfasdfasdfasdf
        """
        subject = u'发送的邮件标题'
        # 如果说发送的内容太过简单的话，很可能会被当做垃圾邮件给禁止发送。
        mailer.send(to=["xxx@qq.com"], subject=subject, body=body)
        self.log('=====>>>>>: finish sendmail')  # 打个日志'''
