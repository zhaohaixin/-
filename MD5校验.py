import hashlib
import os


######大文件MD5校验##########
# def get_md5_02(file_path):
#   f = open(file_path,'rb')
#   md5_obj = hashlib.md5()
#   while True:
#     d = f.read(8096)
#     if not d:
#       break
#     md5_obj.update(d)
#   hash_code = md5_obj.hexdigest()
#   f.close()
#   md5 = str(hash_code).lower()
#   return md5


def get_md5_01(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


rootdir = '/Users/zhaohaixin/Desktop/微信监控'
# 对路径下文件夹内的所有文件做md5值计算,并在该目录下生成md5计算文件


def mdf_cal(rootdir):
    md5_file = open(os.path.join(rootdir, 'md5_file.txt'), 'w')
    # md5_file.truncate()
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            # 你想对文件的操作
            md5_file.write(os.path.basename(path)+': '+get_md5_01(path)+'\n')
    md5_file.close()


mdf_cal(rootdir)
