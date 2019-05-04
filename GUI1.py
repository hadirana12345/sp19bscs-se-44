#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#GUI Libararys
#tkinter>buttons>show_text>

import tkinter
window = tkinter.Tk()
window.title("GUI")
label = tkinter.Label(window, text = "Hello World this is Abubakr\n"
                      "Hello World this is Abubakr Hello World this is Abubakr\n"
                      "Hello World this is Abubakr Hello World this is \n Abubakr").pack()
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="left")
btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack()
btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()
btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple", bg="Aqua").pack()

window.mainloop()

