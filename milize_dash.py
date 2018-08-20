# -*- coding: utf-8 -*-
"""
Created on Mon Aug  15 10:26:34 2018

@author: sxjin
"""

# import models****************************************
#generate UML command :pyreverse -o png -p Pyreverse milize_dash
#pyreverse -ASmy -k -o png milize_dash -p Main

import pandas as pd
import matplotlib.pyplot as plt



import os
#read with this module ,combine function of milize_htm_ani to class milize_dash or its subclass .
from types import MethodType
from sphinx.ext.autosummary import autosummary_table_visit_html

# import milize html binary module 
import milize_htm_ani as ani




#define the csv class***********************************
class milize_file(object):
    
    # args[0]  ,file format,type
    # args[1]  ,file path
    def __init__(self, fname,*args):
               
        self.fname        = fname#include the path,like c:/abc/abc.html
        self.fformat      = args[0]
        self.f_path       = args[1]
        # Add any envelop information below
        self.author       ="sxjin@milize.co.jp"
        self.des          ="use for process milize ai dash;version = 001_00_00"
        
        #private info below
        self.__server_ip="192.168.1.6"

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
    
    #envolop all file readtolist function here
    def read_file_tolist(self):
        if self.f_path=="": return "Need file path "
        #if self.fformat=="":  return "not  file format type be found"
        
        #this value will be included in one filename dict
        '''
        png_f=[]
        txt_f=[]
        csv_f=[]
        '''
        #just read all files ,not distinguish which type what format.
        f_dict=[]
        #print ("class f_path:"+str(self.f_path))
        filenames=sorted((fn for fn in os.listdir(self.f_path) ))
    
        for filename in filenames:
            f_dict.append(self.f_path+filename)

        #print("filenames111: "+str(f_dict))
        return f_dict
    





#define the png class,subclass*************************
class milize_png(milize_file):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    





#define the png class,subclass*************************
class milize_html(milize_file):
    def __init__(self, dash_id,order_id,html_css):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
        
        self.fname        = ""#include the path,like c:/abc/abc.html
        self.dash_id      = dash_id
        self.html_top_1   = ""
        self.html_top_2   = ""
        self.html_bottom  = ""
        self.html_left    = ""
        self.html_right   = ""
        self.html_mid     = ""
        self.html_css     = html_css
    
        # Add any envelop information below
        self.author ="sxjin@milize.co.jp"
        self.des="use for process milize ai dash;version = 001_00_00"
        
        #private info below
        self.__server_ip="192.168.1.6"

    #construct html looking
    def construct_html(self):
        t_html=""
       
        t_html= self.html_css\
        +"<table>"\
        +"<tr>"\
        +self.html_top_1\
        +"</tr>"\
        +"<tr>"\
        +self.html_top_2\
        +"</tr>"\
        +"<td>"\
        +self.html_left\
        +"</td>"\
        +"<td>"\
        +self.html_mid\
        +"</td>"\
        +"<td>"\
        +self.html_right\
        +"</td>"\
        +"</tr>"\
        +"<tr>"\
        +self.html_bottom\
        +"</tr>"\
        +"</table>"
       
        return t_html






#define the txt class,subclass**************************
class milize_txt(milize_file):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值




#define the txt class,subclass**************************
class milize_csv(milize_file):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
        
        self.row_title=[]
        self.head=False #whether has a head of csv,related to title
        self.data_type=[]# future,if there is data process req
        self.row_len=0
        self.columns_len=0
        
        

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值




#***********************************
class milize_dash(object):
    
    #initialize 
    def __init__(self, name, dash_id,order_id):
        self.name = name
        self.dash_id = dash_id
        self.order_id = order_id
        # Add any envelop information below
        self.author ="sxjin@milize.co.jp"
        self.des="use for process milize ai dash;version = 001_00_00"
        
        #private info below
        self.__server_ip="192.168.1.6"
        
        #private function read private information
        def get_server(self):
            return self.__server_ip
    







#***********************************

class milize_dash_csv(milize_dash):
    
    def read_csv(self,csv_path,csv_name):
        out_csv=""
        return out_csv

    #Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    #用于对文件的读写进行限制
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
        
        
        
        
        
#define a class of png        
#***********************************

class milize_dash_png(milize_dash):
    
    def read_png(self,png_path,png_name):
        out_png=""
        return out_png
    
    
    

#define a class of text
#***********************************
class milize_dash_txt(milize_dash):
    
    def read_txt(self,txt_path,txt_name):
        out_txt=""
        return out_txt
    





#***********************************

#all_list is a [] ,contains all files name 
#readR, means how many rows you want read in a csv file ,readC is the column number.
def  combine_mfiles_gen(milize_html_1,all_file,readR,readC):
    
    #
    aaa=0
    tmpstr=""
    single_pngb64                      =""
    single_txt                         =""
    single_csv                         =""# a cycle of all_files   
    
    h1                                 =[]
    h2                                 =[]
    h3                                 =[]
    
    
    for fpng in range(0,len(all_file)):#read all
        if all_file[fpng].endswith('.png'):# match with .png
            h1.append(all_file[fpng])
            
            #read all png file and create animation gif for everyone
            single_pngb64           = ani.png_files_to_base64html(all_file[fpng])
            single_pngb64           = ani.env_png_binary(single_pngb64)
            
            #discard the extension of file
            tmpstr                  =all_file[fpng].strip('.png')
            #read txt, same name without ext, text files ,
            for ftxt in range(0,len(all_file)):#read all
                if all_file[ftxt].endswith('.txt'):# match with .txt
                    if (tmpstr==all_file[ftxt].strip('.txt')):
                        h2.append(all_file[ftxt])
                
                        single_txt      = ani.txt_extr_cntx(all_file[ftxt])
                    else:
                        pass
            #read all csv files ,       
            for fcsv in range(0,len(all_file)):#read all
                if all_file[fcsv].endswith('.csv'):# match with .csv
                    #need change 
                    if (tmpstr+"next"==all_file[fcsv].strip('.csv')):
                        h3.append(all_file[fcsv])
                        #csv header is false,csv want be read one time is readR
                        single_csv = ani.csv_read_ctx(all_file[fcsv],False,readR,readC)   
                    else:
                        pass 
            tmpstr                  =""
            
    
            
            single_row              = "<tr>"+"<td>"+single_txt+"</td>" +"<td>"+single_pngb64 +"</td>" +"<td>"+single_csv+"</td>"+"</tr>"
            
            #print("aaa:"+str(aaa)) 
            aaa=aaa+1
             
            milize_html_1.html_mid  =  milize_html_1.html_mid+single_row
            single_pngb64           =""
            single_txt              =""
            single_csv              =""
            
            
            
            ###########special pngs add together,show the pic here
            ###############
            
    
    
    #the three list can use for future
    #print("h1:"+str(h1))  
    #print("h2:"+str(h2))  
    #print("h3:"+str(h3))  




#***********************************


#***test EXAMPLES , you should do it in others module,not write here****************************




