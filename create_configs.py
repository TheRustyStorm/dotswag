import os
configsources=open(os.getenv("HOME")+"/.swagsources",'r')                       #Which tags to use
all_configs=open(os.getenv("HOME")+"/.swagconf",'r')                            #Masterconfigfile
taglist=[]
for configtag in configsources:                                                 #Add every tag to a list
    taglist.append(configtag[:-1]) #Because \n
tagused=False
fileopen=False
configfile=None
for lines in all_configs:
    if lines[0:10]=='###DOTSWAG':                                               #If line is a header
        if fileopen:                                                            #Close file, if open
            configfile.close()
            fileopen=False
        splitted=lines.split('"')                                               #Split Lines at "
        if splitted[1] in taglist:
            tagused=True
            print("Using "+splitted[1])
            print("Writing to "+splitted[3].replace("~",os.getenv("HOME")))     #Debug Info
            configfile=open(splitted[3].replace("~",os.getenv("HOME")),"w")     #Open the destination path
            fileopen=True
        else:
            print("Not using "+splitted[1])                                     #Debug Info
            tagused=False
    elif tagused:
        configfile.write(lines)                                                 #Dont write Header to FIles
configsources.close()
all_configs.close()
configfile.close()                                                              #Close all resources
