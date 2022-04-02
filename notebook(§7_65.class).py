#===65.

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
age=manA.get_age()
print(age)