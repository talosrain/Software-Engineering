import random as rd
import sys
#print("请输入难度：0为普通运算，1为复合运算,2为随机运算（普通+复合）")
df=int(sys.argv[1])
#print("是否生成小数，0为不生成，1为生成")
dec=int(sys.argv[2])
#print("10以内运算输入0，100以内运算输入1")
on=int(sys.argv[3])
if (on == 0):
    oo = 10
else:
    oo = 100
#print("请输入需要生成的题目数量")
num_file=int(sys.argv[4])
#print("请输入题目长度")
num_len=int(sys.argv[5])
def df2(num_len,oo,df,dec):
    k=True
    s='+'
    l=0
    f = open('question.txt', 'a')
    f1 = open('answer.txt', 'a')
    if(num_len%2==0):
        num_len-=1
    for i in range(num_len):
        a=rd.choice("+-*/(")
        b=rd.choice("+-*/")
        l+=1
        if(dec==1):
            if (df == 0):
                s = s[:l] + str(round(rd.uniform(1, oo),2))
                s = s[:l + 1] + b
                s = s[:l+2] + str(round(rd.uniform(1, oo), 2))
                l += 2
            elif (k):
                s = s[:l] + str(round(rd.uniform(1, oo),2))
                k = False
            else:
                if (a == "("):
                    s = s[:l] + b
                    s = s[:l + 1] + a
                    s = s[:l + 2] + str(round(rd.uniform(1, oo),2))
                    s = s[:l + 3] + b
                    s = s[:l + 4] + str(round(rd.uniform(1, oo),2))
                    s = s[:l + 5] + ")"
                    s = s[:l + 6] + b
                    l += 6
                    k = True
                else:
                    s = s[:l] + a
                    k = True
        elif(df==0):
            s = s[:l] + str(rd.randint(1, oo))
            s = s[:l+1] + b
            s = s[:l+2] + str(rd.randint(1, oo))
            l+=2
        elif(k):
            s=s[:l]+str(rd.randint(1,oo))
            k=False
        else:
            if(a=="("):
                s = s[:l] + b
                s = s[:l + 1] + a
                s = s[:l + 2]+str(rd.randint(1,oo))
                s = s[:l + 3] + b
                s = s[:l + 4] + str(rd.randint(1,oo))
                s = s[:l + 5] + ")"
                s = s[:l + 6] + b
                l+=6
                k=True
            else:
                s = s[:l] + a
                k = True
    f.write (s)
    f.write ("=")
    f.write('\n')
    f.write('\n')
    f1.write(str((round(eval(s),2)))) 
    f1.write('\n')
for i in range(num_file):
    df2(num_len,oo,df,dec)