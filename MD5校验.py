import hashlib
import os
from tkinter import *
import tkinter.messagebox as messagebox

def get_md5_02(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
        return md5
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
# 对路径下文件夹内的所有文件做md5值计算,并在该目录下生成md5计算文件

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='计算MD5', command=self.md5_cal)
        self.alertButton.pack()
        ######大文件MD5校验##########
    
    def md5_cal(self):
        # md5_file.truncate()
        input_location=self.nameInput.get()
        if input_location=='':
            messagebox.showinfo('Message', '请输入合法路径')
            return
        try:
            list = os.listdir(input_location)  # 列出文件夹下所有的目录与文件
        except FileNotFoundError as e:
            messagebox.showinfo('Message', '此路径不存在')
            return
        md5_file = open(os.path.join(input_location, 'md5_file.txt'), 'w')
        for i in range(0, len(list)):
            path = os.path.join(input_location, list[i])
            if os.path.isfile(path) and path!=os.path.join(input_location, 'md5_file.txt'):
                # 你想对文件的操作
                md5_file.write(os.path.basename(path)+': '+get_md5_01(path)+'\n')
        md5_file.close()

app = Application()
# 设置窗口标题:
app.master.title('MD5校验')
# 主消息循环:
app.mainloop()
