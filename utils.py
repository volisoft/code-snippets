import os, re, stat, shutil

def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

def rmdir(root, pattern):
    count = 0
    for root, dirs, files in os.walk(root):
        for dir in filter(lambda x: re.match(pattern, x), dirs):
            try:
                path  = os.path.join(root, dir)
                shutil.rmtree(path, onerror=del_rw)
            except:
                if len(path) >= 260:
                    path = u"\\\\?\\" + path
                    shutil.rmtree(path, onerror=del_rw)
                
            
    
rmdir('C:\\voli\workspaces\idea\cpi', "tags")
