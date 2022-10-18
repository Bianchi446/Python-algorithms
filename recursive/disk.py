import os

def disk_usage(path):
    total= os.path.getsize(path)                     # account for directory usage
    if os.path.isdir(path):                         # if this is a directory
        for filename in os.listdir(path):           # Then for each file of the directory
            childpath = os.path.join(path, filename)    # Compose a full path to child
            total += disk_usage(childpath)              # Add child usage to total

    print('{0:7}'.format(total), path)                   # Descriptive output (optional)
    return total                                        # return the grand total

print(disk_usage("/home/bach/Desktop/python/dsa/recursive"))
