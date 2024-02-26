def on_button_click():
    label_text.set("Hello, this is a simple GUI app!")
 
# إنشاء نافذة
root = tk.Tk()
root.title("Simple GUI App")
 
# إنشاء مربع نص
label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text)
label.pack()
 
# إنشاء زر
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()
 
# تشغيل النافذة
root.mainloop()