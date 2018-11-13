# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : HuJian
# * Email         : swjtu_hj@163.com
# * Create time   : 2018-11-13 18:29
# * Last modified : 2018-11-13 18:29
# * Filename      : ContextBuilder.py
# * Description   : 
# **********************************************************


class ContextBuilder(object):

    pre  = 'Dear {name},\n\n'
    suf  = '\nWith best wishes\n'
    suf += 'What-To-Do Reminder\n\n'
    suf += '-----------------------------------------------------\n'
    suf += 'If you have any advice to help us to promote our service, please reply this email with no doubt. \nThank you.'
    def __init__(self, name, body):
        self.pre = self.pre.format(name = name)
        self.body = body

    def getContext(self):
        return self.pre + self.body + self.suf

        

