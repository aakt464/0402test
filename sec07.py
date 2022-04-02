#===64.クラス概要(座学)

#===65.クラス
class Human(object):
	pass
manA=Human()


# print("manA.name:",manA.name)
# print("manA.age:",manA.age)

class Human(object):
	def __init__(self,name="",age=0):
		self.name=name
		self.age=age

	def get_name(self):
		return self.name

	def set_name(self,name):
		self.name=name

	def get_age(self):
		return self.age

	def set_age(self,age):
		self.age=age

manA=Human("Taro",20)
manA=Human()

manA.set_name("Taro")
name=manA.get_name()
print(name)

#manA.set_age(20)
age=mamA.get_age()	#error
print(age)

#===66.クラスの継承 (ノート怪しい)

class Human(object):
	def __init__(self,name="",age=0):
		self.name=name
		self.age=age

	def get_name(self):
		return self.name

	def set_name(self,name):
		self.name=name

	def get_age(self):
		return self.age

	def set_age(self,age):
		self.age=age

# class Student(Human):
# 	pass


# manA=Student("Taro",20)

# name=manA.get_name()
# print(name)

# age=mamA.get_age()	#error
# print(age)

class Student(Human):
	def __init__(self,name="",age=0):
		super().__init__(name,age)
		self.academic_ability={}
	def study(self,subject):
		self.academic_ability.setdefault(subject,0)
		self.academic_ability[subject]+=5
	def get_academjic_ability(self):
		return self.academic_ability

# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self,arg):
# 		super(ClassName,self).__init__()
# 		self.arg=arg

manA=Student("Taro",20)

for num in range(5):
	manA.study("Japanese")
for num in range(10):
	manA.study("English")
for num in range(9):
	manA.study("Math")
print(manA.get_academjic_ability())

#===67.クラス変数

class Test():
	y=10
	def __init__(self):
		self.x=5
	def get_y(self):
		return Test.y
		#return self.__class__.get_y
		# return self.y
	def set_y(self):
		Test.y=555
		self.__class__.y=555
		self.y=555

y=Test.y
print("Test.y",y)
Test.y=500

t1=Test()
print("t1.y:",t1.y)
t1.y=5
t2=Test()
Test.y=1000
print("t1.y:",t1.y)
print("get_y:",t1.get_y())
print("t2.y:",t2.y)

#===68.クラスメソッド・スタティックメソッド
class Test():
	y=10
	def __init__(self):
		self.x=5
	@classmethod
	def get_y(cls):
		return cls.y
	@classmethod
	def set_y(cls):
		cls.y=555
	@classmethod
	def get_x(cls):
		t=cls()
		return t.x


Test.set_y()
print(Test.get_y())
print(Test.get_x())

#===69.Docstring

help(str)

class ClassName(object):
	"""sum(a+b)
	1
	2
	3"""
	def __init__(self,org):
		"""This is init method"""
		super(ClassName,self).__init__()
		self.arg=arg
help(ClassName)

#=======================================

def sum(a,b):
	"""sum(a+b)
	Args:
		a(int or float):num
		b(int or float):num
	Returns:
		int or float: sum result
		Returns an int if both arguments are ints, a float if either argument is a float
	Examples:
		>>> sum(2,5)
		7
	"""
	return a+b

help(sum)






