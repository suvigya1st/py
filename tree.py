import sys, math
user_input = raw_input()
list1 = [int(i) for i in user_input.split(' ') if i.isdigit()]
length = len(list1)
level = (math.log(length)/math.log(2)) + 1
if math.floor(level)!=level: sys.exit()
max_val = False if level%2==0 else True
list2 = []
while length!=1:
    for j in range(0,length/2):
        for i in range(0,length,2):
            list2.insert(len(list2),max(list1[i],list1[i+1])) if max_val==False else list2.insert(len(list2),min(list1[i],list1[i+1]))
        max_val = not max_val
        length=length/2
        list1=list(list2)
        list2=list()
print "ANS = ", list1[0]
