from tkinter import *
from tkinter import ttk
import pandas as pd


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

        message = StringVar()
        message.set("ボタンを選択してください")
        main_label = Label(frame1, textvariable=message, font=('Helvetica','9','bold'))
        main_label.pack()

        frame2_width = win_width
        frame2_height = int(win_height)-main_label_height
        frame2 = LabelFrame(self, text="", foreground="green", width=frame2_width, height=frame2_height)
        frame2.pack()
        frame2.propagate(False)

        for i in range(len(df)):
            button_text = df['NAME'][i]
            button = ttk.Button(frame2, text=button_text, command=self.selected_button(button_text,message))
            button.grid(column=0, row=0, sticky=(N, S, E, W))
            button_relheight = 1.0 / len(df)
            button_posY = frame2_height * button_relheight
            button.place(x=0 , y=i*button_posY, relwidth=1, relheight=button_relheight)

        self.pack()

    def selected_button(self, text, message):
        return lambda: message.set(text + " を選択しました")


""" MAIN """
# csvファイル読み込み
df = pd.read_csv('setting.csv', sep=',', quotechar='"', comment="#", encoding='cp932')
main_label_height = 30
button_height = 40
win_width = "170"
win_height = str((len(df) + 0) * button_height + main_label_height)

def main():
    root = Tk()
    root.title('gui_test')
    root.geometry(win_width + "x" + str(win_height))
    LoginApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()