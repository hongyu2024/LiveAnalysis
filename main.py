import threading
import tkinter as my_tk
from datetime import time
from tkinter.font import Font
from tkinter import filedialog, W, END
import queue
import datetime
import time
from matplotlib import pyplot as plt
from matplotlib import font_manager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
plt.rcParams['font.sans-serif']=['kaiti']

import reptile
import analysis

event = threading.Event()
event1 = threading.Event()
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
label_ln4 = my_tk.Label(text="高频词(Top15)：", font=l_font_1)
label_ln4.place(x=10, y=330, width=130, height=30)
label_ln5 = my_tk.Label(text="情绪分析：", font=l_font_1)
label_ln5.place(x=410, y=260, width=100, height=30)
label_ln6 = my_tk.Label(text="弹幕云图：", font=l_font_1)
label_ln6.place(x=410, y=100, width=100, height=30)
label_pr = my_tk.Label(text="Power By HongYu2024")
label_pr.place(x=640, y=570, width=150, height=30)
my_entry = my_tk.Entry(width=30)
my_entry.insert(my_tk.END, '567789235524')
my_entry.place(x=70, y=60, width=110, height=30)
my_entry1 = my_tk.Entry(width=30)
my_entry1.insert(my_tk.END, 60)
my_entry1.place(x=250, y=60, width=40, height=30)
my_text = my_tk.Text(width=50, height=30, undo=True, autoseparators=False)
#my_text.insert(my_tk.END, '点击开始进行抓取')
file = open('read.txt', 'r', encoding='utf-8')
rd_txt = file.read()
my_text.insert(my_tk.END, rd_txt)
file.close()
my_text.place(x=10, y=130, width=380, height=190)
btn = my_tk.Button(main_window, text='Start', command=lambda: bt_start(my_entry.get(), my_entry1.get()))
btn.place(x=300, y=60, width=40, height=30)
btn_stop = my_tk.Button(main_window, text='Stop', command=lambda: stop_thread())
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
    entry_name.xview_moveto(1)


def stop_thread():
    btn_stop.config(state='disabled')
    btn.config(state='active')
    for t in threading.enumerate():
        if t.name == "t1":
            event1.clear()
            print("stopThread......1")
            break
    for t in threading.enumerate():
        if t.name == "t2":
            event.clear()
            print("stopThread......2")
            break



def open_txt(t_name,event):
    file1 = open(t_name, 'w', encoding='utf-8')
    file1.write('正在打开Chrome浏览器抓取弹幕......\n初次打开过程可能较慢，请稍侯。\n使用过程中请勿关闭软件打开的直播界面!')
    file1.close()
    while event.is_set():
        my_text.delete(1.0, "end")
        file = open(t_name, 'r', encoding='utf-8')
        r_txt = file.read()
        my_text.insert(my_tk.END, r_txt)
        file.close()
        my_text.see(my_tk.END)
        analysis.do_analysis(t_name)
        try:
            # 打开文本文件并逐行读取
            with open('key_word.txt', 'r', ) as file:
                lines_word = []  # 创建一个空列表用于保存每行内容
                for line in file:
                    lines_word.append(line)  # 将每行添加到列表中
        except FileNotFoundError:
            print("文件未找到！")
        try:
            # 打开文本文件并逐行读取
            with open('key_val.txt', 'r') as file:
                lines_val = []  # 创建一个空列表用于保存每行内容
                for line in file:
                    number = float(line.strip())
                    lines_val.append(number)  # 将每行添加到列表中
        except FileNotFoundError:
            print("文件未找到！")
        # 创建画布和子图对象
        fig = Figure(figsize=(78, 10), dpi=100)
        #ax.set_facecolor('blue')
        # 绘制柱状图
        canvas = FigureCanvasTkAgg(fig, master=main_window)
        ax = fig.add_subplot(1,1,1)
        bars = ax.bar(lines_word, lines_val)
        canvas.get_tk_widget().place(x=10, y=365, width=780, height=205)
        canvas.draw()
        time.sleep(3)


def bt_start(lid,ltime):
    btn.config(state='disabled')
    btn_stop.config(state='active')
    text_name = 'doc\\' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    event1.set()
    print(event1)
    t1 = threading.Thread(target=reptile.re_now, kwargs={'arg1': lid, 'arg2': text_name, 'arg3': ltime,'event1':event1},name='t1')
    t1.start()
   # t1.join(timeout=3)

    event.set()
    print(event)
    t2 = threading.Thread(target=open_txt, kwargs={'t_name': text_name,'event':event},name='t2')
    t2.start()


main_window.mainloop()

# 进入事件循环
