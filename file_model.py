
class File:
    def __init__(self, path, name, ext):
        self.path = path
        self.name = name
        self.ext = ext

    def print_file(self, indent=False): 
        print("\n--File--\nName: ", self.name, " Ext: ", self.ext, " Path: ", self.path, "\n--EndFile--")

class FileList:
    def __init__(self, file_type):
        self.file_type = file_type
        self.files = []

    def print_list(self):
        print("\n--FileList--")
        for file in self.files:
            file.print_file()
        print("\n")
