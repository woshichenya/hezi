import psutil

class powel_go():
    def print_cpu(self,time_go):
        if time_go =="":
            time_go=0.3
        # print("cpu个数:\t",psutil.cpu_count())
        m_all = psutil.virtual_memory().total / 1024 / 1024
        # print("全部内存大小为%sM"%m_all)
        # m_new=psutil.virtual_memory().free/1024/1024
        # m_new_bl=float(m_new)/float(m_all)
        # print("剩余内存大小为%sM，剩余占比为%f"%(m_new,m_new_bl*100),"%")
        # m=psutil.virtual_memory().available/1024/1024
        m = psutil.virtual_memory().used / 1024 / 1024
        # print("已使用内存大小为%sM,已用占比为%s"%(m,m/m_all*100),"%")
        m_bl = psutil.virtual_memory().percent
        print(" CPU使用率:\t" + str(psutil.cpu_percent(time_go)) + "%\t|\t内存使用百分比：", m_bl, "\t", m, "M/", m_all, "M")


