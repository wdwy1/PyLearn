import pandas as pd
import numpy as np
class1 = pd.read_csv("E:\python大数据\class1.csv");
class2 = pd.read_csv("E:\python大数据\class2.csv");
# print(class2)
class1['banji'] = 1
class2['banji'] = 2
grade = pd.concat([class1,class2])
#score
grade['score'] = grade['chinese'] + grade['math'] +grade['english']
maxscore=grade['score'].max()
maxchinese=grade['chinese'].max()
maxmath=grade['chinese'].max()
maxenglish=grade['english'].max()
print("总分最高为"+str(maxscore)+"分")
print("chinese最高分为"+str(maxchinese)+"分")
print("math最高分为"+str(maxmath)+"分")
print("english最高分为"+str(maxenglish)+"分")
for i in range(0, len(grade)):
    if grade.iloc[i][5]==maxscore:
        print('总分最高同学的班级='+str(grade.iloc[i][4])+'  id='+str(grade.iloc[i][0]))
    if grade.iloc[i][1]==maxchinese:
        print('chinese分最高同学的班级=' + str(grade.iloc[i][4]) + '  id=' + str(grade.iloc[i][0]))
    if grade.iloc[i][2]==maxmath:
        print('math分最高同学的班级=' + str(grade.iloc[i][4]) + '  id=' + str(grade.iloc[i][0]))
    if grade.iloc[i][3]==maxenglish:
        print('english分最高同学的班级=' + str(grade.iloc[i][4]) + '  id=' + str(grade.iloc[i][0]))

#update index
index1 = grade['banji']
index2 = grade['id']
index = pd.MultiIndex.from_arrays([index1,index2],names=['班级','姓名'])
grade.index = index

grade = grade[['chinese','math','english','score']]
print(grade)



