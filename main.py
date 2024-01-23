import threading
import tkinter as my_tk
from datetime import time
from tkinter.font import Font
from tkinter import filedialog, W, END
import queue
import reptile
import datetime
import time

result_queue = queue.Queue()
main_window = my_tk.Tk()
# 实例化TK
main_window.title('Live Analysis')
# main_window.geometry('400x600+100+200')
sw = main_window.winfo_screenwidth()
# 得到屏幕宽度
sh = main_window.winfo_screenheight()
# 得到屏幕高度
ww = 800
wh = 600
x = (sw - ww) / 2
y = (sh - wh) / 2
main_window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
main_window.resizable(width=False, height=False)
l_font = Font(family="Arial", size=18, weight="bold")
l_font_1 = Font(family="Arial", size=12)
label_M = my_tk.Label(text="DY Live Analysis!", font=l_font)
label_M.pack()
label_live = my_tk.Label(text="直播间实时数据分析：", font=l_font_1)
label_live.place(x=10, y=30, width=165, height=30)
label_local = my_tk.Label(text="本地文件读取分析：", font=l_font_1)
label_local.place(x=410, y=30, width=150, height=30)
label_ln = my_tk.Label(text="直播间ID:", anchor="w", )
label_ln.place(x=10, y=60, width=60, height=30)
label_ln1 = my_tk.Label(text="监听时长:")
label_ln1.place(x=190, y=60, width=60, height=30)
label_ln2 = my_tk.Label(text="本地文件：")
label_ln2.place(x=410, y=60, width=60, height=30)
label_ln3 = my_tk.Label(text="直播间弹幕：", font=l_font_1)
label_ln3.place(x=10, y=100, width=100, height=30)
label_ln4 = my_tk.Label(text="高频词分析：", font=l_font_1)
label_ln4.place(x=410, y=100, width=100, height=30)
label_ln5 = my_tk.Label(text="情绪分析图：", font=l_font_1)
label_ln5.place(x=410, y=200, width=100, height=30)
label_ln6 = my_tk.Label(text="弹幕云图谱：", font=l_font_1)
label_ln6.place(x=410, y=400, width=100, height=30)
label_pr = my_tk.Label(text="Power By HongYu2024")
label_pr.place(x=640, y=570, width=150, height=30)
my_entry = my_tk.Entry(width=30)
my_entry.place(x=70, y=60, width=110, height=30)
my_entry1 = my_tk.Entry(width=30)
my_entry1.place(x=250, y=60, width=40, height=30)
my_text = my_tk.Text(width=50, height=30, undo=True, autoseparators=False)
my_text.insert(my_tk.END, '点击开始进行抓取')
my_text.place(x=10, y=130, width=380, height=440)
btn = my_tk.Button(main_window, text='Start', command=lambda: bt_start(my_entry.get()))
btn.place(x=300, y=60, width=40, height=30)
btn_stop = my_tk.Button(main_window, text='Stop', command=lambda: bt_start(my_entry.get()))
btn_stop.place(x=350, y=60, width=40, height=30)
btn_txt = my_tk.Button(main_window, text='Open', width=6,
                       command=lambda: browse_for_file(templ_entry, filetype_fasta))
btn_txt.place(x=700, y=60, width=40, height=30)
btn_start = my_tk.Button(main_window, text='start')
btn_start.place(x=750, y=60, width=40, height=30)
templ_filename = my_tk.StringVar()
templ_entry = my_tk.Entry(main_window, textvariable=templ_filename, width=30, justify="right")
templ_entry.xview_moveto(1)
templ_entry.place(x=470, y=60, width=220, height=30)
filetype_fasta = [('fasta files', '*.fasta'), ('All files', '*.*')]

def browse_for_file(entry_name, filetype):
    File_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    entry_name.delete(0, END)
    entry_name.insert(0, File_path)
    # 最关键的步骤就是使用xview_moveto(1) ，xview_moveto(0)表示显示左侧内容，xview_moveto(1)表示显示文本末尾内容
    # 特别需要注意的是，需要先插入内容，再使用xview_moveto。
    # 如果将entry_name.xview_moveto(1)  放在entry_name.insert(0, File_path)之前那么无法生效！
    entry_name.xview_moveto(1)


def open_txt(t_name):
    file1 = open(t_name, 'w', encoding='utf-8')
    file1.write('开始抓取请等待......')
    file1.close()
    while True:
        my_text.delete(1.0, "end")
        file = open(t_name, 'r', encoding='utf-8')
        r_txt = file.read()
        my_text.insert(my_tk.END, r_txt)
        file.close()
        my_text.see(my_tk.END)
        time.sleep(1)


def bt_start(lid):
    text_name = 'doc\\' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    t1 = threading.Thread(target=reptile.re_now, kwargs={'arg1': lid, 'arg2': text_name})
    t1.start()
    t2 = threading.Thread(target=open_txt, kwargs={'t_name': text_name})
    t2.start()


main_window.mainloop()

# 进入事件循环
