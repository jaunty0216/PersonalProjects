def func1(length,thickness):
    shoulder = thickness*(2/3)
    MinTenonSet = thickness*1.5
    MaxTenonSet = thickness*2
    MinWidth = MinTenonSet - shoulder
    MaxWidth = MaxTenonSet - shoulder

    numerator = length-shoulder
    
    MaxAmountOfDovetail = numerator/MinTenonSet
    MinAmountOfDovetail = numerator/MaxTenonSet
    print(f"鳩尾榫的數量從",MinAmountOfDovetail,"到",MaxAmountOfDovetail)
    print(f"你可能也需要以下資訊:\n","根部間隙:",shoulder)
    print(f"根部寬度範圍",MinWidth,"到",MaxWidth)

def func2(length,thickness,DefaultDovetail):
    shoulder = thickness*(2/3)
    numerator = length-shoulder
    TenonSet = numerator/DefaultDovetail
    TenonWidth = TenonSet - shoulder

    print(f"鳩尾榫的根部寬度為",TenonWidth)
    print(f"你可能也需要以下資訊:\n","根部間隙:",shoulder)

length = float(input("那一邊有多長?"))
thickness = float(input("板子多厚?"))

SelectMode = int(input("計算尾榫數請按1，根據尾榫數回推根部寬度請按2"))

if(SelectMode == 1):
    func1(length,thickness)
elif(SelectMode == 2):
    DefaultDovetail = int(input("請問你鳩尾榫有多少個?"))
    func2(length,thickness,DefaultDovetail)
else:
    print("你一定是眼睛脫窗的啦。")