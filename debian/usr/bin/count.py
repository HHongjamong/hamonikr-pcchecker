# count the score of 'check list' and set the score at 'security status'
import subprocess
from datetime import date
import os


# count the score of 'check list'

# count the score of 'password'
def count_pw_score():
    cnt = 0
    total_cnt = 10

    pw_date = subprocess.check_output("sudo passwd -S $PCCHECKER_USER | awk '{print $3}'", shell=True).decode().split(
        '/')
    if date.today() == date(int(pw_date[2]), int(pw_date[0]), int(pw_date[1])):
        pw_date = 0
    else:
        pw_date = int(str(date.today() - date(int(pw_date[2]), int(pw_date[0]), int(pw_date[1]))).split(' day')[0])
    if 1 >= pw_date:
        cnt = 10
    elif 10 >= pw_date:
        cnt = 9
    elif 20 >= pw_date:
        cnt = 7
    elif 40 >= pw_date:
        cnt = 5
    elif 60 >= pw_date:
        cnt = 3
    elif 80 >= pw_date:
        cnt = 1
    pw_score = round(cnt/total_cnt*100)
    return(pw_score)

# count the score of 'update'
def count_update_score():
    cnt = 0
    total_cnt = 10
    osname = subprocess.check_output("lsb_release -i", shell=True).decode().strip()
    if "Hamonikr" in osname:
        update_list = subprocess.check_output("mintupdate-cli list | wc -l", shell=True).decode().strip()
    else:
        update_list = subprocess.check_output("apt list --upgradable | wc -l", shell=True).decode().strip()
    
    if 1 >= int(str(update_list)):
        cnt = 10
    elif 10 >= int(str(update_list)):
        cnt = 9
    elif 20 >= int(str(update_list)):
        cnt = 7
    elif 30 >= int(str(update_list)):
        cnt = 5
    elif 40 >= int(str(update_list)):
        cnt = 3
    elif 50 >= int(str(update_list)):
        cnt = 1
    update_score = round(cnt/total_cnt*100)
    return(update_score)

# count the score of 'ufw'
def count_ufw_score():
    cnt = 0
    total_cnt = 10

    ufw_val = subprocess.check_output("sudo ufw status | awk '{print $2}' | head -1", shell=True).decode().strip()
    if ufw_val == "활성" or ufw_val == "active":
        cnt = 10
    ufw_score = round(cnt/total_cnt*100)
    return(ufw_score)

# count the score of 'backup'
def count_backup_score():
    cnt = 0
    total_cnt = 10

    ts_path = "/timeshift/snapshots"
    if os.path.isdir(ts_path):
        backup_list = subprocess.check_output("ls " + ts_path, shell=True).decode().strip().split('\n')
        backup_list_len = int(len(backup_list))
        if (backup_list_len == 1 and os.listdir(ts_path) == []):
            cnt = 0
        else:
            backup_list = sorted(backup_list, reverse=True)
            bk_date_list = backup_list[0].split('_')[0].split('-')
            bk_date = date(int(bk_date_list[0]), int(bk_date_list[1]), int(bk_date_list[2]))
            diff_day = str(date.today() - bk_date)
            if "0:00:00" == diff_day:
                diff_day = 0
            else:
                diff_day = int(str(date.today() - bk_date).split(' day')[0])
            if 2 > diff_day:
                cnt = 10
            elif 10 > diff_day:
                cnt = 9
            elif 20 > diff_day:
                cnt = 7
            elif 40 > diff_day:
                cnt = 5
            elif 60 > diff_day:
                cnt = 3
            elif 80 > diff_day:
                cnt = 1
    backup_score = round(cnt/total_cnt*100)
    return(backup_score)

#calculate total_score
def count_score():
    score = round((count_pw_score() + count_update_score() + count_ufw_score() + count_backup_score())/4)
    return(score)


# set the score at 'security status'
def set_score():
    # count score
    total_score_val = count_score()

    # set the total score and status
    if 100 == total_score_val:
        total_score_text = "<span color='green' font='40'><b>" + str(total_score_val) + "</b></span><span><b>/100</b></span>"
        total_status_text = "<span color='green' font='80'><b>안전</b></span>"
        total_info_text = "<span>시스템이 안전합니다.</span>"
    elif 60 < total_score_val:
        total_score_text = "<span color='orange' font='40'><b>" + str(total_score_val) + "</b></span><span><b>/100</b></span>"
        total_status_text = "<span color='orange' font='80'><b>주의</b></span>"
        total_info_text = "<span>시스템 관리에 주의가 필요합니다.</span>"
    else:
        total_score_text = "<span color='red' font='40'><b>" + str(total_score_val) + "</b></span><span><b>/100</b></span>"
        total_status_text = "<span color='red' font='80'><b>위험</b></span>"
        total_info_text = "<span>시스템을 관리해 주시기 바랍니다.</span>"
    return (total_score_text, total_status_text, total_info_text)
