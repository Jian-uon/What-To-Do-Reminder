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

    pre  = '<p>Dear {name},</p>'
    suf  = '<p>With best wishes</p>'
    suf += '<p style="color: #9900CC;">What-To-Do Reminder</p>'
    suf += '<p style="color: #CE0000;">稻米会听着人的脚步声慢慢长大</p>'
    suf += '<p>-----------------------------------------------------</p>'
    suf += '<p>If you have any advice to help us to promote our service, please reply this email with no doubt.</p> <p>Thank you.</p>'
    def __init__(self, name, body):
        self.pre = self.pre.format(name = name)
        self.body = body

    def getContext(self):
        return self.pre + self.body + self.suf

        

