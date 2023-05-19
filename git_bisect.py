import sys
import subprocess
import os

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Not enough argumets')
        exit(1)
    _, path, hash1, hash2, com = sys.argv
    os.chdir(path)
    hashs = subprocess.check_output(['git', 'log', '--pretty=format:%h'], encoding = 'utf-8').split('\n')
    
    #now run binary search
    l = 0 
    r = len(hashs)
    while r - l > 1:
        middle_commit = (l + r) // 2
        subprocess.call(['git', 'checkout', hashs[middle_commit]], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        p = subprocess.call(com.split(' '),stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if p == 0:
            r = middle_commit
        else:
            l = middle_commit
    print(f'mistooked here {hashs[l]}')
    
    subprocess.run(['git', 'checkout', 'master'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    

