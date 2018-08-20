# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:26:34 2018

@author: sxjin
"""

# import models

from io import BytesIO
import base64

import imageio,os


from lxml import etree
#import webbrowser

#for csv reading 
import pandas as pd





#******temply*****************************
def ttest(in_val):
    print("the input value:"+str(in_val))
  
   
   
#***********************************




ainame="getAInameFromoutside"
passvalue=9999 #should get from outside,keep for future

#this name depend on caller, caller should know path and gif_name,all depend on caller,will not return .
#*******************html_gif_name="milizeAI.gif"
#******************CUR_PATH = r'c:/JINSHUXIN/Milize_AI/Milize_AI/templates/images/'

fileorder=1000000001




#***********************************
#clean the temp pic folder. If dont want others pics interfere with you , 
#you should clear the folder.
#DANGEROUS!!!!,make sure you want this action

def del_file(pth):
    
    ls = os.listdir(pth)
    for i in ls:
        c_path = os.path.join(pth, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)



#***************************************
#DANGEROUS!!!!,make sure you want this action
def del_spec_file(flist):
    
    countd=0
    if len(flist)<1: return -1
        
    for f in range(0,len(flist)):#read all
        if os.path.exists(flist[f]):
                os.remove(flist[f])
                countd=countd+1
        #the count be del of file        
        return countd
    

#***************************************
#DANGEROUS!!!!,make sure you want this action
#flist is a [] ,contains the file names,
def rmv_file_from_list(flist,rmv_fname):
    if len(flist)<1: return ""
    for f in range(0,len(flist)):#read all
        if flist[f]==rmv_fname:# match with .png
            #print("move:"+flist[f],rmv_fname)
            del(flist[f])
            #print("what:"+str(flist))
            return flist
        
        else:
            pass
    


       

#******pgn buffer convert to base64 binary*****************
#*******************problem ,need debug********************
def png_buffer_to_base64html(fig,ainame, passvalue, *args):
    #begin
    #consider check security?

    pngbinary="" 
    #method 1, create html binary stream files.
    buffer = BytesIO()  #buffer 
    
    fig.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
     
     
     
    plot_data = buffer.getvalue()
    #imb = base64.b64encode(buffer.getvalue())  
    pngbinary = base64.encodebytes(plot_data).decode()
    buffer.close
    return pngbinary
    
    
    

#*********convert png files to base64 binary of html ********#  
def png_files_to_base64html(pngnam):

    pngbinary="" 

    #if a gif name exist
    if pngnam:
        with open(pngnam,"rb") as fpng:
        
            pngbinary= base64.encodebytes(fpng.read()).decode()
        #create base64 binary for gif picture
        return pngbinary

    #gif name not exist
    else:
        return ""
    
    
    

#*********read text ********************
def txt_extr_cntx(txtnam):
    txt_ctx="" 
    try:
        #if a txt name exist
        if txtnam:
            with open(txtnam,'r') as ftxt:
                txt_ctx =  ftxt.read()
                return txt_ctx
        #txt name not exist
        else:
            return ""
    except:
        return ""
#***********************************





#*********read csv ********************
def csv_read_ctx(csvnam,csv_header=False,N=0,M=0):
    if not csv_header:
        try:
            #if a csv name exist
            if csvnam:
                
                csv_data = pd.read_csv(csvnam,header=None)  # 
                #print("11csv_data.shape") 
                #print(csv_data.shape)  #
                if not N: N = 0
                
                csv_batch_data = csv_data.tail(N)  # 取后5条数据
                
                #print("csv_batch_data") 
                return  csv_batch_data.to_html()
                #print("22csv_batch_data.shape") 
                #print(csv_batch_data.shape)  # 
                #train_batch_data = csv_batch_data[list(range(N, M))]  # 
                #print("33train_batch_data") 
                #print(train_batch_data)       
               
      
            #csv name not exist
            else:
                return ""
        except:
            return ""
    
    else:
        pass#if you want extend csv header process ,coding here
    
    
    
#***********************************



#******pgn buffer convert to base64 binary**#
#consider args[0] as gif name
def gif_to_base64html(openpath, gifnam):
    gifbinary =""
     #if no path para be got
    if not (openpath.strip()): return ""
    #if a gif name exist
    if gifnam:
        with open(openpath + gifnam,"rb") as fgif:
            # 
            gifbinary= base64.encodebytes(fgif.read()).decode()
        #create base64 binary for gif picture
        return gifbinary
   
        
    #gif name not exist
    else:
        return ""
#*******************************************# 



    
    
    

#************Abstract save png**********#
## *args type (), **kw type {}
#figure,fig
#plot ,plt
#passvalue ,y_test, test Dataset
#args0 and 1 is the figsize para,
#args2 is Epoch , str(ee)
#args3 is Batch ,str(ii))
def save_to_png(fig,plt,datatest,fileorder,save_path,*args,**kw):
    #begin
    #use this buffer to store series legends,if more than 1.
    #for common pic
   
  
    #optimize the chart
    #fig.set_dpi(100)
    #args to int

    
    list1 = [int(x) for x in args]
 
    
    if (list1[0] and list1[1]):
        fig = plt.figure(figsize=(list1[0],list1[1]))
    else:
        #if this para not be got
        fig = plt.figure(figsize=(10,7.6))
        
    #clear the history mark???
    #plt.xticks([])  #去掉横坐标值
    #plt.yticks([])  #去掉纵坐标值
    plt.xlabel('Time')
    plt.ylabel('Value')
    
    #plt.xticks(0, [1970,1980,1990,2000,2010,2020,2030])
    #ax1.set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000])
    #ax1.set_xticks([1970,1980,1990,2000,2010,2020,2030])
    #ax1.xaxis_date()
    #plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
    #plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
    
    
    ax1 = fig.add_subplot(111)
    
    #ax1.xaxis.grid(True, which='minor') #x坐标轴的网格使用主刻度
    #ax1.yaxis.grid(True, which='major') #y坐标轴的网格使用次刻度
    
    #test dataset
    ax1.plot(datatest)
   
    
    #title of chart,ee jis epoch number, ii is batch number
    
    ee=list1[2]
   
    ii=list1[3]
   
    #list1 = map(lambda xx:type(xx)==int, args)
    #print("list you:"+ str(ee)+str(ii))
    plt.title('Epoch ' + str(ee) + ', Batch ' + str(ii))
    #print("list you:"+ str(ii)  +"title :"+'Epoch ' + str(ee) + ', Batch ' + str(ii))
    #pause for view
    plt.pause(0.01)
    
    

    
    preimg='epoch_' + str(fileorder)+'.png'
    
    fig.savefig(save_path+preimg, format='png')  
    #print("save_path+preimg:"+ save_path+preimg)
    
    #release
    save_path=""
    
    #args,kw=None
    
    #end of save to png, png folder still caller give the CUR_PATH
    
#***************************************#

    
    #release plt
    plt.close()
    
    
    
    
#******   create gif format pic  *******# 
def folder_create_gif(png_path,gif_path,gif_name):
    # *****  Method 2 
    images    = []   
    #print("999: "+png_path+"::"+gif_name+"::"+gif_path)
    filenames=sorted((fn for fn in os.listdir(png_path) if fn.endswith('.png')))

    for filename in filenames:
        images.append(imageio.imread(png_path+filename))
        
        
    if folder_exist(gif_path):     
       imageio.mimsave(gif_path.strip()+gif_name.strip(), images,duration=1)
       return True
    else:
       return False
    


    
    #end , return a gif folder+name    
#***************************************


'''  
def folder_exist(folder_path):
    file_dir = os.path.split(folder_path)[0]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        return True
    else:
        return False
    
'''
def folder_exist(folder_path):
    #print("folder_path is :"+folder_path)
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        
            return True
        except:
            return False
        
    else:
        return True
  




#***************read all pngs together in this time FROM FOLDER
#***************convert to binary together 
def folder_pngs_to_binary64(CUR_PATH1):
    
    iris_im=""
    
    iris_im = iris_im+"""<tr>"""
    ims=""
    tcount=0
    
    #read all png files in the special folder
    
    filenames1=sorted((fn1 for fn1 in os.listdir(CUR_PATH1) if fn1.endswith('.png')))
    #must sort the name,otherwise ,gif not in order 
    for filename1 in filenames1:  
        ims=png_files_to_base64html(CUR_PATH1+filename1)
    
        #ims= png_buffer_to_base64html(fig,ainame, passvalue)
        ims = "data:image/png;base64,"+ims
        #iris_im = iris_im+"""<td><h3> AI Predict Step: """ +'Epoch ' + str(e) + ', Batch ' + str(i)+ """</h3> <img src="%s">""" % ims + """<br></td>"""
        iris_im = iris_im+"""<td><h3> >>> """ +str(tcount)+ """>>></h3> <img src="%s">""" % ims + """<br></td>"""
        tcount=tcount+1
        if ((tcount% 3)==0):
            iris_im = iris_im +"""</tr><tr>"""
        else:
            pass
        ims=""
    iris_im = iris_im +"""</tr>"""
    
    return iris_im
#**************************************************



#***************convert to binary together  FROM file list
def flist_pngs_to_binary64(f_list):
    
    iris_im=""
    

#**************************************************





#*************define read file
def readSpecFileInFolder(f_path,spec_name):
    file_list = []   
    #print("fpath:"+f_path +" spec name:"+spec_name)
    #read all special format files in the special folder,only ONE level folder.
    filenames=sorted((fn for fn in os.listdir(f_path) if fn.endswith(spec_name))) #spec_name like '.png'
    
    for filename in filenames:
        #print(filename)
        file_list.append(f_path+filename)
    
    return file_list
    #return a gif folder+name    
#***************************************






#*************define creat html with gif file
# f_name: c:/abc/abc.gif
def env_gif_binary(f_path,f_name,html_head):
    
    base64_gif          =""
    CUR_PATH            =""
    html_gif_name       =""
    
    if f_name == None and f_path ==None : return ""

    CUR_PATH            =f_path
    html_gif_name       =f_name
    #print("fpath is s%,fname is s%",f_path,f_name)
    base64_gif = "data:image/gif;base64,"+ gif_to_base64html(CUR_PATH, html_gif_name)
    base64_gif =  """<br><img src="%s">""" % base64_gif + """<br>"""
    
    base64_gif = "<br><h2> Milize Similar Stock Trend Animation </h2><br>"+html_head+base64_gif  +"<br>"
    

    return base64_gif

#***********************************


#*************define creat html with gif file
# f_name: c:/abc/abc.gif
def env_png_binary(base64png):
    
    env_base64png = "data:image/png;base64,"+base64png

    env_base64png = """<br> <img src="%s">""" % env_base64png + """<br>"""
    return env_base64png


#**************************************************



#*************define creat html with gif file
# html_name  example : c:/abc/abc.html
def wopen_to_html_f(contxtf,html_name):
    if not html_name: return ""
    # lxml lib etree convert the info to html soure code ,and write it to file
    html = etree.HTML(contxtf)
    tree = etree.ElementTree(html)
    tree.write(html_name)
    # open html file with explorer,PATH info get from common file later,test now
    #test open ,not 
    #webbrowser.open(html_name,new = 0.3)
    contxtf=""

    return html_name

    
#***********************************


#***********************************


#***********************************














