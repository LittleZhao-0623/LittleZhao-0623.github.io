import subprocess
import sys
go = input ('您好 确定要开始测试父亲姓氏吗？Y/N')
if go == 'N':
    print ('再见')
elif go == 'Y':
    xing = input ('请问您随父姓吗? Y/N')
    if xing == 'Y':
        name = str(input ('请输入您的姓名'))
        Chinese_name = 0
        English_name = 0
        for ch in name:
            if '\u4e00' <= ch <='\u9fff':
                Chinese_name += 1 
            elif ch.isascii () and ch.isalpha() :
                English_name +=1
        if Chinese_name > 0 and English_name == 0:
             surname = name [:1]
             print ('您父亲的姓氏可能为', surname)
        elif English_name > 0 and Chinese_name == 0:
             parts = name.split()
             surname = parts [-1]
             print ("your father's surname maybe ", surname)
             
        else:
                print ('仅支持中文与英文哦')
    elif xing == 'N':
        print ('正在为您跳转母亲姓氏计算器')
        subprocess.Popen([sys.executable, 
             r"C:\Users\huizh\Desktop\python\test_your_mothers_surname.py"
        ], 
        creationflags=subprocess.CREATE_NEW_CONSOLE)
            