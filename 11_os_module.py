import os
from datetime import datetime

# + os.getcwd()                                            => get current working directory
# + os.chdir(<path>)                                    => change directory 
# + os.listdir()	                                            => list directory
# + os.mkdir(<dirname>)                           => create a directory
# + os.makedirs(<dirname>)                    => make directories recursively
# + os.rmdir(<dirname>)	                   => remove directory
# + os.removedirs(<dirname>)                => remove directory recursively
# + os.rename(<from>, <to>)                   => rename file
# + os.stat(<filename>)                            => print all info of a file
# + os.walk(<path>)	                          => traverse directory recursively
# + os.environ		                                 => get environment variables
# + os.path.join(<path>, <file>)              => join path without worrying about /
# + os.path.basename(<filename>)     => get basename
# + os.path.dirname(<filename>)         => get dirname
# + os.path.exists(<path-to-file>)         => check if the path exists or not
# + os.path.splitext(<path-to-file>)      => split path and file extension
# + dir(os)			                               => check what methods exists

# print(dir(os));

# os.chdir('./');
# print(os.getcwd());

# for item in os.listdir():
#     print(item);


# os.mkdir("new/");
# print(os.listdir());

# print(os.stat("new"));

# os.rmdir("new");

# print(os.listdir());
files = [];
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    if len(filenames)>0:
        for file in filenames:
            files.append(os.path.join(dirpath,file));
    else:
        continue;


print("Total Files in Directory", len(files));
print(files);