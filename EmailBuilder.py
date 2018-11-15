# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : HuJian
# * Email         : swjtu_hj@163.com
# * Create time   : 2018-11-12 19:20
# * Last modified : 2018-11-12 19:20
# * Filename      : EmailBuild.py
# * Description   : 
# **********************************************************
import smtplib
from ExcelTaskReader import ExcelTaskReader
from ContextBuilder import ContextBuilder
from email.mime.text import MIMEText
import config
import time


class EmailBuilder(object):
    
    mail_to_list = config.MAIL_TO_LIST
    user = config.MAIL_USER
    pswd = config.MAIL_PSWD
    host = config.MAIL_HOST

    def __init__(self):
        #self.for_all_user()
        pass

    def run(self):
        self.for_all_user()

    def get_date(self):
        timer = time.localtime(time.time())
        return timer.tm_year, timer.tm_mon, timer.tm_mday

    def for_all_user(self):
        for item in self.mail_to_list:
            name = item['name']
            email = item['email']
            y, m, d = self.get_date()
            tmp = ExcelTaskReader(name)
            tmp.getTasks('{year}.{month}.{day}'.format(year=y, month=m, day=d))
            content = ''
            for item in tmp.todolist:
                content += '<p>' + item[1] + '</p>'

            sub = "Hello {name}! Don't forget these things today!".format(name=name)
            contexter = ContextBuilder(name, content)
            content = contexter.getContext()

            self.send_mail(email, sub, content)

    def send_mail(self, to, sub, content):
        me = 'WTD-Reminder<' + self.user + '>'
        msg = MIMEText(content,_subtype='html',_charset='gb2312')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = to# + ';swjtu_hujian@163.com'
        #print(conten
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.login(self.user, self.pswd)
            server.sendmail(me, to, msg.as_string())
            server.close()
            return True
        except Exception as e :
            print(to, e)
            return False



if __name__ == '__main__':
    EB = EmailBuilder()
    EB.run()
    #a.send_mail('735342728@qq.com', 'send-email-test', 'Rt')
    
