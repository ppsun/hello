#coding=utf-8
#!/user/bin/env python
print('hello word')
print "hello word"
print("hello word")
print('''hello word''')
#python语句中一般以新行作为语句的结束符


#变量：Python中的变量不需要声明，变量的赋值操作即是变量声明和定义过程
#每个变量在内存中创建，都包含变量的标识，变量名称和变量数据这些信息
#每个变量在使用前都必须赋值，赋值后该变量才会被创建

#单个变量赋值
name = "李四"
age = 18
print name,age
print age

#多个变量赋值

#创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
a = b = c = 1
print a,b,c

#为多个对象指定多个变量; 整型对象1赋值给变量a，浮点型对象0.34赋值给变量b，字符串对象赋值给变量c
a,b,c = 1,0.34,"john"
print(a,b,c)
print a,b,c









