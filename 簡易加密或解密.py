destinationRoute = "C:\\Users\\jaunt\\Desktop\\"
announcement = "服務內容：\n解密：1\n加密：2\n同時：3\n"
userText = input('輸入文字：\n')
print(announcement)
modeSelection_1 = int(input('請選擇模式：'))


def takeOut(contend):
    modeSelection_2 = int(input("\n要幫你打包嗎？\n要：1\n不要：2\n"))
        
    if modeSelection_2 == 1:
        modeSelection_3 = int(input("\n自己取名嗎？(清一色幫你弄成txt檔)\n要：1\n不要：2\n"))
        if modeSelection_3 == 1:
            fileName = input("檔名：")+".txt"
        else:
            fileName = "Content.txt"
        
        with open(destinationRoute+fileName,'w') as file:
            file.write(contend)
            print("已匯出，小孩愛吃。")
    else:
        print("感謝使用")

def decode(userText):
    spiltter = input("分隔符號：")
    contend = userText.replace(spiltter," ")
    print("預覽：\n"+contend)
    takeOut(contend)
    return contend 

def encode(userText):
    spiltter = input("分隔符號：")
    contend = userText.replace(" ",spiltter)
    print("預覽：\n"+contend)
    takeOut(contend)
    return contend

def together(contend):
    oldSpiltter = input("分隔符號：")
    newSpiltter = input("分隔符號：")
    contend = userText.replace(oldSpiltter,newSpiltter)
    print("預覽：\n"+contend)
    takeOut(contend)
    return contend

if modeSelection_1 == 1:
    decode(userText)
elif modeSelection_1 == 2:
    encode(userText)
elif modeSelection_1 == 3:
    together(userText)
else:
    print("你眼瞎嗎？")