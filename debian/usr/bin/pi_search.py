import subprocess
import sys
# home = subprocess.check_output("USER_HOME=$(eval echo ~${SUDO_USER}) && echo ${USER_HOME}", shell=True).decode().strip()
home = sys.argv[1]
# print('home!!  ', home)
# home = '/home/yeji'

def search_info(info_type):
    types = 4
    total_num = 0
    total_result = []
    for i in range(types):
        num, result = search(info_type,i)
        total_num += num
        total_result += result

    f = open('result'+str(info_type)+'.txt', mode='w', encoding='utf-8')
    f.write(str(total_num)+'\n')
    for r in total_result:
        f.write(r+'\n')

    return total_num, total_result

def search(s_type, f_type):
    # ID card number
    if s_type == 0:
        regex = '[0-9][0-9][0-1][0-9][0-3][0-9]-[1-4][0-9][0-9][0-9][0-9][0-9][0-9]'
    # phone number
    elif s_type == 1:
        regex = '010-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
    # address
    elif s_type == 2:
        regex = '(([가-힣]+(시|도)|[서울]|[인천]|[대구]|[광주]|[부산]|[울산])( |)[가-힣]+(시|군|구))( |)((([가-힣]+(d|d(,|.)d|)+(읍|면|동|가|리))(^구|)((d(~|-)d|d)(가|리|)|))([ ](산(d(~|-)d|d))|)|(([가-힣]|(d(~|-)d)|d)+(로|길)))'
    # card number
    elif s_type == 3:
        regex = '[34569][0-9]{3}[-~. ][0-9]{4}[-~. ][0-9]{4}[-~. ][0-9]{4}'

    if f_type == 0:
        num, result = reg_search(regex)
        subprocess.run('echo 0 >> progress.txt', shell=True)
    elif f_type == 1:
        num, result = odt_search(regex)
        subprocess.run('echo 0 >> progress.txt', shell=True)
    elif f_type == 2:
        num, result = hwp_search(regex)
        subprocess.run('echo 0 >> progress.txt', shell=True)
    elif f_type == 3:
        num,result = pdf_search(regex)
        subprocess.run('echo 0 >> progress.txt', shell=True)

    return num, result

# search all type files
def reg_search(regex):   
    try:
        result = subprocess.check_output("grep -orIP --exclude={.*,*.svg,*.png,*.jpg,*.jpeg} --exclude-dir={.*,logs,venv,node_modules,2021-1,git} '"+regex+"' "+home+"/", shell=True, executable='/bin/bash', timeout=None)
        result = result.decode().strip()
        num = 0
        if (result!=""): num = len(result.split('\n'))
        print(num)
        print(result)
        result = result.split('\n')
        return num, result
    except subprocess.CalledProcessError as e: 
        print('no reg_search found: ',regex)
        return 0,""

# search *.odt files
def odt_search(regex):
    result = subprocess.check_output("sudo sh odtsearch.sh '"+regex+"' "+home, shell=True, executable='/bin/bash', timeout=None)
    result = result.decode().strip()
    num = 0
    if (result!=""): num = len(result.split('\n'))
    print(num)
    print(result)
    result = result.split('\n')
    return num, result

# search *.hwp files
def hwp_search(regex):
    result = subprocess.check_output("sudo sh hwpsearch.sh '"+regex+"' "+home+"/", shell=True, executable='/bin/bash', timeout=None)
    result = result.decode().strip()
    num = 0
    if (result!=""): num = len(result.split('\n'))
    print(num)
    print(result)
    result = result.split('\n')
    return num, result

# search *.pdf files
def pdf_search(regex):  
    try:
        result = subprocess.check_output("pdfgrep -orP '"+regex+"' "+home, shell=True, executable='/bin/bash', timeout=None)
        result = result.decode().strip()
        num = len(result.split('\n'))
        print(num)
        print(result)
        result = result.split('\n')
        return num, result
    except subprocess.CalledProcessError as e:
        print ('no pdf file found')
        return 0, ""


for i in range(4):
    search_info(i)