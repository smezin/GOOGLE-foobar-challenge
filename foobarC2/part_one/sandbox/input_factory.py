import random

afile = open("sandbox\input_data.py", "w" )
afile.write('input_list = [')
for i in range(9999):
    line = str(random.randint(1, 2**30))
    afile.write(line+',')
afile.write('1]')
afile.close()