import os
filenames = os.popen('''du -a|awk '{print $2'}|grep \.py''').read()

for file in filenames.split('\n')[:-1]:
    os.system(f'ed - {file} < cmd')
