
#01
l=["A","B","C","D"]
l=[1,2,3]
l=[1,"A"]
print(l)

l=list("ABCDE")
l=list(range(2,5,3)) #要素3:上限数 負の値は降順を表す
print(l)

list(range(10))
list(range(1,10))
list(range(1,10,3))

#error
list_2D=[
["A","B","C"],
list(range(3))
]
print(list_2D)

import glob
import pprint #見やすくするためのライブラリ
dir_list=glob.glob("c:/*")
print(dir_list)
pprint.pprint(dir_list)

#02
num_list=list(range(10))
print(num_list[::2])
print(len(num_list))

list_2D=[
["A","B","C"],
list(range(3))
]
print(list_2D[1][2])

a,b,c=["A","B","C"]
print("a:",a)
print("b:",b)
print("c:",c)


#03
num_list=list(range(10))
num_list[0]=100
num_list[-1]="A"
num_list[0:-1]="A"

#(略)

num_list1=list(range(5))
num_list2=list(range(10,15))
num_list=num_list1+num_list2
num_list1+=num_list2
print(num_list1)


#04

num_list=list(range(10))
num_list.insert(10,"A")
num_list.insert(len(num_list),"A")
print(num_list)
num_list.append(["A","B"])
num_list.extend(["A","B"])
num_list.pop(3)#指定した要素を取り除く
num_list.remove(5) #指定した値を取り除く
print(num_list)
num_list=[5,4]*4
num=5
while num in num_list:
	num_list.remove(num)
print(num_list)
"[value] in [list]"
result=5 in [0,1,2,3,4,5]
print(result)
num_list=[1,5,2,2,3,4,5,2]
count=num_list.count(100)
print(count)
index=num_list.index(2)#値がある要素を返す
print(index)
if 100 in num_list:
	index=num_list.index(100)
	print(index)
random_list=[1,5,8,4,6,2,9,0]
random_list.sort(reverse=True)
random_list.reverse()
print(random_list)
path="w:\\Sublimetext\\sec04"

split_path=path.split("\\")#書き換える箇所
split_path.insert(2,"edit_list")#挿入
new_path="/".join(split_path)#書き換える文字
print(new_path)


#05
num_list1=list(range(1,6))
num_list1=[list(range(1,6))]
num_list2=num_list1[:]
num_list2[0][0]=100

print(num_list1)
print(num_list2)

#06
#映像方講義

#========================
#07
import copy
num_list1=list(range(1,6))
num_list2=num_list1[:]
num_list2=copy.deepcopy(num_list1)
#num_list2[0][0]=100 TypeError: 'int' object does not support item assignment
print("list1:",num_list1,type(num_list1),id(num_list1))
print("list2:",num_list2,type(num_list2),id(num_list2))
print("list1[0]:",num_list1[0],type(num_list1[0]),id(num_list1[0]))
print("list2[0]:",num_list2[0],type(num_list2[0]),id(num_list2[0]))
[[[[1,2,3],4,5,[6,7]],8,9],10]
#[1,2,3]=>[:]



#07
tuple
t=(1,2,3)
t=1,2,3
#NG : t=tuple("A","B","C")
t=tuple("ABC")
t=tuple([1,2,3])
t=(1,)
l=[]
print(t,type(t))
tuple_2D=(
(1,2,3),
[4,5,6])
print(tuple_2D[0][0])
print(tuple_2D[1][1])

t=(1,2,3)
t=tuple("ABC")
t=tuple(range(5))
t=tuple([1,2,3])
t=(1,)#リストと異なり,がないとtupleとして認識されない
l=[]
print(t,type(t))
typle_2D=(
(1,2,3),
[4,5,6]
)
print(tuple_2D[0][0])
print(tuple_2D[1][1])

#==================================
#learning06タプル(編集できないリスト型)のスライス
num_tuple=(1,2,3,4,5,6,7,8,9,10)
num_tuple[0]
num_tuple[1]
#num_tuple[100] #error
num_tuple[-1]
num_tuple[-3]
num_tuple[0:2]
num_tuple[0:-1]
num_tuple[:-1]
num_tuple[:-3]
num_tuple[3:]
num_tuple[:]
num_tuple[::2] #(1, 3, 5, 7, 9)

num_tuple2=num_tuple[:] #スライスで別のデータにすると中身が変わるのでidも変わる ex)num_tuple[1:3]
print(num_tuple,id(num_tuple))
print(num_tuple2,id(num_tuple2))

year, month, day=2019,7,24 #tupleとpythonでは認識される
print(year)
print(month)
print(day)
#タプルの編集、メゾット

#occured error
num_tuple=(1,2,3,4,5)
#num_tuple=[0]=100 #error
#num_tuple[1:4]=["A"."B"."C"]
#---can use method---
	count()
	index()

#データを書き換えたいときtuple型 (＋の演算子で二つのタプルをtらしあわせることができる)
num_tuple=(1,2,3,4,5)
num_tuple2=(11,12,13)
num_tuple=num_tuple+num_tuple2

print(num_tuple)
print(num_tuple2)

# ===str.join()=== # 文字列のjoinメゾットについてみていく
al_tuple=("A","B","C")
al_str="_".join(al_tuple)
print(al_str) #->A_B_C


#learning08

num_tuple5=([1,2,3],[4,5,6])
num_tuple6=num_tuple5
num_tuple6[0][1]=200
print(num_tuple5)
print(num_tuple6)
#->5も6も同様に一つの要素が200に変更される
#6のみを変更する方法　-> -> ->
import copy
num_tuple5=([1,2,3],[4,5,6])
#num_tuple6=num_tuple5
num_tuple6=copy.deepcopy(num_tuple5)
num_tuple6[0][1]=200
print(num_tuple5)
print(num_tuple6)


#=====================
#dict構造:keyとvalueを持つデータ構造 {}でデータ全体を括る learning09
dict
d={"key":"value"}

my_profile={"first_name":"Kotono",
"last_name":"Waki",
"age":20,
"phone":"090-1234-5678",
#1:"one",
#(1,):"tuple"
}
my_profile["city"]="Tokyo" #要素の追加
my_profile["age"]=21

import pprint
pprint.pprint(my_profile) #アルファベット順に改行されて(整理)出力される
print(my_profile["first_name"])#部分的な情報のみ取り出す　存在しない要素は選択できない

my_profile["friends"]="Taro","Hanako"
myfriends={
	"Tom":{"age":32, "phone":"090-1234-5678"},
	"Hanako":{"age":26, "phone":"080-1234-5678"}
}

print(myfriends)
myfriends["Tom"]["hobby"]="Reading"

import pprint
pprint.pprint(myfriends)
print(myfriends["Hanako"])
print(myfriends["Hanako"]["age"])


#=====================================
#learning10 辞書型のメソッド
my_profile={"first_name":"Kotono",
"last_name":"Waki",
"age":20,
"phone":"090-1234-5678",
}

keys=my_profile.keys() #keyのみを取り出す
print(keys)
#print(keys[0])
print(type(keys)) #<class 'dict_keys'>
print(list(keys)) #リスト化


values=my_profile.values() #valueのみを取り出す　*再掲* dict {"key":value}
print(type(values))
print(list(values))

import pprint
items=my_profile.items()
print(items) #dict_itemsが取り出された
print(type(items))　#リスト型でkeyとvalueが入る
pprint.pprint(list(items))


my_profile={"first_name":"Kotono",			#.update()
"last_name":"Waki",
"age":20,
"phone":"090-1234-5678",
}

add_data={
	"friends":["Taro","Hanako"],
	"phone":"080-1234-5678"
}

my_profile.update(add_data)
import pprint
pprint.pprint(my_profile) #updateはkeyが存在しなければ追加し、存在すれば上書きする


my_profile={"first_name":"Kotono",			#.get()
"last_name":"Waki",
"age":20,
"phone":"090-1234-5678",
}
#value=my_profile["friends"] 存在しないためerror -> (存在していれば該当する要素valueを返す)
value=my_profile.get("friends",[])
#存在しなかったためgetメソッドがNoneを返す(errorが出ない)
#							＋データが存在しないとき出力するものを指定できる
print(value)
print(type(value))

my_profile={}
print("1:",my_profile)
my_profile.setdefault("friends",[])			#.setdefault()指定したものが存在すれば何もしない
print("2:",my_profile)
my_profile["friends"].append("Tom")
print("3:",my_profile)

my_profile={"friends":["Hanako"]}
print("1:",my_profile)
my_profile.setdefault("friends",[])			#花子が要素として存在する場合
print("2:",my_profile)
my_profile["friends"].append("Tom")
print("3:",my_profile)

my_profile={"friends":["Hanako"]}
print("1:",my_profile)
#my_profile.setdefault("friends",[])			#.setdefault()の使い方↓
my_profile["friends"]=[] #dictにkeyが存在するかわからない状況で存在すれば[]を渡したい時に使用する
print("2:",my_profile)
my_profile["friends"].append("Tom")
print("3:",my_profile)

#=============================================
#36.辞書型のコピー

d1={						#参照する辞書の中身・id共に変化
	"key1":1,
	"key2":2
}
d2=d1
d2["key2"]=10
d2["key3"]=30
print("d1",d1,id(d1))
print("d2",d2,id(d2))

d1={						#idのみ区別がついた状態 subKey : NG
	"key":{"subKey":1}
}
d2=d1.copy()
d2["key"]["subKey"]=100

print("d1",d1,id(d1))
print("d2",d2,id(d2))

d1={						#OK(ジショガタノコピー)subKeyに違う値が保存された
	"key":{"subKey":1}
}
#d2=d1.copy()
import copy
d2=copy.deepcopy(d1)
d2["key"]["subKey"]=100

print("d1",d1,id(d1))
print("d2",d2,id(d2))



#***=======================================***
#37.集合型(set)

set()
s={1,2,3} #keyとvalueの追記があればdict型、(,)区切りのみはsetと認識される
s=set([1,2,3])#リストからセットへの変換
print(s,type(s))

s=set("ABC")
s=("ABBACCAC")
print(s,type(s))#文字列からsetへの変換＝文字列の順番を保持しない、同じ値や文字は1つになる
l=list({"A","B","C"})
print(l)

l=[1,4,2,3,3,2,4]	#重複のないlistの作り方(setの特性を利用する)
s=set(l)
l=list(s)		#===:  l=list(set(l)) しかし順番が1,2,3,4に並んだ←元に戻したい
print(l)

l=[1,4,2,3,3,2,4]			#元のリストの順番を保持しつつ重複をなくすために
l=sorted(set(l),key=l.index)
#要素として並び替えてlに代入
#l.index: listの各値のindexの値を元にした順番でsorted関数が順番を並び替える
print(l)


#======================================================================
#38.和集合、積集合、差集合、対称差(共通部分を除いた集合範囲)

A={1,2,3,4}
B={3,4,5,6}

union			=A|B
intersection	=A&B
difference_AB	=A-B
difference_BA	=B-A
symmetric_diff	=A^B

print("union:",union)
print("intersection:",intersection)
print("difference_AB:",difference_AB)
print("difference_BA:",difference_BA)
print("symmetric_diff:",symmetric_diff)

#======================================
#39.部分集合、上位集合(Bの範囲をAが覆っている状態)、素集合

#**部分集合
A={1,2}
B={1,2,3}

subset		=A <= B
true_subset	=A <  B

print("Subset:",subset)				#True
print("true_subset:",true_subset)	#True

A={1,2,3}	#3を加えてA=Bにする
B={1,2,3}

subset		=A <= B
true_subset	=A <  B

print("Subset:",subset)
print("true_subset:",true_subset)	#False:真部分集合ではない A=B

#**上位集合
A={1,2,3}
B={1,2}

superset		=A >= B
true_superset	=A >  B

print("Superset:",superset)				#true
print("True Superset:",true_superset)	#true

A={1,2,3}
B={1,2,3}

superset		=A >= B
true_superset	=A >  B

print("Superset:",superset)				#true
print("True Superset:",true_superset)	#false

A={1,2,3}
B={1,2,3}

superset		=A >= B
true_superset	=A >  B

print("Superset:",superset)				#false
print("True Superset:",true_superset)	#false

#素集合
A={1,2}
B={3,4}

disjoint=A.isdisjoint(B) #メソッドisdisjoint()を使用
print("Disjoint:",disjoint)				#True

A={1,2}
B={2,4}

disjoint=A.isdisjoint(B) #メソッドisdisjoint()を使用
print("Disjoint:",disjoint)				#False



#=====================================================
#40.集合型のメソッド
A={"A","B","C"} #setは要素番号で要素を取り出すことができない
print(len(A))
A.add(10)		#要素の追加 .add()

A.discard("B") 	#要素の値を指定して削除したいときに使う関数　存在しない値を指定してもerrorにならない
A.discard("D")
#A.remove("B")	#存在しない値を指定するとerrorになる　

print(A)

A.pop() 		#setの中身の要素を1つ取り出す ！何が取り出されるかはわからない！
print(A)

#=====================================================
#41.集合型のコピー
A={1,2,3,4,5}
B=A
B.add(100)
#idが同じで末尾に100が追加されたものがprintされる
print("A:",A,id(A))
print("B:",B,id(B))

#AとBで異なる結果が出力される
A={1,2,3,4,5}
B=A.copy()
B.add(100)

print("A:",A,id(A))
print("B:",B,id(B))



 #§4.fin




