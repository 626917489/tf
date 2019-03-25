import requests
import base64
import easygui as g
from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title('车牌识别系统')
cv= Canvas(root, width = 800, height =600, bg = "white")
cv.pack()
frame = Frame(root)
frame.pack()

def get_file_content(filePath):
    with open(filePath,"rb") as fp:
        return fp.read()

def img_show():
    global imgurl
    imgurl=g.fileopenbox('选择文件','提示','C:/Users/admin/Desktop/')
    image_file = Image.open(imgurl)
    im = image_file.resize((440,350),Image.BILINEAR)
    im = ImageTk.PhotoImage(im)
    image_label = Label(root,image = im)
    cv.create_window(40, 70, anchor=NW, window= image_label)
    root.mainloop()
def main():
    global imgurl
    host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AxzSTIGeXDSDDP2Wu5elaHnv&client_secret=gWKIBjBzSRDQOl4pyd6G33khnOamg1pV'
    headers = {
        'Content-Type':'application/json;charset=UTF-8'
    }
    res = requests.get(url=host,headers=headers).json()
    print(res['access_token'])
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate'
    data = {}
    data['access_token']=res['access_token']
    image = get_file_content(imgurl)
    data['image'] = base64.b64encode(image)
    headers={
    "Content-Type":"application/x-www-form-urlencoded",
    "apikey":"AxzSTIGeXDSDDP2Wu5elaHnv"
    }
    res = requests.post(url=url,headers=headers,data=data)
    result = res.json()
    print(result["words_result"]['number'])
    output_label = Label(root,text =result["words_result"]['number'],font =("仿宋", 14,"bold"))
    cv.create_window(640, 80, anchor=NW, window= output_label)
Button1 = Button(root, text="读取车牌",font =("仿宋", 14,"bold"),width=10,height=1,command = img_show)
cv.create_window(640, 240, anchor=NW, window=Button1)
Button2 = Button(root, text="识别车牌",font =("仿宋", 14,"bold"),width=10,height=1,command = main)
cv.create_window(640, 280, anchor=NW, window=Button2)
output_label2 = Label(root,text ="原车牌",font =("仿宋", 14,"bold"))
cv.create_window(40, 30, anchor=NW, window= output_label2)
output_label1 = Label(root,text ="车牌号码",font =("仿宋", 14,"bold"))
cv.create_window(640, 30, anchor=NW, window= output_label1)
root.mainloop()
