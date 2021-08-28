import sys
import os
from file_model import FileList, File


def get_ext(file_name):
    str_arr = file_name.split(".")
    if len(str_arr) == 2:
        return str_arr[1]
    else:
        return None


def traverse(file_list, directory):
    if os.path.dirname(directory) == "auto_compile":
        return
    print(directory)
    for file_name in os.listdir(directory):
        path = os.path.join(directory, file_name)
        print("Path: ", path, " Ext: ", get_ext(file_name))

        if get_ext(file_name) == file_list.file_type:
            file = File(path, file_name, get_ext(file_name))
            file_list.files.append(file)

            # file_list.print_list()

        if os.path.isdir(path):
            print("Helo ", path)
            traverse(file_list, path)


def find_by_ext(origin, ext):
    file_list = FileList(ext)
    traverse(file_list, origin)
    file_list.print_list()
    write_file_list(file_list)


def write_file_list(file_list):
    if os.stat("files.txt").st_size != 0:
        file = open("files.txt", "w")
        file.truncate(0)
        file.close()

    with open("files.txt", "w") as f:
        for file in file_list.files:
            f.write(file.path)
            f.write("\n")


def get_src_path():
    curr_dir = os.path.abspath(os.getcwd())
    path = traverse_back(os.path.basename(curr_dir), curr_dir)
    print(path)
    return path

def get_usr_path(name, send_to_file=False):
    path = os.path.dirname(os.path.abspath(os.getcwd())) + "/" + name
    if send_to_file is True:
        if os.stat("files.txt").st_size != 0:
            file = open("files.txt", "w")
            file.truncate(0)
            file.write(path)
        file.close()

    return path

def traverse_back(name, path):
    if name == "src":
        return path

    parent = os.path.dirname(path)
    name = os.path.basename(parent)

    return traverse_back(name, parent)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        '''if sys.argv[1] == "c":
            print(sys.argv)
            return get_usr_path(name=sys.argv[2], send_to_file=True)'''
        find_by_ext(get_usr_path(sys.argv[1]), sys.argv[2])
    else:
        find_by_ext(get_usr_path(sys.argv[1]), sys.argv[2])
    # get_src_path()
