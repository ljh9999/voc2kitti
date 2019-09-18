#coding=utf-8
import cv2
import os
from xml.etree.ElementTree import ElementTree, Element
import difflib

outdir = './labels'

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


def read_xml(in_path):
    '''读取并解析xml文件
       in_path: xml路径
       return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")

def get_file_extension(filename):
    arr = os.path.splitext(filename)
    #return arr[len(arr) - 1]
    return arr[len(arr) - 1].replace(".","")


mkdir(outdir)

g = os.walk(r"./labels")
for path,dir_list,file_list in g:
    for file_name in file_list:
        if get_file_extension(file_name) == 'xml':
            label_name = file_name
            tree = read_xml(os.path.join(path, label_name))
            root = tree.getroot()
            for node in root:
                if node.tag == 'path':
                    #print(node.text)
                    #print(label_name)
                    #print(os.path.join('/home/nano/Documents/students/train/images',str(label_name[:6]+'.jpg')))
                    node.text = os.path.join('/home/nano/Documents/students/train/images',str(label_name[:6]+'.jpg'))

                    #if string_similar(label_name[:7], node.text[:7]) < 0.85:
                    #    print(label_name,end=' ')
                    #    print('have error')
            tree.write(os.path.join(outdir,label_name))
print('--- end of generating ---')


