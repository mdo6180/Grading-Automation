from os import listdir, system, chdir
from os.path import isdir, isfile
import sys
import subprocess


input_dir = input('Path to folder containing files that need grading: ')
if not isdir(input_dir):
    sys.exit('input directory must be a folder not a file!')

tester_file = input('Path to tester file: ')
if not isfile(tester_file):
    sys.exit('tester file is file not a folder!')

dir_list = sorted(listdir(input_dir))

chdir(input_dir)    # cd into input directory

for i in range(0, len(dir_list)):
    pipe = subprocess.Popen(['python3', tester_file, dir_list[i]],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    output = pipe.stdout.readlines()[-1].decode('UTF-8')      # string is in the form like '10/10'

    print('{}: {}'.format(dir_list[i], output))

    '''
        try:
        score = int(output.split('/')[0])
        max_score = int(output.split('/')[1])
        print('{}: {}'.format(dir_list[i], score))

    except Exception as e:
        print('{}: {}'.format(dir_list[i], e))    
    '''

