import hashlib

import logging
##############################
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
##############################

class md5Handle:            #######这是一个将除了sign外的其他入参转换成md5的类
    """ 使用md5工具进行签名 """

    def signature(self, data_source, private_key):           ###需要传入的参数：data_source是一个字典，private_key是私钥
        data_source['key'] = private_key
        # md5签名
        result = hashlib.md5(self.sort_to_str(data_source).encode(encoding='utf-8'))
        # 转化为16进制
        result = result.hexdigest().upper()
        logger.debug("md5签名值是:{}".format(result))
        return result

    @staticmethod
    def sort_to_str(data_source):
        """ 对传入的数据升序排序后并返回 """
        result_str = ""
        logger.debug("排序前的数据是:{}".format(data_source))
        # 对字典升序排序,sorted默认为升序排序
        sorted_result = sorted(data_source.items(), reverse=False)
        logger.debug("排序后的数据是:{}".format(sorted_result))
        # 遍历数组
        for i in range(0, len(sorted_result)):
            data_i = sorted_result[i]
            # 拼接字符串：key1=value1&key2=value2
            d_str = data_i[0] + '=' + data_i[1] + '&'
            result_str = result_str + d_str
        # 截取最后一个&符号
        if len(result_str) > 0:
            result_str = result_str[0:len(result_str) - 1]
            logger.debug("截取最后一个&符号:{}".format(result_str))
        return result_str

'''
if __name__ == "__main__":
    data = {'zhangsan': '19', 'libai': '40', 'baijuyi': '30'}
    key = "1233"
    md5Handle().signature(data, key)
'''