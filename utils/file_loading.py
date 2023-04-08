import os, time

def get_files(target):
    file_arr = []
    for file in os.listdir(target):
        path = os.path.join(target, file)
        if os.path.isfile(path):
            file_arr.append ([
                file,
                time.ctime(os.path.getmtime(path)),
                os.path.getsize(path)
            ])
    return file_arr


def load_file(targetFolder, fileName):
    with open(os.path.join(targetFolder, fileName), 'r') as f:
      file = f.read()
    f.close()
    return file