import sys
import subprocess

def ls(path="."):
    output = subprocess.run(["ls", "-l", path], stdout=subprocess.PIPE, text=True)
    output = str(output.stdout)
    output = output.split("\n")
    output.pop(len(output)-1)
    output.pop(0)
    results = []
    for element in output:
        obj = element.split(" ")
        for i in range(len(obj)-1):
            obj.pop(0)
        string = obj[0]
        results.append(string)
    return results

def mkdir(directory):
    output = subprocess.run(["mkdir", "-p", directory], stdout=subprocess.PIPE, text=True)
    return str(output.stdout)

def rm(file=None,directory=None,force=False):
    if file == None and directory == None:
        print("Error while inwoking rm function : please specify a file or a directory")
        sys.exit(-1)
    if force != False and force != True:
        print("Error : force param must be a boolean")
        sys.exit(-1)
    if file != None:
        if force == False:
            output = subprocess.run(["rm", file], stdout=subprocess.PIPE, text=True)
        else:
            output = subprocess.run(["rm", "-f", file], stdout=subprocess.PIPE, text=True)
    else:
        if force == False:
            output = subprocess.run(["rm", "-r", directory], stdout=subprocess.PIPE, text=True)
        else:
            output = subprocess.run(["rm", "-rf", directory], stdout=subprocess.PIPE, text=True)
    return str(output.stdout)

