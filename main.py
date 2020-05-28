import os
import pandas as pd
import pathlib
import nltk
from datetime import datetime
from nltk.tokenize import word_tokenize
from tkinter import *
files = []
filename=[]
word=[]
frequency=[]
searches=[]
temp=[]
ovrvw=[]
ovrview=[]
dt=[]
pattern="hu"

def getAllindex(list, num):
    return filter(lambda a: list[a]==num, range(0,len(list)))


def killroot():
	global root
	root.destroy()

def savesearch():
    global searchh_entry,search,searches
    search=str(searchh_entry.get())
    if(" " in search):
        for i in range(len(search.split(" "))):
            temp.append(list(all_casings(search.split(" ")[i])))
        for i in (range(len(temp))):
            for j in temp[i]:
                searches.append(j)
    else:
        searches=list(all_casings(search))
    killroot()
def savefilepath():
    global directory_entry,path
    n=open("file_path_config_file.txt","w")
    n.write(str(directory_entry.get()))
    n.close()
    path=str(directory_entry.get())
    killroot()

    
    



def all_casings(input_string):
            if not input_string:
                yield ""
            else:
                first = input_string[:1]
                if first.lower() == first.upper():
                    for sub_casing in all_casings(input_string[1:]):
                        yield first + sub_casing
                else:
                    for sub_casing in all_casings(input_string[1:]):
                        yield first.lower() + sub_casing
                        yield first.upper() + sub_casing





print("\n\nMake Sure all the libraries are installed if not in cmd or Terminal write : pip install nltk pandas\n\n")



root=Tk()
root.title("Python Text Mining")
try:
    n=open("file_path_config_file.txt")
    path=str(n.read())
    n.close()
    killroot()
except:
	#nltk.download('punkt')
	label_for_directory=Label(text="Enter your folder Directory [One Time Only] (Example : C:\\Users\\User\\Desktop' ) : ")
	label_for_directory.pack()
	directory_entry=Entry(root)
	directory_entry.pack()
	butn=Button(text="Lets Go!",command=savefilepath)
	butn.pack()
    
    
    
    # path=input("Enter your folder Directory [One Time Only] (Example : C:\\Users\\User\\Desktop' ) : ")
    # n=open("file_path_config_file.txt","w")
    # n.write(path)
    # n.close()
    

root.mainloop()


root=Tk()
root.title("Python Text Mining")

label_for_searchh=Label(text="Enter the Topic you are Looking for ; Enter 0 for everything : ")
label_for_searchh.pack()

searchh_entry=Entry(root)
searchh_entry.pack()

searchh_button=Button(text="Lets Go!", command=savesearch)
searchh_button.pack()

root.mainloop()


# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
for ff in files:
    a=open(ff)
    a_=str(a.read())
    tokens = word_tokenize(a_)
    fdist = nltk.FreqDist(tokens)
    for f in fdist:
        freq=str(fdist[f])
        if(search=="0"):
            frequency.append(freq)
            filename.append(ff)
            word.append(f)
        

        elif(str(f) in searches):
            frequency.append(freq)
            filename.append(ff)
            word.append(f)
            # print(a_)
            # print(tokens)
            # print(list(getAllindex(tokens,search)))
            # print(tokens.index(str(search)))
            for i in (list(getAllindex(tokens,search))):
                if(i>=1 and len(tokens)>1):
                    # print(tokens[i-1:i+2])
                    ovrvw.append(tokens[i-1:i+2])
                
                else:
                    pass
            
            temps=ovrvw

            ovrvw=[]
            ovrview.append((str(temps)))
            print(frequency)
            
            
                # print(tokens[(tokens.index(str(search))-1):(tokens.index(str(search))+2)])



print(ovrview)

df = pd.DataFrame({"Filename":filename,"Word Frequency":frequency,"Word":word,"Short Overview":ovrview})
# print(df)
        
datetime_details=str(datetime.today())[-26:-16]+" "+str(datetime.today())[-16:-13]+"."+str(datetime.today())[-12:-10]+"."+str(datetime.today())[-9:]
    
name='Report _Automated '+datetime_details+".csv"
# df = pd.DataFrame(rows,columns)
df.to_csv(name)
root=Tk()
root.title("Success")

success_label=Label(text="Spreadsheet File Saved at : "+path+name)
success_label.pack()
buttn=Button(text="Done",command=killroot)
buttn.pack()
# input("Spreadsheet File Saved at : "+path+name)
root.mainloop()
#     except:
#         input("Check if the Directory is correct or not, if it is : then neccessary libraries not installed")

# except:
#     input("Neccessary modules are not installed")