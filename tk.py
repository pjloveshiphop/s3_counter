from tkinter import *

root = Tk()
root.title('S3 File Counter')
root.geometry('{}x{}'.format(350, 350))

# create all of the main containers
#top_frame = Frame(root, bg='gray', width=350, height=175)
#bttom_frame = Frame(root, bg='white', width=350, height=175)

# layout all of the main containers
#root.grid_rowconfigure(1, weight=1)
#root.grid_columnconfigure(0, weight=1)

accesskey_txt = StringVar()
accesskey_lbl = Label(root, text='Access Key: ', font=('bold', 14), pady=10, padx=20)
accesskey_lbl.grid(row=0, column=0, sticky=W)
acceskey_etr = Entry(root, textvariable=accesskey_txt)
acceskey_etr.grid(row=0, column=1)

secretkey_txt = StringVar()
secretkey_lbl = Label(root, text='Secret Key: ', font=('bold', 14), pady=10,padx=20)
secretkey_lbl.grid(row=1, column=0, sticky=W)
secretkey_etr = Entry(root, textvariable=secretkey_txt, show='*', width=20)
secretkey_etr.grid(row=1, column=1)

endpointurl_txt = StringVar()
endpointurl_lbl = Label(root, text='Endpoint URL: ', font=('bold', 14), pady=10,padx=20)
endpointurl_lbl.grid(row=2, column=0, sticky=W)
endpointurl_etr = Entry(root, textvariable=endpointurl_txt)
endpointurl_etr.grid(row=2, column=1)

bucket_txt = StringVar()
bucket_lbl = Label(root, text='Bucket Name: ', font=('bold', 14), pady=10,padx=20)
bucket_lbl.grid(row=3, column=0, sticky=W)
bucket_etr = Entry(root, textvariable=bucket_txt)
bucket_etr.grid(row=3, column=1)

prefix_txt = StringVar()
prefix_lbl = Label(root, text='Prefix: ', font=('bold', 14), pady=10,padx=20)
prefix_lbl.grid(row=4, column=0, sticky=W)
prefix_etr = Entry(root, textvariable=prefix_txt)
prefix_etr.grid(row=4, column=1)


generate_report_btn = Button(text='Generate Report', width=25, pady=10, padx=10)
generate_report_btn.grid(row=5, column=0)

#generate_report_btn.place(relx=0.0, rely=0.0, anchor=S)


root.mainloop()