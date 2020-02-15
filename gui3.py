from tkinter import *
from tkinter import ttk
import pandas as pd
from selenium import webdriver
import time
import sys

# csvファイル読み込み
df = pd.read_csv('setting.csv', sep=',', quotechar='"', comment="#", encoding='cp932')
main_label_height = 30
button_height = 40
win_width = "170"
win_height = str((len(df) + 0) * button_height + main_label_height)


class LoginApp(ttk.Frame):
    """ログインアプリ"""
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        frame1_width = win_width
        frame1_height = main_label_height
        frame1 = LabelFrame(self, text="", foreground="green", width=frame1_width, height=frame1_height)
        frame1.pack()
        frame1.propagate(False)

        message = "ボタンを選択してください"
        self.main_label = Label(frame1, text=message, font=('Helvetica','9','bold'))
        self.main_label.pack()

        frame2_width = win_width
        frame2_height = int(win_height)-main_label_height
        frame2 = LabelFrame(self, text="", foreground="green", width=frame2_width, height=frame2_height)
        frame2.pack()
        frame2.propagate(False)
        
        for i in range(len(df)):
            button = ttk.Button(frame2, text=df['NAME'][i], command=lambda i=i:[self.update_label(df['NAME'][i]), self.browser_operation(df['NAME'][i])  ])
            button.grid(column=0, row=0, sticky=(N, S, E, W))
            button_relheight = 1.0 / len(df)
            button_posY = frame2_height * button_relheight
            button.place(x=0 , y=i*button_posY, relwidth=1, relheight=button_relheight)

        self.pack()

    def update_label(self, b_text):
        # 自身のメソッド名を取得
        print("[[ " + sys._getframe().f_code.co_name + " ]]")
        self.main_label["text"] = b_text + " を選択しました"
        print(b_text + " を選択しました")
    
    def browser_operation(self, b_text):
        print("[[ " + sys._getframe().f_code.co_name + " ]]")
        print("selected: " + b_text)
        for i in range(len(df)):
            if b_text == df['NAME'][i]:
                print(str(df['NAME'][i])+'、'+str(df['URL'][i])+'、'+ \
                    str(df['ID'][i])+'、'+str(df['ID_TYPE'][i])+'、'+ \
                    str(df['PW'][i])+'、'+str(df['PW_TYPE'][i])+'、'+ \
                    str(df['SUBMIT'][i])+'\n')

                NAME = str(df['NAME'][i])
                URL = str(df['URL'][i])
                ID = str(df['ID'][i])
                ID_TYPE = str(df['ID_TYPE'][i])
                PW = str(df['PW'][i])
                PW_TYPE = str(df['PW_TYPE'][i])
                SUBMIT = str(df['SUBMIT'][i])

        # ログイン処理
        # Chromeを起動
        driver = webdriver.Chrome('C:\drivers\chromedriver.exe')
        time.sleep(1)
        driver.refresh()

        #指定のURLにアクセス
        if not URL == '':
            driver.get(URL)
            # if NAME == "******":
            #     driver.find_element_by_name('param3').click()
            #     time.sleep(1)
            if not ID == '':
                id_type = driver.find_element_by_name(ID_TYPE)
                id_type.send_keys(ID)
            if not PW == '':
                pw_type = driver.find_element_by_name(PW_TYPE)
                pw_type.send_keys(PW)
            if not SUBMIT == '':
                pass
            
        else:
            print('ERROR:01')
            
def main():
    root = Tk()
    root.title('gui_test')
    root.geometry(win_width + "x" + str(win_height))
    LoginApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()