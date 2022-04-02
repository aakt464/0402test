#45.イントロダクション　if,for,while  bool,none function try(original errorを作る)


#46. if

print("start")

num=5
total=num+5
print(total)
print("End")


print("Start")



if num >0:
	pass


#47. elif,else



print("SRTRT")
num=5
if num ==0:
	print("zero")
elif num>0:
	print("plus")
#elif num<0:
else:	print("minus")

print("END")

#=====48. if文のネスト

print("START")
num=5
if num>0:
	print("plus")
	if (num%2)==1:
		print("plus, odd")
	else:
		print("plus, even")
elif num<0:
	print("minus")
	if (num%2)==1:
		print("minus, odd")
	else:
		print("minus, even")

else:
	print("zero")

print("END")
#文字を選択してcommand+Dで複数選択

#=====49. and,or


# print(True and True) #True
# print(True and False) #False
# print(False and True) #Flase
# print(False and False) #False
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

person={
	"member":False,
	"age":18,
	"paid":True
}

if person["member"] or person["age"] >= 18 and person["paid"]:
	print("You ca  use a sports club.")
else:
	print("You can't use a sports club.")



#50. ブーリアン(bool)

"""
bool() #ifは条件によって(条件に正しいかどうか)処理を分岐させるが、条件の正誤を返す

True
False


1 == 1.0
1 !="1"
1 <1.1
1<=1.0
1>1.0
2>1.0
1>=1.0

num=5
0<num<=10

#str
"BC"in "ABCD"
"z" not in "ABCD" #存在しなければTrueを返す

#list tuple set


0 in [0,1,2]
3 not in [0,1,2]

#dict
"age" in {"age":18}				Trueを返す(18はfalse)
"friends" not in {"age":18}

"""
true_int = int(True)
false_int =int(False)

print(true_int)
print(false_int)


print(True==1)
print(False==0)

if 1:
	print("<True>") #1はTrue,0はFalseの領域
else:
	print("<False>")

if 0:
	print("<True>")
else:
	print("<False>")
"""
False
	0
	0.0
	""
	[]
	{}
	tuple()
	set()
	None
True
	1,5,10,-1,-5,-10
	0.1,0.5,10.3,-0.1
	"0"," ","ABC"
	[0],[""],[None]
	{0:0}
	(0,)
	{0}
値ではなく何かしら要素を持っているかで判断される
"""

print(not True )
print(not False)
print(not 1)
print(not 0)

#a is b
a="ABC"
b="{}{}{}".format("A","B","C") #"ABC"

print(id(a))
print(id(b))

print(a==b)#値を確認するので文字が違ってもtrueを返す
print(a is b)	#idを確認するので文字の並びがABCと同じでもfalseを返す

#====51.none

d={}
d.setdefault("key")#setdefaultはvalueにnoneが設定されている
print(d)
data=None	#noneはただ一つ
if data is None:
	print("data is None")
if data is not None:
	print("data is not None")


#====52.for

print("Start")

#iterableなオブジェクトとはy０お嘘を反復して取り出すことのできるインターフェースのこと
num_list=[1,2,3,4,5]

for num in num_list:
	print(num)
print("End")
#[](){}set()"String"
#list(range())

r=list(range(5))
#r=list(5)	listに整数を入れるとerrorが出る
print(r,type(r))


print("Start")
for num in range(5):
	print(num)

print("End")


#====53.for(タプル、セット、文字列のループ)　mute


#tuple
for s in ("A","B","C"):
	print(s)

#set
for s in {"A","B","C"}:
	print(s)

#string
for s in "あいうえお漢字ABC":
	print(s)

#tuple
for s in ("Nakamori","Sato","Suzuki"):
	print(s)


#54.for(辞書型のループ)
d={
	"key4":3,
	"key2":1,
	"key1":2,
	"key3":4
}

# for key in d.values():
# 	print("*************************")

for item in sorted(d.values(),reverse=True):
	print(item)

for key, item in d.items():
	print(key)
	print(item)
#=print(key,item)

print("*************************")

for key,item in sorted(d.items(),key=lambda t:t[1]):
	print(key,item)

#===
for item in sorted(d.items(),reverse=True):
	print(item)
for key,item in sorted(d.items(),key=lambda t:t[1],reverse=True):
	print(key,item)

#===55.for loopで使える、便利な関数
#enumurate

iter1=(1,2,3,4,5,6,7)
iter2=["A","B","C","D","E","F","G"]
iter3=range(7)

for z in zip(iter1,iter2,iter3):
	print(z)

iter2=["A","B"]
for z in zip(iter1,iter2,iter3):
	print(z)

import itertools

for z in itertools.zip_longest(iter1,iter2,iter3,fillvalue="ABC"):
	print(z)

	#===56.while

print("Start")
num=0
while num<10:
	print(num)
	num+=1  #この行がなくなると無限にループされる->tools-> Cancel Build
print("End")


#===57.continue,break,else

#continue
for num in range(10):
	if (num%3)==0:
		print(num,"continue")
		continue
	print(num)
print("Done")

#break
for num in range(10):
	if (num%3)==0:
		print(num,"continue")
		break
	print(num)
print("Done")

#else

for num in range(10):
	if (num%3)==0:
		print(num,"continue")
		continue
else:
	print(num)
print("Done")

#while  - continue
num=0
while num<10:
	if (num%3)==0:
		print(num,"break")
		break
	print(num)
	num+=1
else:
	print("ELSE")
print("Done")

while num<10:
	# if (num%3)==0:
	# 	print(num,"break")
	# 	break
	print(num)
	num+=1
else:
	print("ELSE")
print("Done")


#58.関数(def)定義、返り値

def func():
	return
func()
def say_hello():
	#print("hello")
	return "good morning"
say_hello()

greeting=say_hello()
print(greeting)


#===59.[関数]位置関係、キーワード引数、デフォルト引数
def to_even(num):
	if num%2==1:
		return num*1
	else:
		return num
	print("xxx")
result=to_even(56)
print(result)	#56

def to_even(num):
	if num%2==1:
		return num+1
	else:
		return num
	print("xxx")
result=to_even(99)
print(result)	#100

def plus(num1,num2):
	return num1+num2
result=plus(100,5)
#result=plus(100)	#error
print(result)

def plus_5(num1,num2,num3,num4,num5):
	total=num1+num2+num3+num4+num5
	return total
result=plus_5(1,2,3,0,0)
print(result)

#**************************
def plus_list(num_list):
	total=0
	for num in num_list:
		total+=num
	return total
result=plus_list([1,2,3,4,5,6,7,8,9,10])
print(result)

#==========================
def division(divisor,dividend):
	print("{}/{}".format(divisor,dividend))
	return divisor / dividend
result=division(dividend=5,divisor=2)
print(result)

def print_greeting(greeting="Good morning"):
	print(greeting)
	return
print_greeting(greeting="Good Evening")

def func(a,b,c,d=0,e=0,f=0):
	print(a,b,c,d,e,f)
	return
func(100,200,300,f=600)
def func(l=None):
	if l is None:
		l=[]
	l.append(10)
	return l
print(func())
print(func())
print(func())


#===60.[関数]可変長引数*args,**kwargs

max1=max(1,2,3,4,5,11,12,13,14,15)
max2=max(5,6)
print(max1)
print(max2)

#=================================
def function(*args):
	print(args,type(args))
	return
function(1,2,3,4,5)
function(*(1,2,3,4,5))

def func(a,b,c,*args):
	print("a:",a)
	print("b:",b)
	print("c:",c)
	print("args:",args)
func(1,2,3,4,5,6,7,8,9)

#==================================
def func(**kwargs):
	print(kwargs,type(kwargs))
func(a=1,b=2)
d={"a":1,"b":2}
func(**d)
#==================================
"{drive}:{sec}/{filename}.{extension}".format(drive="W",
	sec="sec06",
	filename="sec06",
	file="learning13",
	extension="py")
d={
	"drive":"W",
	"sec":"sec06",
	"filename":"sec06",
	"file":"learning13",
	"extension":"py"
}
s="{drive}:{sec}/{filename}.{extension}".format(**d)
print(s)	#ファイルパス完成

#==================================
def func(a,b,*args,c=0,d=0,**kwargs):
	print("a",a)
	print("b",b)
	print("args",args)
	print("c",c)
	print("d",d)
	print("kwargs",kwargs)
func(1,2,3,4,c=100,d=200,e=300,f=400)

#===60.スコープ

num=10
def func():
	#global num
	num=100
	print("local:",num)
#関数の中local区間 外global空間
func()
print("global:",num)

num=10
def func():
	global num
	num=100
	print("local:",num)
func()
print("global:",num)

num=10
def func():
	print("local:",num)
func()
print("global:",num)

#===62.例外処理(try,except,else,finaly)

divisor=100
dividend=0

#tryにerrorが起こるとexceptに処理がうつる
# try:
# 	result=divisor/dividend
# except Exception as e:
# 	raise e
# 	→→→途中で処理が中断される　 ZeroDivisionError

# print(result)
# print("End")

try:
	result=divisor/dividend
except Exception as e:
	print(e)
	result=0
#raiseを書かなければerrorが出ても処理続行

print(result)
print("End")

try:
	result=divisor/dividend
except ZeroDivisionError as e:
	result=0
except Exception as e:
	raise e

print(result)
print("End")
#=======================
try:
	print("TRY")
except Exception as e:
	print(e)
else:
	print("ELSE")
finally:	#必ず実行される
	print("FINALLY")
print("END")

#===63.カスタム例外
#自分で新しくエラーを作ることが可能

class FilePathNeamingError(Exception):
	pass
raise FilePathNeamingError("File path contains invalid characters.")







