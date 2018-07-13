import os
import re
import copy
import shutil
from googletrans import Translator


# 获取当前目录下所有的css文件路径
def getAllMd (file_dir):
    all_whole_path_files = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            try:
                if (file[-4:] == ".png") or (file[-4:] == ".jpg"):
                    file_info = [root+'/', file]
                    all_whole_path_files.append(file_info)
            except Exception as e:
                print(e)
    return all_whole_path_files
    

# 将中文转换为英文
def getRepName(path_file):
    # 暂时保留后缀
    extension_name = ''
    extension_name = path_file[1].split(".")[-1]
    # 无后缀的文件名
    path_file[1] = path_file[1][0:-len(extension_name)-1]
    # 实例化翻译
    translator = Translator()
    tmp_en_name = translator.translate(path_file[1], dest='en').text
    # 将数字和字母保存到最终的字符串中, 遇到空格则替换为中划线保存
    en_name = ''
    for en_name_str in tmp_en_name:
        # 将大写字母转换为小写字母
        en_name_str = en_name_str.lower()
        # 保留小写字母
        if re.match('[a-z]', en_name_str):
            en_name += en_name_str
        # 将空格转换为"-"
        elif en_name_str == " ":
            en_name += "-"
        else:
            pass
    # 补充后缀名
    path_file[1] = en_name + '.' + extension_name
    return path_file


# 根据相对路径及新旧英文名 创建新文件
def createNewFile(whole_path_file, new_whole_path_file):
    # 在图片的同级目录, 创建一个enName的文件夹
    if os.path.exists(whole_path_file[0] + "./enName/"):
        pass
    else:
        os.makedirs(whole_path_file[0]+ "./enName/")
    # 拷贝创建新的文件
    shutil.copyfile(whole_path_file[0]+whole_path_file[1], new_whole_path_file[0]+"./enName/"+new_whole_path_file[1])
        

def main():
    all_whole_path_files = getAllMd('./')
    for whole_path_file in all_whole_path_files:
        # 获取英文名
        new_whole_path_file = getRepName(copy.deepcopy(whole_path_file))
        print("旧的路径和英文名:", whole_path_file, "新的路径和英文名:", new_whole_path_file)
        # 根据相对路径及新旧英文名创建新文件
        createNewFile(whole_path_file, new_whole_path_file)


if __name__ == '__main__':
    main()