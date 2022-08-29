import yaml
def get_yaml_data(filedir):
    """
    :param filedir: 文件的路径
    :return: 返回yaml内容
    """
    #1- 文件在磁盘----open函数---在内存去打开
    with open(filedir,encoding='utf-8') as fo:#fo 文件对象
        return yaml.safe_load(fo.read())#使用yaml加载方法去得到文件里内容

if __name__ == '__main__':
    res = get_yaml_data('../config/apiConfig.yml')
    print(res)