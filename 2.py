k=open('d:/a.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in rangge(0,len(line)):
        char +=1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc, lc=wc+1, lc=1
print("The no.of chars is %d\n The no.of words in%d\n The no.of lines is %d%(char,wc,lc))
