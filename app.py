# starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title('GUI')

# create labels
name_label=ttk.Label(win,text="Enter Your Name:") 
name_label.grid(row=0,column=0,sticky=tk.W) # grid to give position of label# grid to give position of label

Email_label=ttk.Label(win,text="Enter your email:")
Email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter your age:")
age_label.grid(row=2,column=0,sticky=tk.W)

gender_lebel=ttk.Label(win,text="Select Your Gender:")
gender_lebel.grid(row=3,column=0,sticky=tk.W)

# create entry Box
name_var=tk.StringVar()    # for storing value in string format
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
Email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
Email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','other') # to choose value
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# radio button
usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text="Student",value="Student",variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
radiobtn2.grid(row=4,column=1)

# check button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text="check if you want see my account",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3,sticky=tk.W) # not to disturb other part

#create button,writing to files
# def action():
# 	user_name=name_var.get()
# 	user_email=email_var.get()
# 	userage=age_var.get()
# 	print(f"{user_name} is {userage} years old and email is {user_email}")
# 	gender_type=gender_var.get()
# 	user_type=usertype.get()
# 	if checkbtn_var.get()==0:
# 		subscribed="NO"
# 	else:
# 		subscribed="YES"
# 	print(gender_type,user_type,subscribed)
# 	# writing to file
# 	with open("GUI.txt",'a') as f:
# 		f.write(f"{user_name},{user_email},{userage},{gender_type},{user_type},{subscribed}\n")
# 		name_entrybox.delete(0,tk.END) # tk.END-->global varible to to clear entrybox
# 		Email_entrybox.delete(0,tk.END)
# 		age_entrybox.delete(0,tk.END)
# 		name_label.configure(foreground='#F23026')   # to change colur of label after clearing
# 		Email_label.configure(foreground='#F23026')  # foreground for text
# 		age_label.configure(foreground='#F23026')
# 		gender_lebel.configure(foreground='#F23026')
# 		submit_button.configure(foreground='#F23026')
#  writing to csv files
def action():
	user_name=name_var.get()
	user_email=email_var.get()
	userage=age_var.get()
	gender_type=gender_var.get()
	user_type=usertype.get()
	if checkbtn_var.get()==0:
		subscribed="NO"
	else:
		subscribed="YES"
	with open("GUI.csv","a",newline='') as f:
		dict_writer=DictWriter(f,fieldnames=['userName','userEmail','age','Gender','UserType','subscribed'])
		if os.stat('GUI.csv').st_size==0:
			dict_writer.writeheader()
		dict_writer.writerow({
			'userName':user_name,
			'userEmail':user_email,
			'age':userage,
			'Gender':gender_type,
			'UserType':user_type,
			'subscribed':subscribed
			})
submit_button=tk.Button(win,text="submit",command=action) # we can use ttk too
submit_button.grid(row=6,column=0)
win.mainloop()