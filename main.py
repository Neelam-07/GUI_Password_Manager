from tkinter import *
from tkinter import messagebox  
import random
import pyperclip
import json

# -------------------- -------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_lis= [random.choice(letters) for _ in range(nr_letters)]
    symbol_lis= [random.choice(symbols) for _ in range(nr_symbols)]
    number_lis= [random.choice(numbers) for _ in range(nr_numbers)]

    password_list= letter_lis + symbol_lis + number_lis
    random.shuffle(password_list)

    password= "".join(password_list)
    password_box.insert(0, password)  # to insert this generated password into the password box
    pyperclip.copy(password)    #to copy password


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email= email_username_box.get()    #to use the previous enteries use get()
    password =password_box.get()
    website= website_entry_box.get()
    my_json_data= {website: {
        "emali": email,
        "password": password
        }
    }

    #to check if the user has filled all blanks ::
    if len(email)==0 or len(password)==0 or len(website) == "0":
        messagebox.showinfo("Oops", "You have left blank empty")

    else:
        is_ok= messagebox.askokcancel(title=website, message=f"Please check the details:\nemail: {email}\n password: {password}")
        if is_ok:
            # using json data frame to store data instead of txt file
            #reading old data:
            try:
                with open("./Day_30/data.json","r") as password_file:
                    data= json.load(password_file)
                
            except FileNotFoundError:
                with open("./Day_30/data.json","a") as password_file:
                    json.dump(my_json_data, password_file, indent=4 )
                     
            #saving updated data:
            else:
                #updating old data:
                data.update(my_json_data)
                with open("./Day_30/data.json","a") as password_file:
                    json.dump(my_json_data, password_file, indent=4 )
                    
            finally:
                website_entry_box.delete(0, END)   #to dlt whatevr u typed in entry box,, (0, end) > index
                password_box.delete(0, END)        #once the file is create evrything will be deleted from window

def search():
    website= website_entry_box.get()
    with open("./Day_30/data.json","r") as password_file:
        data= json.load(password_file)
        if website in data:
            email= data[website]["email"]
            password= data[website]["password"]
            messagebox.showinfo(title= website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title= "error", message=f"The website {website} doesnt exist")


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password generator") 
window.config(padx=10, pady=10)

# canvas 
canvas= Canvas(height=200, width=200)    #bd = border of the canvas window.
photo= PhotoImage(file="/Neelam Rawat/python/Day_29_password_gen_GUI/logo.png")
canvas.create_image(100, 100, image= photo)   #(200, 200 are x & y pos of image on canvas)
canvas.grid(row=0, column=1)

#labels
website_label= Label(text="Website:")
website_label.grid(row= 1,column=0 )

email_username_label= Label(text="Email/Username:")
email_username_label.grid(row=2, column=0 )

password_label= Label(text="Password:")
password_label.grid(row= 3, column=0)

#entries

website_entry_box= Entry(width=30)
website_entry_box.grid(row=1, column=1)

email_username_box=Entry(width=30)
email_username_box.grid(row=2,column=1, columnspan=1)
email_username_box.insert(0, "" )   # 0 = index, where will be inserted

password_box=Entry(width=30)
password_box.grid(row=3,column=1, columnspan=1)

# #Button

password_button=Button(text="Generate password", command=password_gen)
password_button.grid(row=3,column=2, columnspan=2, padx=1, pady=1)

add_button=Button(text="Add",width=30, command= save )
add_button.grid(row=4, column=1, padx=1, pady=1)

search_button= Button(text= "Search", command= search)
search_button.grid(row=1, column=2, padx=1, pady=1)

window.mainloop()
