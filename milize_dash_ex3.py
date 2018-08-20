# -*- coding: utf-8 -*-
"""
Created on Mon Aug  15 10:26:34 2018

@author: sxjin
"""

# import models****************************************

import milize_htm_ani as ani
import milize_dash as dash


def read_common_paras():
    print("all common paras should get from file or database")
    
def do_ai(in_val):    
    #***test EXAMPLES , you should do it in others module,not write here****************************
    
    print("low level,the input value:"+str(in_val))
    
    stockid=in_val
    
  
    
    
    #
    bart = dash.milize_dash_png('test_dash_name,', 99,999)
    
    #common paras should organized like this ,
    filestructure={'filepath':'C:/JINSHUXIN/milize_dash/output/','stockid':['1570'],'dateformat':'0000-00-00','main_file_format':'_stockid'}#read file as structure ,append later
    
    #used for dramaticly generate files,make files in order
    fileorder=11000000000 #this value will be read from a public file in future 
   
    #how many content you want read from a csv file,
    csv_def_type={'readR':'5','readC':'7'}#it should define in public files ,and this para get from such files
    
    #temp folder for dramatic html content ,used by current procedure
    
    tmp_path        = 'c:/JINSHUXIN/milize_dash/_tmp'
    html_gif_name   = 'stockid.gif' # a temp file name
    
    # common defination of output html name, 
    tmp_html_format ="__stockid.html"
    
    dash_list=[]#keep for future ,which kind of dash you want ? define a list include all type,like animation ,like mp4,
    
    
    #perhaps other app need a output file list, 
    out_file_list   ={}
    
    tmp_html_name   =""
    
    
    file_path       ='C:/JINSHUXIN/milize_dash/output/output/1570/2018-08-14/'
    #can cover all type,future will consider TXT 
    file_type1      =['.png','.txt','csv','']
    
    
    all_file        =[]
    
    milize_file1    =dash.milize_file("",file_type1[3],file_path)
    # Creat a object of milize_html,dash_id is 9999,no meaning now .
    milize_html_1   =dash.milize_html(9999,2200000,"")
    
    
    #tmp_html_format, chang to flex name when got the input stockid,here not include the PATH info,
    milize_html_1.fname   = "C:/JINSHUXIN/Milize_AI/Milize_AI/templates/"+"__"+stockid+".html"
    
    
    all_file        =milize_file1.read_file_tolist()
    #print("all files "+str(all_file))
          
    
      
    
    
    
    # a total gif be show in the top

                                     
    tmp_html                           = ani.folder_pngs_to_binary64(file_path)
    milize_html_1.html_top_1           = tmp_html 
    
    tmp_html                           =""
    
    
    
        
        
    
    
    
    ####Single process,          html page top with an animation gif
    
    ###you can add other content to html page header, if you like .Need change the example
    
    if ani.folder_create_gif(file_path,(tmp_path+'/1570/'),html_gif_name):
        print( 'ok')
    else:
        print("create gif fail ")
        #print("para �Cfilepath is s% ,tmp_path is s% :",file_path,tmp_path+'/1570/',html_gif_name)
        pass
    
    tmp_html=""
    
    append_top_show=""
    
    #show stock id and included
    
    if not (stockid.strip()==""):
        append_top_show                    ="<br>Below is delivered data :" +"<h2>ID: {{ stockid }}</h2>"\
                                            +"{% include \"included.html\" %}"\
                                            +"<a href=\"./\"> Main page .</a>"
    
    
    
    
    #siget base64 binary of gif for html,   
    tmp_html = ani.env_gif_binary(tmp_path+'/1570/',html_gif_name,"all Stocks Together")
    milize_html_1.html_top_1           =  tmp_html +append_top_show 
    append_top_show                    =""
     
     
    #before operation ,make sure you got the right stockname
    
    ###THIS FUNCTION USED Remove one file from list非常重要，目前是多此一举
    ####all_file = ani.rmv_file_from_list(all_file,file_path+'_'+stockid+'.png')
    
    dash.combine_mfiles_gen(milize_html_1,all_file,int(csv_def_type['readR'])  ,int(csv_def_type['readC']))
   
    #end of the cycle
    
    
    tmp_html = ""
    tmp_html = milize_html_1.construct_html()
    
    
    redirectp=""
    redirectp=ani.wopen_to_html_f(tmp_html , milize_html_1.fname)
    
    tmp_html = ""
    
    #del the temp gif file,not process the return value now .
    ani.del_spec_file(tmp_path+'/1570/'+html_gif_name)
    return redirectp
        

    #old method,future can reuse
    # milize_file1.readSpecFileInFolder     =  ani.readSpecFileInFolder # combine one method to class
    #abc= ani.readSpecFileInFolder(file_path.strip(),file_type1[0])

    



    
    
    
    #tmp_html = ""
    #get base64 binary of pngs for html
    #tmp_html = ani.folder_pngs_to_binary64(file_path)
    #milize_html_1.html_top_2 = tmp_html
    
   
    
    #***********************************
    
    
    # multiple implement
    ####class coins(milize_dash,milize_data,milize_cat):



 