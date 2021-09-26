filename = 'demo.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))
count=0
for i in lines:
    for j in i:
        if(j!=' '):
            count+=1
        else:
            count+=0
lines = ['#'+str(index)+(9-len(str(index)))*' '+line.rstrip().ljust(maxLength)+'\n'
         for index, line in enumerate(lines)]
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)
with open(filename[:-3]+'_new.py', 'a') as fp:
    fp.write(str(len(lines)))
    fp.write('   ')
    fp.write(str(count))
