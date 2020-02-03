from tkinter import *
import pandas as pd
from selenium import webdriver
import time

global df
global root

# csvファイル読み込み
df = pd.read_csv('setting.csv', sep=',', quotechar='"', comment="#", encoding='cp932')

root = Tk()
root.title("Test Title")

main_label_height = 30
button_height = 40
win_width = "170"
win_height = str((len(df) + 0) * button_height + main_label_height)

# print("H:" + win_height + ", W:" + win_width)
# root.geometry("150x200")
root.geometry(win_width + "x" + win_height)

frame1_width = win_width
frame1_height = main_label_height

frame1=LabelFrame(root, text="", foreground="green", width=frame1_width, height=frame1_height)
frame1.pack()
# frame1.propagate(True)
frame1.propagate(False)

message = StringVar()
message.set("ボタンを選択してください")
# main_label = Label(frame1, textvariable=message)
main_label = Label(frame1, textvariable=message, font=('Helvetica','9','bold'))
main_label.pack()

def Update_Label(text):
    return lambda: message.set(text + " を選択しました")

# print("df_len:" + str(len(df)))

frame2_width = win_width
frame2_height = int(win_height)-main_label_height

frame2=LabelFrame(root, text="", foreground="green", width=frame2_width, height=frame2_height)
frame2.pack()
frame2.propagate(False)


for i in range(len(df)):
    button = Button(frame2, text=df['NAME'][i], command=Update_Label(df['NAME'][i]), bd=2)
    # <Button-1>:左クリック, <Button-2>:ホイールクリック, <Button-3>:右クリック
    # button.bind("<Button-1>", Label_Update(button))
    # button.pack()

    button_relheight = 1.0 / len(df)
    button_posY = frame2_height * button_relheight
    button.place(x=0 , y=i*button_posY, relwidth=1, relheight=button_relheight)

root.mainloop()
