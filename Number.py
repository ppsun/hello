#coding=utf-8
#Python有五个标准数据类型
#Number(数字)  String（字符串）   List（列表）  Tuple(元组)   Dictionary(字典)

#Python数字  数字数据类型用于存储数值，他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象
#当你指定一个值时，Number对象就会被创建
var1 = 12
var2 = 20
print var1,var2

var1 = 24
print var1

#可以使用del语句删除一些对象引用
#del var1
#print var1

var3,var4 = 2,3
print var3,var4

#del var3,var4
print var3,var4


#Python支持四种不同的数值类型
# int（有符号整型）   long（长整型，也可以代表八进制和十六进制）  float（浮点型）  complex（复数）
#复数由实数部分和虚数部分组成，可以用a+bj,或者complex(a,b)表示，复数的实部a和虚部b都是浮点型

int1 = 12
int2 = -777
int3 = 024
int4 = -025
int5 = int1 + int3
print int1,int2,int3,int4,int5

#长整型结尾用L表示，也可以用小写“l”，只是容易与1混淆，最好用大写“L”
long1 = 5192456L
print long1
long2 = 0x2345566L
long3 = -0x2345566L
print long2,long3

float1 = 0.0
float2 = 0.2345
float3 = -98.0
float4 = 22.54e23
float5 = .99
print float1,float2,float3,float4,float5

complex1 = 3.14j
complex2 = 5 + 0.24j
complex3 = .45j
complex4 = -.34 + 0j
complex5 = -77j
complex6 = complex(12,34)
print complex1,complex2,complex3,complex4,complex5,complex6











