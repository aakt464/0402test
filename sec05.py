#* ctrl(command)+shift(alt,option)+/ ->複数業コメントアウト

#42.演習の内容について、43.filedialog, copyfile
"""
#===41.code
import shutil		#(エスエイチユーティル)
#from tkinter import filedialog

#ファイルの複製とファイル名の変更(Python上)
get_file_form=filedialog.askopenfilename()	#filedialogの参照
print(get_file_form)	#開かれるfinderから対象のファイルを選択するとfiledialogが得られる

file_from=("/Users/kotono/Desktop/Sublimetext/0906")
file_to="/Users/kotono/Desktop/Sublimetext/0906_2"

shutil.copyfile(file_from,file_to)		#0906_2として0906を複製


"""
#演習のためのファイル複製
import shutil		#(エスエイチユーティル)
from tkinter import filedialog

#ファイルの複製とファイル名の変更(Python上)
get_file_form=filedialog.askopenfilename()	#filedialogの参照
print(get_file_form)	#開かれるfinderから対象のファイルを選択するとfiledialogが得られる

file_from=("/Users/kotono/Desktop/Sublimetext/0906.py")
file_to="/Users/kotono/Desktop/Sublimetext/0906_01.py"

shutil.copyfile(file_from,file_to)		#0906_1として0906を複製


#===42.code 解答例
import shutil		#(エスエイチユーティル)
from tkinter import filedialog

#file_from=filedialog.askopenfilename() #/Users/kotono/Desktop/Sublimetext/0906.py

file_from="/Users/kotono/Desktop/Sublimetext/0906_01.py"

split_path=file_from.split("/") #['', 'Users', 'kotono', 'Desktop', 'Sublimetext', '0906.py']


basename=split_path[-1] #ファイル名は必ず最後に来るため	"print(1+1).py"
print(basename)
filename=basename.split(".")[0]
print(filename)
old_ver=filename.split("_")[-1]
print(old_ver)
ver_num=filename[-2:] 	#(1+1)←なし
print(ver_num)
increament=int(ver_num)+1
new_ver="v{:02}".format(increament)	#_v02
file_to=file_from.replace(old_ver,new_ver)
print(new_ver)
print(file_to)	#/Users/kotono/Desktop/Sublimetext/0906_v02.py

# shutil.copyfile(file_from,file_to)
# print("File Form:",file_from, file_to)
# print("File_To:", file_to)


"""??
演習途中(講義もう一度)

#===43.
from tkinter import filedialog

file_from=filedialog.askopenfilename()
print(file_from)


# shutil.copyfile(file_from,file_to)
# print("File Form:",file_from, file_to)
# print("File_To:", file_to)


"""
