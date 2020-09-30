# coding:utf-8
import numpy as np
import urllib.request
from urllib.request import urlretrieve
import re
import datetime
from dateutil.relativedelta import relativedelta
import random
import cv2
import os,stat

#根据URL下载文件,并返回本地文件名
def request_download(imgurl):
#{
  #处理后图片文件位置
    return_ImageFileName = "images/";
    newWblogpath_ImagePaht = "NewWBlog/";
    
    imgfilename = str(random.randint(10000,99999));
    imgfilename += ".png";
    return_ImageFileName += imgfilename;
    imgfilename = newWblogpath_ImagePaht + return_ImageFileName;
   
    urlretrieve(imgurl, imgfilename);
    return return_ImageFileName;
    
#}
if __name__ == '__main__':
#{
   #处理后文件位置
   newWblogpath = "./NewWBlog/";
    #处理后图片文件位置
   newWblogpath_ImagePaht = "./NewWBlog/images/";
   #原来的文件名
   oldWblogFile = "./Backup_of_Tencent_Weibo.html";

   #判断要处理的文件是否存在
   if not os.path.exists(oldWblogFile):
       print("weiBlog file is not exiting,fail!");

   #文件大小
   fsize = 0;
   #创建文件夹
   if not os.path.exists(newWblogpath):
       os.makedirs(newWblogpath);
  #创建图片文件夹
   if not os.path.exists(newWblogpath_ImagePaht):
       os.makedirs(newWblogpath_ImagePaht);

   #获取文件大小   
   fsize = os.path.getsize(oldWblogFile);
   #打开并读取文件
   fblog = open(oldWblogFile,"r",encoding='utf8');
   strHtml = fblog.read(fsize);
   fblog.close();
   #正则表达式，要取出图片的URL
   imgurl   = r'<img src="(.+?)"';
   #编译一下
   reg_imgurl   = re.compile(imgurl);

   urlimgList   = reg_imgurl.findall(strHtml)#进行匹配

   for imgurl in urlimgList:
   #{
       try:
         #{           
            #下载图片，并得到地址
            newimageurl = request_download(imgurl);
            
       #}
       except IOError:
           print(imgurl + "没有下载成功，请手动替换");
       else:
           #替换掉哦图片地址
            strHtml =strHtml.replace(imgurl,newimageurl);
    #}
   newWblogfile = newWblogpath + "index.html";
   fblog = open(newWblogfile,"w",encoding='utf8');
   fblog.write(strHtml);
   fblog.close();
  
#}

  