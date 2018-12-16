#位置参数
strTemp = "{0} {1} love {2}".format("I", "do not", "you")
print(strTemp + "  execute successful")
#关键字参数
strTemp = "{a} {b} love {c}".format(a="I", b="do not", c="you")
print(strTemp +"  execute successful")
#关键字参数,关键字位置先后验证,证明关键字与位置无关
strTemp = "{a} {b} love {c}".format(b="do not", a="I", c="you")
print(strTemp +"  execute successful")
#关键字参数,format位置参数和关键字参数混用，证明关键字参数不能作为位置参数使用，若字符串中有位置参数，则format参数
#中也必须提供位置参数
strTemp = "{0} {b} love {c}".format("I",b="do not", a="I", c="you")
print(strTemp +"  execute successful")
#格式化输出测试,占位符格式化
strTemp = "{0:x}".format(100)
print(strTemp)
#%操作测试
#%要与参数成对出现
strTemp = "a = %x %d "%(200,300)
print(strTemp)
#'%#03x'中只有#有效，03无效
strTemp = "a = %#03x %#x "%(4,26)
print(strTemp)
