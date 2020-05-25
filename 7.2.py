with open('C:/test/text.txt','r') as myfile:
    count = sum(1 for line in myfile)
