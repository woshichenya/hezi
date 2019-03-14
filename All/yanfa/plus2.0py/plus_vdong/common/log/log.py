#!/usr/bin/python
# encoding: utf-8
import logging
import ctypes
import os


class Logger():
    # logMode: 日志打印级别，值为10: DEBUG_MODE、20: INFO_MODE、30: WARNING_MODE、40: ERROR_MODE
    # logFileName: 日志文件路径名
    # loggerName: 日志器名称
    def __init__(self, logMode, logName):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """
        self.path = '/var/log/plus2.0py_log/'
        self.logMode = logMode
        self.logFileName = '%s%s.log' % (self.path,logName)
        self.loggerName = logName
        self.logger = self.createLogger()
        

    def createLogger(self):
        # 创建一个logger
        logger = logging.getLogger(self.loggerName)
        if self.logMode==10:
            logger.setLevel(logging.DEBUG)
        elif self.logMode==20:
            logger.setLevel(logging.INFO)        
        elif self.logMode==30:
            logger.setLevel(logging.WARNING)
        elif self.logMode==40:
            logger.setLevel(logging.ERROR)
        else:
            print "Wrong logMode"
            return;
                        
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logFileName, mode='a') #模式默认为append。默认情况下，日志文件可以无限增大。
        fh.setLevel(logging.DEBUG)
        
        # 获取线程id,%(thread)d
        # Tid = threading.currentThread().ident
        Tid = ctypes.CDLL('libc.so.6').syscall(186)
        strformat='%(asctime)s %(msecs)d | Pid: %(process)d, Pname: %(processName)s, Tid: {0} | File: %(filename)s, Line: %(lineno)d, Function: %(funcName)s | Log_level: %(levelname)s | Message:\n%(message)s\n'.format(Tid)

        # 定义handler的输出格式
        formatter = logging.Formatter(fmt=strformat,
                                      datefmt='%Y%m%e %H:%M:%S')
        #formatter = format_dict[int(logMode)]
        fh.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        
        return logger
        

    def getLogger(self):
        if not os.path.exists(self.logFileName):
            self.logger = self.createLogger()
        return self.logger