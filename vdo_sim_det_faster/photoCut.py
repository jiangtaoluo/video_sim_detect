# coding=utf-8
from PIL import Image

def photo_cut(img_dir):
    im = Image.open(img_dir)
    # 图片的宽度和高度
    img_size = im.size
    img_cut_px = 50
    # print("图片宽度和高度分别是{}".format(img_size))
    '''
    裁剪：传入一个元组作为参数
    元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
    '''
    # 截取图片中一块宽和高都是250的
    #圆心坐标
    o_x = img_size[0]/2
    o_y = img_size[1]/2
    #获取的宽度
    get_x = 500
    get_y = 300
    #开始的坐标
    start_x = o_x-get_x/2
    start_y = o_y-get_y/2
    region = im.crop((start_x, start_y, start_x+get_x, start_y+get_y))
    region.save(img_dir)