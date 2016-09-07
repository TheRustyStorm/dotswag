import os
inputfile=open(os.getenv("HOME")+'/.swagconf','r')          #This is the masterconfig, all headers are read here
outputfile=open(os.getenv("HOME")+'/.swagsources','w')      #To choose, which configs have to be read, in this file every used tag is saved
for line in inputfile:                                      #We check every line, whether it starts with our beatiful tag
    if line[0:10] == '###DOTSWAG':
        splitted_line=line.split('"')                       #We split on " , because a path can contain wanky symbols or spaces
        outputfile.write(splitted_line[1]+'\n')             #Every tag is written into a new line in the outputfile
inputfile.close()                                           #Close each file
outputfile.close()

