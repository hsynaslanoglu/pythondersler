name="Duru"
age=1
sex="girl"
father_name="Burak"

print(str(age)+" yaşındaki "+name+"'nun babasının ismi "+father_name)

tb_boyz = ["Hüseyin","Konkan","Alp","Aksoy","Kaan"]
tb_boyz2 = ["Şükrü","Ali","Alp","Aksoy","Kaan"]

def TB_listeme(tb,tb1):
    print(tb[0]+" "+tb[1]+" "+tb[2]+" "+tb[3]+" "+tb[4])
    print(tb1[0]+" "+tb1[1]+" "+tb1[2]+" "+tb1[3]+" "+tb1[4])

TB_listeme(tb_boyz,tb_boyz2)

a=6
b=2
c=3

def topla_cikar(a,b,c):
    print(a+b-c)

topla_cikar(1,2,3)

print(a)
