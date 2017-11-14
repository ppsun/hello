#coding=utf-8

#Python字符串
#字符串或串（String）是由数字、字母、下划线组成的一串字符，它是编程语言中表示文本的数据类型

sting1 = "0123hhhhaa"
print sting1 #输出完整的字符串

string2 = '_hajjaj'
print string2

string3 = '''bl kalkl_233'''
print string3

string4 = "'ah han'"
print string4


#从字符串中获取一段子串，使用变量[开始下标:结束下标]，就可以取到相应的字符串，取到的字符串“包含开始下标，不包含结束下标”
#从左到右：下标从0开始，最大值为字符串长度减1

str = "i love you"

#python返回一个新的对象
print str[2:6] #输出第三个字符到第7个字符之间的字符串（包含第三个字符，不包含第七个字符）

#输出字符串的第一个字符
str1 = str[0]
print str1

#输出从第三个字符开始的字符串（包含第三个字符）
str2 = str[2:]
print str2

#星号*代表乘法，输出字符串三次
str3 = str * 3
print str3

#加号用在字符串时，为字符串连接运算符，空格表示空格
print str + " 逗你玩"

#*和+混合使用
str4 = (str + " 逗你玩 ") * 3
print str4

#输出第一个字符到第七个字符之间的字符串（不包含第七个字符）
print str[:6]




