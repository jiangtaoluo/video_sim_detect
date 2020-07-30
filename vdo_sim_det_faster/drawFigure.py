# coding=utf-8
from PIL import Image
import os
#import matplotlib.pyplot as plt

#figureNum = 1

def drawPhotoInFigure(dirpath,i,j):
	index = 1
	dirpathList = os.listdir(dirpath)
	dirpathList.sort(key= lambda x:int(x[:-4]))
	for filename in dirpathList:
		#print filename
		pathname = os.path.join(dirpath,filename)
		if (filename!=''):
			#print filename
			img = Image.open(dirpath + filename)
			#print img
			#subImg = plt.subplot(i,j,index) #(i,j,index) 行,列,索引 需要改进
			#subImg.set_title('%s' % filename,fontsize=6)
			index += 1
			#print i
			#plt.imshow(img)
			#plt.axis('off') #关闭坐标

       	#plt.show()
