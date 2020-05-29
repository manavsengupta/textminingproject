print("\n\nNote: Make Sure all the libraries are installed if not in cmd or Terminal write : pip install nltk pandas pdfminer and if nltk is not installed before then enter python in cmd or terminal and then enter import nltk and then enter nltk.download('punkt')\n\n .....Loading.......")
import os
import pandas as pd
import nltk
from datetime import datetime
from nltk.tokenize import word_tokenize
from tkinter import *

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
files = []
filename=[]
word=[]
frequency=[]
searches=[]
temp=[]
ovrvw=[]
ovrview=[]
dt=[]
pattern=[]
delta=[]
rep=1
for i in range(13):
    year=2000
    for j in range(22):
        if(i<10):

            pattern.append("/"+"0"+str(i)+"/"+str(year))
        else:
            pattern.append("/"+"0"+str(i)+"/"+str(year))
        year=2000
        year+=j
k=False





# This Function is provided by : "Zoum Datascience"   Video link : https://youtu.be/1TDS6-hYPDI ; Github link : https://github.com/zoumdatascience/Natural-Language-Processing/blob/master/getPDFContent.ipynb
def pdftotexts(filename):
    path_to_pdf=filename
    # Load your PDF
    

    '''
    path_to_pdf: is the parameter that will give access to the PDF File 
    we want to extract the content.
    '''
    
    '''
    PDFResourceManager is used to store shared resources such as fonts or images that 
    we might encounter in the files. 
    '''
    
    resource_manager = PDFResourceManager(caching=True)
    
    '''
    create a string object that will contain the final text the representation of the pdf. 
    '''
    out_text = StringIO()
    
    '''
    UTF-8 is one of the most commonly used encodings, and Python often defaults to using it.
    In our case, we are going to specify in order to avoid some encoding errors.
    '''
    codec = 'utf-8'
    
    """
    LAParams is the object containing the Layout parameters with a certain default value. 
    """
    laParams = LAParams()
    
    '''
    Create a TextConverter Object, taking :
    - ressource_manager,
    - out_text 
    - layout parameters.
    '''
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(path_to_pdf, 'rb')
    
    '''
    Create a PDF interpreter object taking: 
    - ressource_manager 
    - text_converter
    '''
    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    '''
    We are going to process the content of each page of the original PDF File
    '''
    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    '''
    Retrieve the entire contents of the “file” at any time 
    before the StringIO object’s close() method is called.
    '''
    text = out_text.getvalue()

    '''
    Closing all the ressources we previously opened
    '''
    fp.close()
    text_converter.close()
    out_text.close()


    with open(str(filename)[:-4]+"_text.txt", 'w') as f:
            f.write(text)
            f.close()
        
        # Save all text to a txt file.
        # with open(str(filename)[:-4]+"_text.txt", 'w') as f:
        #     f.write("\n\n".join(pdf))
        #     f.close()




def getAllindex(list, num):
    return filter(lambda a: list[a]==num, range(0,len(list)))


def killroot():
    global root
    root.destroy()

def savesearch():
    global searchh_entry,search,searches,temp
    search=str(searchh_entry.get())
    if(" " in search):
        for i in range(len(search.split(" "))):
            temp.append(list(all_casings(search.split(" ")[i])))
        for i in (range(len(temp))):
            for j in temp[i]:
                searches.append(j)
    else:
        searches=list(all_casings(search))
    temp=[]
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








root=Tk()
root.title("Python Text Mining")
try:
    n=open("file_path_config_file.txt")
    path=str(n.read())
    n.close()
    killroot()
except:
    #If nltk punkt is not downloaded then in cmd or terminal type nltk.download('punkt')
    label_for_directory=Label(text="Enter your folder Directory [One Time Only] (Example : C:\\Users\\User\\Desktop' ) : ")
    label_for_directory.pack()
    directory_entry=Entry(root)
    directory_entry.pack()
    butn=Button(text="Lets Go!",command=savefilepath)
    butn.pack()
    
    
    
    
    

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
        if '.pdf' in file:
            files.append(os.path.join(r, file))



for ff in files:
    pdftotexts(ff)

files=[]

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

            
            
            for i in (list(getAllindex(tokens,f))):

                if(i>=1 and len(tokens)>1):
                    ovrvw.append(tokens[i-1:i+3])
                elif(i>=2):
                    ovrvw.append(tokens[i-3:i+3])
                elif(i>=3):
                    ovrvw.append(tokens[i-3:i+3])
                
                else:
                    ovrvw.append(tokens[i:i+3])


            temps=ovrvw

            ovrvw=[]
            ovrview.append((str(temps)))

            for i in pattern:
                if(i in a_):
                    rep+=1
                if(i in a_ and rep<=2):
                    dt.append(str(i[1:]))
                    delta.append(int(str(datetime.today())[:-22])-(int(str(i)[-4:])))
                    k=True
                if(rep>2):
                    dt.pop(-1)
                    delta.pop(-1)
                    dt.append("Multiple Dates Detected")
                    delta.append("Cannot be Determined")
                    k=True
                    break
            rep=1

            

            if(k):
                k=False
            else:
                dt.append("Not Found")
                delta.append("Cannot be Determined")
                k=False

            
        

        elif(str(f) in searches):
            frequency.append(freq)
            filename.append(ff)
            word.append(f)
            for j in searches:
                for i in (list(getAllindex(tokens,j))):
                    if(i>=1 and len(tokens)>1):
                        # print(tokens[i-1:i+2])
                        ovrvw.append(tokens[i-1:i+3])
                    elif(i>=2):
                        ovrvw.append(tokens[i-3:i+3])
                    elif(i>=3):
                        ovrvw.append(tokens[i-3:i+3])
                    
                    else:
                        ovrvw.append(tokens[i:i+3])
            
            temps=ovrvw

            ovrvw=[]
            ovrview.append((str(temps)))

            
            for i in pattern:
                if(i in a_):
                    rep+=1
                    print(rep)
                if(i in a_ and rep<=2):
                    dt.append(str(i[1:]))
                    delta.append(int(str(datetime.today())[:-22])-(int(str(i)[-4:])))
                    k=True
                if(rep>=3):
                    dt.pop(-1)
                    delta.pop(-1)
                    dt.append("Multiple Dates Detected")
                    delta.append("Cannot be Determined")
                    k=True
                    break
            rep=1
                    
                

            if(k):
                k=False
            else:
                dt.append("Not Found")
                delta.append("Cannot be Determined")
                k=False

            


df = pd.DataFrame({"Filename":filename,"Word Frequency":frequency,"Word":word,"Date[MM/YYYY]":dt,"Years since Published":delta,"Short Nearby Words Overview":ovrview})
        
datetime_details=str(datetime.today())[-26:-16]+" "+str(datetime.today())[-16:-13]+"."+str(datetime.today())[-12:-10]+"."+str(datetime.today())[-9:]
    
name='Report _Automated '+datetime_details+".csv"
df.to_csv(name)
root=Tk()
root.title("Success")

success_label=Label(text="Spreadsheet File Saved at : "+path+name)
success_label.pack()
buttn=Button(text="Done",command=killroot)
buttn.pack()

root.mainloop()
