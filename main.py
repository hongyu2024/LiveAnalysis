import threading
import tkinter as my_tk
from tkinter.font import Font
import reptile

main_window = my_tk.Tk()
# 实例化TK
main_window.title('Live Analysis')
# main_window.geometry('400x600+100+200')
sw = main_window.winfo_screenwidth()
# 得到屏幕宽度
sh = main_window.winfo_screenheight()
# 得到屏幕高度
ww = 400
wh = 600
x = (sw - ww) / 2
y = (sh - wh) / 2
main_window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
main_window.resizable(width=False, height=False)
l_font=Font(family="Arial", size=18, weight="bold")
label_M = my_tk.Label(text="DY Live Analysis!",font=l_font )
label_M.pack()
label_ln = my_tk.Label(text="直播间ID:")
label_ln1 = my_tk.Label(text="监听时长:")
my_entry = my_tk.Entry(width=30)
my_entry1 = my_tk.Entry(width=30)
my_text = my_tk.Text(width=50, height=30, undo=True, autoseparators=False)
my_text.insert(my_tk.END,'oldval')
label_ln.place (x=20,y=40, width=60, height=30)
label_ln1.place (x=240,y=40, width=60, height=30)
my_text.pack(side='left')
my_entry.place (x=90,y=40, width=120, height=30)
my_entry1.place (x=310,y=40, width=40, height=30)
bt = my_tk.Button(main_window)
bt['text'] = 'start'
bt.pack()
def bt_click(e):
    liid=my_entry.get()
   # reptile.thread_1(e)
    reptile.thread_1(e)
def str_thr(e):
    threading_1 = threading.Thread(target=bt_click('553493414829'))
    threading_1.start()
bt.bind("<Button-1>",str_thr)
def thread_down(func):
    # 创建线程
    t = threading.Thread(target=func)
    # 启动
    t.start()
def wt():
    while True:
        time.sleep(1)
        print("1")
btn = my_tk.Button(main_window,text = '分析下载', command = lambda :thread_down(bt_click('334855313337')))
btn.pack()
main_window.mainloop()

# 进入事件循环