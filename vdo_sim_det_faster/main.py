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
    
    same_num = 0  # 相同的个数
    # videopath1 = './video/01.mp4'
    videopath1 = sys.argv[1]
    # videopath2 = './video/04.mp4'
    videopath2 = sys.argv[2]

    dir1 = './extract_result1/'
    dir2 = './extract_result2/'
    # dir1 = './extract_result3/'
    # dir2 = './extract_result4/'

    # for i in range()

    if (os.path.exists('./txt/64a.txt')):
        os.remove('./txt/64a.txt')
    file_64a = open('./txt/64a.txt', 'a+')
    if (os.path.exists('./txt/64b.txt')):
        os.remove('./txt/64b.txt')
    file_64b = open('./txt/64b.txt', 'a+')
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
    # photoCompareFlag = 0
    # audioCompareFlag = 0

    # '''
    print "图片对比部分开始..."
    # 生成关键帧
    keyframe_extract.keyframe_extract(videopath1, dir1)
    keyframe_extract.keyframe_extract(videopath2, dir2)
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

    # 遍历文件夹中的图片并进行对比
    start_time = time.clock()
    photolist1 = os.listdir(dir1)
    photolist1.sort(key=lambda x: int(x.split('.')[0]))  # 按照文件夹中文件的排列顺序
    photolist2 = os.listdir(dir2)
    photolist2.sort(key=lambda x: int(x.split('.')[0]))  # 按照文件夹中文件的排列顺序
    # 创建实例
    # dhash = photoCompare.DHash()
    # 用帧少的去比较帧多的
    photoScore = 0
    # '''
    if (len(photolist1) > len(photolist2)):
        temp = photolist1
        photolist1 = photolist2
        photolist2 = temp
        temp_dir = dir1
        dir1 = dir2
        dir2 = temp_dir
        print ("1")
    # '''
    if (1):
        # else:
        print ("2")
        # foreach_two_photo() 截取关键帧的中心100px图片
        ##获取相同数目的帧
        # all_group_num = []
        all_num = numpy.zeros((8, len(photolist2)))
        # all_num = numpy.zeros((56,len(photolist2)))
        print len(photolist2)
        img_num_index = 0
        for img_a_str in photolist2:

            img_a = Image.open(os.path.join(dir2, img_a_str))
            # 计算每一关键帧的指纹
            dhash_a = photoCompare.DHash.calculate_hash(img_a)
            dhash_str_a = dhash_a + '\n'
            # print isinstance(dhash_a,str)
            # 写入文件中
            file_64a.write(dhash_str_a)

            num_str = re.compile('.{2}').findall(dhash_a)  # 写出正则表达式 任意2个字符
            # print len(num_str)
            # print num_str
            groups = list(itertools.combinations(num_str, 1))  # 组合
            # groups = list(itertools.combinations(num_str, 3))#组合
            # print len(groups)
            # print 'hhh\n'
            group_num_index = 0
            group_num = dict()
            # group_num.append(1)
            for group_i_str in groups:  # 遍历每一个组
                # 计算video_a每一块的值且转换为十进制
                group_i_num = int(group_i_str[0], 16)  # 拿这个值与后面的值比较
                # print group_i_str
                # print 'hhh\n'
                # group_i_num = int(group_i_str[0]+group_i_str[1]+group_i_str[2],16)#拿这个值与后面的值比较
                # print group_i_num
                group_num[group_num_index] = group_i_num  # {group_num_index:number}
                all_num[group_num_index][img_num_index] = group_i_num
                group_num_index += 1
            img_num_index += 1
        file_64a.close()
        file_64a = open('./txt/64a.txt', 'a+')
        lines_a = file_64a.readlines()
        # print lines_a
        # 建立倒排索引

        invert_index = {}
        table_index = 0
        for table in all_num:
            a_table_diff_num = set(table)
            # for diff_num in table:#改
            for diff_num in a_table_diff_num:
                # print diff_num
                num_index = 0
                for num in table:
                    # if
                    temp = dict()
                    if diff_num == num:
                        num_list = []
                        num_list.append(table_index)
                        temp[num_index] = num_list
                        if invert_index.has_key(diff_num):
                            if invert_index[diff_num].has_key(num_index):
                                invert_index[diff_num][num_index].append(temp[num_index][0])
                            else:
                                invert_index[diff_num].update(temp)
                        else:
                            invert_index[diff_num] = temp
                    # temp.append(num_index)
                    # print 'hh'
                    num_index += 1
                    # print isinstance(invert_index[diff_num], list)
                # if invert_index.has_key(diff_num):
                #     if invert_index[diff_num].has_key(num_index):
                #         invert_index[diff_num][num_index].append(temp[num_index])
                #     invert_index[diff_num].update(temp)
                #
                #     #     invert_index[diff_num]
                # else:
                #     invert_index[diff_num] = temp

            # print "hhh"
            table_index += 1
        test = int("4c", 16)
	
        # for key,value in invert_index[test].items():
        # print key
        # print value
        # diff_num = set(all_num)#numbers in the set are all different

        # print diff_group_num
        # num = 0
        # print all_group_num
        all_num_b = numpy.zeros((8, len(photolist1)))
        # all_num_b = numpy.zeros((56,len(photolist1)))
        similar_dict = {'a': [], 'b': [], 'dis': []}
        sim_a_list = list()
        sim_b_list = list()
        sim_dis_list = list()
        img_num_index_b = 0
        count = 0
        all_dis = []

        for img_b_str in photolist1:
            img_b = Image.open(os.path.join(dir1, img_b_str))
            # 计算每一关键帧的指纹
            dhash_b = photoCompare.DHash.calculate_hash(img_b)
            dhash_str_b = dhash_b + '\n'
            # print isinstance(dhash_a,str)
            # 写入文件中
            file_64b.write(dhash_str_b)
            num_str_b = re.compile('.{2}').findall(dhash_b)  # 写出正则表达式 任意2个字符
            groups_b = list(itertools.combinations(num_str_b, 1))  # 组合
            # groups_b = list(itertools.combinations(num_str_b, 3))#组合
            # print groups_b
            group_num_index_b = 0
            group_num_b = dict()
            # group_num.append(1)
            key_list = list()
            # print dhash_b
            temp_dis = []
            for group_i_str_b in groups_b:  # 遍历每一个组
                # 计算video_a每一块的值且转换为十进制
                group_i_num_b = int(group_i_str_b[0], 16)  # 拿这个值与qian面的值比较
                # group_i_num_b = int(group_i_str_b[0]+group_i_str_b[1]+group_i_str_b[2],16)#拿这个值与qian面的值比较
                # print group_num_index_b
                if invert_index.has_key(group_i_num_b):

                    invert_list = invert_index[group_i_num_b]
                    for key, values in invert_list.items():
                        for value in values:
                            if value == group_num_index_b:
                                if 1:
                                    # print key

                                    dhash_a = lines_a[key]
                                    hamming_dis = photoCompare.DHash.hamming_distance(dhash_a, dhash_b)
                                    key_list.append(key)

                                    if hamming_dis <= 7:
                                        similar = "a:" + str(key) + "b:" + str(img_num_index_b) + "hamming_dis:" + str(
                                            hamming_dis)
                                        if key not in similar_dict['a']:
                                            similar_dict['a'].append(key)
                                            similar_dict['b'].append(img_num_index_b)
                                            similar_dict['dis'].append(hamming_dis)
                                            count += 1

                                        temp_dis_temp = [img_num_index_b, key, hamming_dis]

                                        if temp_dis_temp not in temp_dis:
                                            temp_dis.append(temp_dis_temp)

                group_num_index_b += 1
            # print count
            # print group_num_b
            img_num_index_b += 1
            all_dis.append(temp_dis)
        scoreLine = "score:" + str(round(count * 100 / len(photolist2)))
        all_dis_temp = numpy.array(all_dis)
        print all_dis
        print count * 100.0 / len(photolist2)
        print similar_dict
        for i in range(len(similar_dict['a'])):
            similar = "a:" + str(photolist2[similar_dict['a'][i]]) + "b:" + str(
                photolist1[similar_dict['b'][i]]) + "hamming_dis:" + str(similar_dict['dis'][i])
            print similar
        # print i
        # print  key_list

        # print len(set(all_dis_temp[:,0]))
        # 		# print len(set(all_dis_temp[:, 1]))
        # 	print  len(a_arr)
        a_arr = []
        b_arr = []
        # while [] in all_dis:
        # 	all_dis.remove([])
        # print all_dis

        all_dis_clear = []
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

        # for sim_list in all_dis:
        # 	# for sim2 in all_dis:
        # 	# # if sim_list[0] == 46:
        #
        # 	if len(sim_list) > 1:
        # 		sim_list_np = numpy.array(sim_list)
        # 		sim_list_np = sim_list_np[numpy.argsort(sim_list_np[:,2])]
        # 		for sim2_np in sim_list_np:
        # 			if sim2_np[0] not in b_arr and sim2_np[1] not in a_arr:
        #
        # 					# print "11111111111111111"
        # 				a_arr.append(sim2_np[1])
        # 				b_arr.append(sim2_np[0])
        # 			else:
        # 				sim_list.remove(list(sim2_np))
        # 				if len(sim_list) == 0:
        # 					all_dis.remove([])
        #
        # 	else:
        # 		# print sim_list
        #
        # 		if sim_list[0][1] not in a_arr:
        # 			a_arr.append(sim_list[0][1])
        # 			b_arr.append(sim_list[0][0])
        # 		else:
        # 			all_dis.remove(sim_list)
        # 			if len(sim_list) == 0:
        # 				all_dis.remove([])
        for sim_list in all_dis_clear:
            print sim_list
        # temp_arr = all_dis.index(sim[0])
        print len(all_dis_clear) * 100.0 / min(len(photolist1),len(photolist2))
        # print  temp_arr
        # all_dis_temp.in
        # if sim[0] ==

        # print  all_dis[:,0].index(sim[0])
        # else:
        # 	if sim[1] in all_dis_temp[:,1]:
        # 		# all_dis_temp.remove(sim)
        # 		print sim
        # 	else:
        # 		a =  1
        # print all_dis_temp[:,0]
        # if sim[0] in all_dis[:,0]:
        # 	print 1
        elapsed = (time.clock() - start_time)
        print("Time used:", elapsed)
        # for g in similar_list:

        # print len(group_num_b)
        '''
		print all_num_b #
		for b_num in all_num_b:
			print b_num
			invert_list = invert_index[b_num]
			for key,value in invert_list.items():
				print key
				print value
		'''

        '''
                if (same_num >= len(photolist2)/2):
                        #print "相似视频"
			#photoCompareFlag = 1
                else:
                        #print "非相似视频"
			#photoCompareFlag = 0
		'''

        # else:
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
    # print 'hhh'
    # print "图像相似度为:(%d)" % photoScore
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




