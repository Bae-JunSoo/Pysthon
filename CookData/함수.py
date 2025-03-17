Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> age = 10
>>> print(age)
10
>>> age = 20
>>> print(age)
20
>>> type(age)
<class 'int'>
>>> 
>>> 
>>> print("안녕하세요")
안녕하세요
>>> print(100+100")
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("100+100")
...       
100+100
>>> print("%d" %(100+100))
...       
200
>>> print("%d" %age)
...       
20
>>> print("%s" % age)
...       
20
