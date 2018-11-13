# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : HuJian
# * Email         : swjtu_hj@163.com
# * Create time   : 2018-11-13 01:00
# * Last modified : 2018-11-13 13:19
# * Filename      : WTDReminderService.py
# * Description   : 
# **********************************************************
# -*- coding: UTF8 -*-
# 
import win32serviceutil 
import win32service 
import win32event
import winerror
import servicemanager
import os, sys, time, copy
import config
from EmailBuilder import EmailBuilder

class PythonService(win32serviceutil.ServiceFramework): 

    _svc_name_ = "WTDReminder"   #  服务名
    _svc_display_name_ = "What-To-Do-Reminder"   # 服务在windows系统中显示的名称
    _svc_description_ = "To remind people of things by email."   #服务的描述
    _promotion_time_list_ = [
            {'time':'23:00', 'isSent':0}, 
            #{'time':'19:03', 'isSent':0}, 
            #{'time':'22:00', 'isSent':0}, 
            #{'time':'19:05', 'isSent':0}, 
            ]

    def __init__(self, args): 
        win32serviceutil.ServiceFramework.__init__(self, args) 
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.run = True

    def _test(self):
        EB = EmailBuilder()
        EB.run()
    
    def _CheckTime(self):
        curTime = time.strftime("%H:%M", time.localtime())
        if curTime == '00:00':
            for item in self._promotion_time_list_:
                item['isSent'] = 0

        to_be_sent_list = self._promotion_time_list_
        for i in range(len(to_be_sent_list)):
            ct = to_be_sent_list[i]['time']
            flag = to_be_sent_list[i]['isSent']
            if ct == curTime and flag == 0:
                to_be_sent_list[i]['isSent'] = 1
                EB = EmailBuilder()
                EB.run()

    def SvcRun(self):
        while self.run:
            # 已经运行
            self._CheckTime()
            #self._test()
            time.sleep(10)   #推迟调用线程<F6>的运行2秒
                
    def SvcStop(self): 
        # 服务已经停止
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) 
        win32event.SetEvent(self.hWaitStop) 
        self.run = False

if __name__=='__main__':
    if len(sys.argv) == 1:
        try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(PythonService)
            servicemanager.Initialize('PythonService', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(PythonService)
