# coding=utf-8
import photoCompare
import keyframe_extract
import photoCut
from PIL import Image
import os
import reset_photo_size
#import matplotlib.pyplot as plt
from drawFigure import drawPhotoInFigure
import itertools

def foreach_two_photo(dir1,dir2,photolist1, photolist2):
    same_num = 0
    for i in range(0, len(photolist1)):
        img1 = os.path.join(dir1, photolist1[i])
        #首先将图片设置为图2一样大小
        # reset_photo_size.resize_image(img1)
        #只取中间的部分
        # photoCut.photo_cut(img1)
        image1 = Image.open(img1)
        if image1:
            for j in range(0, len(photolist2)):
                img2 = os.path.join(dir2, photolist2[j])
                # reset_photo_size.resize_image(img2)
                # photoCut.photo_cut(img2)
                image2 = Image.open(img2)
                if image2:
                    #用dhash的方法判断是否为相似图片
                    differ_num = photoCompare.DHash().hamming_distance(image1, image2)
                    if (differ_num < 10):
                        print 1-differ_num / 64.0
                        same_num += 1
			plt.figure(1)
			plt.suptitle("same KEYFRAMES in video1 and video2")
			#drawPhotoInFigure(img,4,9)
			subImg = plt.subplot(5,6,same_num*2-1) #(i,j,index) 行,列,索引 需要改进
			plt.imshow(image1)
			plt.axis('off') #关闭坐标
			subImg = plt.subplot(5,6,same_num*2) #(i,j,index) 行,列,索引 需要改进
			plt.imshow(image2)
			plt.axis('off') #关闭坐标
                        #print "%d" % (same_num) + ".相似的关键帧有img1:" + img1 + "和img2:" + img2 + " result:%d" % (
                            #photoCompare.DHash().hamming_distance(image1, image2))
                        #print "\n"
                        break
                #image2.close()
        #image1.close()
    plt.show()
    return same_num
