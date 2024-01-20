import tkinter as my_tk
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
label_M = my_tk.Label(text="DY Live Analysis!")
label_M.pack()
label_ln = my_tk.Label(text="直播间ID:")
label_ln.pack()
bt = my_tk.Button(main_window)
bt['text'] = '开始'
bt.pack()
main_window.mainloop()
# 进入事件循环