email=[ ]
f1=open('details.txt','r')
f2=(f1.readlines())
for i in f2 :
    f3=i.split(" ")
    for p in f3:
       if p.endswith(".com"):
           email.append(p)
           print(p)

fp = open('demoemail.txt')
read_demoemail= fp.read()
fp1 = open('details.txt')
details_list = fp1.readlines()
for i in details_list:
    p = i.split(' ')
    print(read_demoemail.format(p[0],p[1],p[-1]))
    print("*********************************")
