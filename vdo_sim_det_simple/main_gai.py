# coding=utf-8
import sys
import photoCompare
import keyframe_extract
import photoCut
from PIL import Image
import os
import commands
from foreach_two_photo import foreach_two_photo
import re
#import matplotlib.pyplot as plt
from drawFigure import drawPhotoInFigure
import itertools
import numpy
import time
	
if __name__ == "__main__":
	
	same_num = 0 #相同的个数
        #videopath1 = './video/01.mp4'
	videopath1 = sys.argv[1]
        #videopath2 = './video/04.mp4'
	videopath2 = sys.argv[2]
	
	#dir1 = './extract_result1/'
	#dir2 = './extract_result2/'
	dir1 = './extract_result3/'
	dir2 = './extract_result4/'
	
	#for i in range()
	'''
	if (os.path.exists('./txt/64a.txt')):
        	os.remove('./txt/64a.txt')
        file_64a = open('./txt/64a.txt','a+')
	if (os.path.exists('./txt/64b.txt')):
        	os.remove('./txt/64b.txt')
        file_64b = open('./txt/64b.txt','a+')
	'''
	'''
	if (os.path.exists('./txt/81.txt')):
        	os.remove('./txt/81.txt')
        file_81 = open('./txt/81.txt','a+')
	if (os.path.exists('./txt/82.txt')):
        	os.remove('./txt/82.txt')
        file_82 = open('./txt/82.txt','a+')
	if (os.path.exists('./txt/83.txt')):
        	os.remove('./txt/83.txt')
        file_83 = open('./txt/83.txt','a+')
	if (os.path.exists('./txt/84.txt')):
        	os.remove('./txt/84.txt')
        file_84 = open('./txt/84.txt','a+')
	if (os.path.exists('./txt/85.txt')):
        	os.remove('./txt/85.txt')
        file_85 = open('./txt/85.txt','a+')
	if (os.path.exists('./txt/86.txt')):
        	os.remove('./txt/86.txt')
        file_86 = open('./txt/86.txt','a+')
	if (os.path.exists('./txt/87.txt')):
        	os.remove('./txt/87.txt')
        file_87 = open('./txt/87.txt','a+')
	if (os.path.exists('./txt/88.txt')):
        	os.remove('./txt/88.txt')
        file_88 = open('./txt/88.txt','a+')
	group_txt = []# group_txt list
	'''
	'''
	for i in range(0,56):
		txt_name_str = './txt/' + str(i) + '.txt'
		if (os.path.exists(txt_name_str)):
        		os.remove(txt_name_str)
       		#group_txt.append(open(txt_name_str,'a+'))
	'''
	#photoCompareFlag = 0
	#audioCompareFlag = 0

	#'''
	print "图片对比部分开始..."
	#生成关键帧
	keyframe_extract.keyframe_extract(videopath1, dir1)
	keyframe_extract.keyframe_extract(videopath2, dir2)
	start_time = time.clock()
	'''
	#显示两段视频的关键帧
	plt.figure(1)
	plt.suptitle(videopath1+"'s KEYFRAMES")
	drawPhotoInFigure(dir1,4,9)
	plt.figure(2)
	plt.suptitle(videopath2+"'s KEYFRAMES")
	drawPhotoInFigure(dir2,4,9)#3,5
	plt.show() #显示figure,想要同时显示多个figure只能有一个show
	'''

        #遍历文件夹中的图片并进行对比
        photolist1 = os.listdir(dir1)
	photolist1.sort(key=lambda x: int(x.split('.')[0]))#按照文件夹中文件的排列顺序
        photolist2 = os.listdir(dir2)
	photolist2.sort(key=lambda x: int(x.split('.')[0]))#按照文件夹中文件的排列顺序
        #创建实例
        # dhash = photoCompare.DHash()
        #用帧少的去比较帧多的
	photoScore = 0
	
	if(len(photolist1)<len(photolist2)):
		temp = photolist1
		photolist1 = photolist2
		photolist2 = temp
		temp_dir = dir1
		dir1 = dir2
		dir2 = temp_dir
        if(1):
        #if(len(photolist1)<len(photolist2)):
	#if(len(photolist1)>len(photolist2)):
                #foreach_two_photo() 截取关键帧的中心100px图片
                ##获取相同数目的帧
		#all_group_num = []
		#all_num = numpy.zeros((56,len(photolist2)))
		#print all_num
		#img_num_index = 0
		count_num = 0
		b_list = []
		a_index = -1
		all_dis = []
		for img_a_str in photolist2:
			a_index += 1
			img_a = Image.open(os.path.join(dir2,img_a_str))
			#计算每一关键帧的指纹
			dhash_a = photoCompare.DHash.calculate_hash(img_a)
			
			b_index = -1
			temp_dis = []
			for img_b_str in photolist1:
				b_index += 1
				img_b = Image.open(os.path.join(dir1,img_b_str))
				dhash_b = photoCompare.DHash.calculate_hash(img_b)
				hamming_dis =photoCompare.DHash.hamming_distance(dhash_a,dhash_b)
				if hamming_dis <= 7:
					#if img_b_str not in b_list:
					temp_dis_temp = [a_index,b_index,hamming_dis]

					if temp_dis_temp not in temp_dis:
							# if temp_dis_temp != []:
						temp_dis.append(temp_dis_temp)

					b_list.append(img_b_str)
					#if hamming_dis <= 7:
					prt_str = dir2+":"+img_a_str+dir1+":"+img_b_str+"hamming:"+str(hamming_dis)
						#print prt_str
					count_num += 1
						#break
			all_dis.append(temp_dis)
		scoreLine = "score:"+str(count_num*100.0/len(photolist2))
		#print all_dis

		all_dis_clear = []
		a_arr = []
		b_arr = []
		for sim_list in all_dis:
			if len(sim_list) > 1:
				sim_list_np = numpy.array(sim_list)
				sim_list_np = sim_list_np[numpy.argsort(sim_list_np[:, 2])]
				for sim2_np in sim_list_np:
					if sim2_np[0] not in b_arr and sim2_np[1] not in a_arr:

							# print "11111111111111111"
						a_arr.append(sim2_np[1])
						b_arr.append(sim2_np[0])
						all_dis_clear.append(sim2_np)
						break
			elif len(sim_list) == 1:
				if sim_list[0][1] not in a_arr:
					a_arr.append(sim_list[0][1])
					b_arr.append(sim_list[0][0])
					all_dis_clear.append(sim_list[0])
		print len(all_dis_clear) * 100.0 / min(len(photolist1),len(photolist2))
		#print all_dis_clear
		#print len(photolist1)
		#print len(photolist2)
		for sim_list in all_dis_clear:
			print sim_list
		elapsed = (time.clock() - start_time)
		print("Time used:",elapsed)	
	
			
        else:
		'''
                same_num = foreach_two_photo(dir1,dir2,photolist1, photolist2);
		photolen = len(photolist1)
		photoScore = same_num * 100 / photolen
                if (same_num >= len(photolist1)/2):
                        #print "相似视频"
			#photoCompareFlag = 1
                else:
                        #print "非相似视频"
			#photoCompareFlag = 0
		'''
	#print "图像相似度为:(%d)" % photoScore
	'''
	print "音频对比部分开始..."
	#提取视频中的音频
	mp3Shell1 = "ffmpeg -i " + videopath1 + " -f mp3 -vn " + dir1 + "01.mp3 -loglevel quiet"
	os.system(mp3Shell1)
	mp3Shell2 = "ffmpeg -i " + videopath2 + " -f mp3 -vn " + dir2 + "02.mp3 -loglevel quiet"
	os.system(mp3Shell2)
	#比较音频
	audioCompareShell = "python AudioCompare-master/main.py -f " + dir1 + "01.mp3 -f" + dir2 + "02.mp3"
	#正则提取相似度
	(status, output) = commands.getstatusoutput(audioCompareShell)
	#print output
	if (output == "NO MATCH"):
		#audioCompareFlag = 0
		print "音频相似度为:(0)"
	else:
		#audioCompareFlag = 1
		similarScore = re.search(r"\(([0-9]*)\)",output)
		similarTime = re.search(r": ([0-9]+).0s",output)
		print "音频相似度为:" + similarScore.group() + "有" + similarTime.group(1) + "s相似"
		#print "非相似视频"
	'''



