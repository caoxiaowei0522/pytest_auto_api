import hashlib
def get_md5_data(psw:str):
    """
    :param psw: 加密前的密码
    :return: 加密后的密码
    """
    #1- 创建md5实例
    md5 = hashlib.md5()
    #2- 调用加密方法
    md5.update(psw.encode('utf-8'))
    return md5.hexdigest()#加密后的结果