import os

def print_directory_tree(startpath, indent_level=0):
    items = os.listdir(startpath)
    items.sort()

    for item in items:
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print('  ' * indent_level + '📁 ' + item)
            print_directory_tree(path, indent_level + 1)
        else:
            print('  ' * indent_level + '📄 ' + item)

print_directory_tree(r'E:\!Learning\Python\dir1')
