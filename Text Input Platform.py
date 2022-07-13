from tkinter import *
import os.path

root = Tk()
root.geometry("500x250")
root.config(bg="#6D9886")
save_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

file_name = "data.txt"

completeData = os.path.join(save_path, file_name)


# Accept Text After Submit Button


def getvals():
    # This function is invoked when button `submit` is clicked
    with open(completeData, 'w') as file:
        file.write(namevalue.get()),
        file.write('\n'),
        file.write(surnamevalue.get()),
        file.write('\n'),
        file.write(phonevalue.get()),
        file.write('\n'),
        file.write(adressvalue.get()),
        file.write('\n'),
        file.write(emailvalue.get())
    print("Accepted")


# Heading
Label(root, text="Please Enter Your Information Bellow", font="ar 15 bold", bg="#6D9886", fg="white").grid(row=0,
                                                                                                           column=3)

# Field Name
name = Label(root, text="Name", bg="#6D9886", fg="white", font="ar 12 bold")
surname = Label(root, text="Surname", bg="#6D9886", fg="white", font="ar 12 bold")
phone = Label(root, text="Phone", bg="#6D9886", fg="white", font="ar 12 bold")
adress = Label(root, text="Adress", bg="#6D9886", fg="white", font="ar 12 bold")
email = Label(root, text="Email", bg="#6D9886", fg="white", font="ar 12 bold")

# Packing Fields
name.grid(row=1, column=2)
surname.grid(row=2, column=2)
phone.grid(row=3, column=2)
adress.grid(row=4, column=2)
email.grid(row=5, column=2)

# Variable for Storing data
namevalue = StringVar()
surnamevalue = StringVar()
phonevalue = StringVar()
adressvalue = StringVar()
emailvalue = StringVar()
checkvalue = IntVar()

# Creating Entry Field
nameentry = Entry(root, textvariable=namevalue, width=30, fg="black", bg="#CEE5D0", font="italic 12")
surnameentry = Entry(root, textvariable=surnamevalue, width=30, fg="black", bg="#CEE5D0", font="italic 12")
phoneentry = Entry(root, textvariable=phonevalue, width=30, fg="black", bg="#CEE5D0", font="italic 12")
adressentry = Entry(root, textvariable=adressvalue, width=30, fg="black", bg="#CEE5D0", font="italic 12")
emailentry = Entry(root, textvariable=emailvalue, width=30, fg="black", bg="#CEE5D0", font="italic 12")

# Packing Entry Fields
nameentry.grid(row=1, column=3)
surnameentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
adressentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)

# Creating CheckBox
checkbtn = Checkbutton(text="Remember Text?", variable=checkvalue, fg="white", bg="#6D9886", font="italic 10 bold")
checkbtn.grid(row=8, column=3)

# Submit Button
Button(root, text="Submit", bg="#6D9886", fg="white", command=getvals).grid(row=9, column=3)

root.mainloop()
