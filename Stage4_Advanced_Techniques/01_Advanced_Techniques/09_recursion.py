import os

def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list，包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """

    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                #进入到这里，表明这个目录是文件夹不是文件
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list

if __name__ == '__main__':
    print(get_files_recursion_from_dir("D:/test"))