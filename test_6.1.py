
#def myFirstFunction(name,code):
def myFirstFunction(name='lidianjun',code='123456'):
    """ 
    here is function document string
    """
    print("this is my first python function")

    if (name == 'lidianjun') and (code == '123456'):
        print('use default params')
        return 'code_right'
    elif (name == 'shajinzhu') and (code == 123456):
        print('use input information')
        return 'code_right'
    else:
        print('use default params')
        return 'code_wrong'

#help(myFirstFunction)
UseDefaultParams = True
while True:
    if UseDefaultParams == True:
        strName = input('please input name:')
        strCode = input('please input code:')
#        print('name input:' + strName)
#        print('code input:' + strCode)
#        strExtValue = myFirstFunction(strName,strCode)
        strExtValue = myFirstFunction(code=strCode, name=strName)
        print('return code is ' + strExtValue)
        UseDefaultParams = False
    else:
        strName = input('please input name:')
        strCode = input('please input code:')
        strExtValue = myFirstFunction()
        print('return code is ' + strExtValue)
        UseDefaultParams = True 

