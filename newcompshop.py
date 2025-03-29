import datetime
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
def disable_event():
    pass
main_window = Tk()
main_window.title('Computer Shop')
main_window.state('zoom')
main_window.minsize(1500, 700)

users = [{"usernamed": "admin", "passcode": "admin"}] # Dictionary to store the users and passwords
error_signup = False
# motherboards items
motherboard_items = []

# rams items
ram_items = []

# pcmonitor items
pc_monitor_items = []

# compcase items
pc_case_items = []

selected_items = []

def add_user(username, password):
    users.append({"usernamed": username, "passcode": password})

# image paths
image_paths = {
    "bg_image1": "C:/Users/mcyor/Documents/Mycodes/pythonProject/computersale/bg_image.png",
    "bg_image2": "C:/Users/mcyor/Documents/Mycodes/pythonProject/computersale/bg_image2.png",
}

# Load and resize the image
original_image = Image.open(image_paths["bg_image1"])
resized_image = original_image.resize((1600, 900))
bg_image1 = ImageTk.PhotoImage(resized_image)

original_image2 = Image.open(image_paths["bg_image2"])
resized_image2 = original_image2.resize((1600, 900))
bg_image2 = ImageTk.PhotoImage(resized_image2)

main_frame = Frame(main_window)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Set image as background
bg_label = Label(main_frame, image=bg_image1)
bg_label.place(x=0, y=0)

def bg_label_action(event):
    cart_list_frame.place_forget()
    purchase_table_frame.place_forget()
    selected_items_frame.place_forget()
    add_product_window.place_forget()
    delete_product_window.place_forget()

bg_label.bind("<Button-1>", bg_label_action)

add_product_window = Frame(main_frame, bg='#010e38', bd=2, relief="solid")
add_product_window.focus_set()
form_frame = Frame(add_product_window, padx=10, pady=10, bg='#41566b')
form_frame.place(x=0, y=0, relwidth=1, relheight=1)

Label(form_frame, text="Add New Product", font=("Arial", 16, "bold"), bg="#41566b", fg="white").place(relx=0.5, y=20, anchor="center")

Label(form_frame, text="ID:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
id_entry = Entry(form_frame, state="readonly", bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", font=("Arial", 12, "bold"))
id_entry.place(x=150, y=50, width=200, height=25)

Label(form_frame, text="Name:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
name_entry = Entry(form_frame, bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", font=("Arial", 12, "bold"))
name_entry.place(x=150, y=90, width=200, height=25)

Label(form_frame, text="Brand:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
brand_entry = Entry(form_frame, bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", font=("Arial", 12, "bold"))
brand_entry.place(x=150, y=130, width=200, height=25)

Label(form_frame, text="Stack:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
stack_entry = Entry(form_frame, bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", font=("Arial", 12, "bold"))
stack_entry.place(x=150, y=170, width=200, height=25)

Label(form_frame, text="Price:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=210)
price_entry = Entry(form_frame, bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", font=("Arial", 12, "bold"))
price_entry.place(x=150, y=210, width=200, height=25)

Label(form_frame, text="Image:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=290)
image_path_var = StringVar()
image_entry = Entry(form_frame, textvariable=image_path_var, state="readonly", bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", font=("Arial", 12, "bold"))
image_entry.place(x=150, y=290, width=200, height=25)

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        image_path_var.set(file_path)

browse_button = Button(form_frame, text="Browse", command=browse_image, bg="blue", fg="white", font=("Arial", 10, "bold"))
browse_button.place(x=360, y=290, width=80, height=25)

Label(form_frame, text="Type:", bg="#41566b", fg="white", font=("Arial", 12, "bold")).place(x=50, y=250)
type_var = StringVar(value="MotherBoard") # default value
type_option = ttk.Combobox(form_frame, textvariable=type_var, values=["MotherBoard", "Ram", "PC Monitor", "PC Case"], state="readonly")
type_option.place(x=150, y=250, width=200, height=25)

close_window = Label(form_frame, text="Close Window", font=("Arial", 12, "bold"), bg="#41566b", fg="white")
close_window.place(relx=0.5, y=410, anchor="center")

def close_window_enter(event):
    close_window.config(fg="#D4B0FF", cursor="hand2")
def close_window_leave(event):
    close_window.config(fg="white")
def close_window_action(event):
    open_close_add_product()
def type_option_action(event):
    print(f"Selected Type: {type_var.get()}")
    id_entry.config(state="normal")
    id_entry.delete(0, END)
    if type_var.get() == "MotherBoard":
        id_entry.insert(0, len(motherboard_items) + 1)
        id_entry.config(state="readonly")
    elif type_var.get() == "Ram":
        id_entry.insert(0, len(ram_items) + 1)
        id_entry.config(state="readonly")
    elif type_var.get() == "PC Monitor":
        id_entry.insert(0, len(pc_monitor_items) + 1)
        id_entry.config(state="readonly")
    elif type_var.get() == "PC Case":
        id_entry.insert(0, len(pc_case_items) + 1)
        id_entry.config(state="readonly")

close_window.bind("<Enter>", close_window_enter)
close_window.bind("<Leave>", close_window_leave)
close_window.bind("<Button-1>", close_window_action)
type_option.bind("<<ComboboxSelected>>", type_option_action)

id_entry.config(state="normal")
id_entry.delete(0, END)
if type_var.get() == "MotherBoard":
    id_entry.insert(0, len(motherboard_items) + 1)
    id_entry.config(state="readonly")

def done_action():
    if not name_entry.get() or not brand_entry.get() or not stack_entry.get() or not price_entry.get() or not image_path_var.get():
        messagebox.showerror("Error", "All fields are required.")
    elif not stack_entry.get().isdigit():
        messagebox.showerror("Error", "Stack must be a number.")
    else:
        try:
            price = float(price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number.")
            return

        new_item = {
            "id": int(id_entry.get()),
            "product": name_entry.get(),
            "brand": brand_entry.get(),
            "image": image_path_var.get(),
            "stack": stack_entry.get(),
            "quantity": "0",
            "price": f"${price:.2f}",
            "type": type_var.get()
        }

        if type_var.get() == "MotherBoard":
            motherboard_items.append(new_item)
            messagebox.showinfo("Success", "Product added successfully!")
        elif type_var.get() == "Ram":
            ram_items.append(new_item)
            messagebox.showinfo("Success", "Product added successfully!")
        elif type_var.get() == "PC Monitor":
            pc_monitor_items.append(new_item)
            messagebox.showinfo("Success", "Product added successfully!")
        elif type_var.get() == "PC Case":
            pc_case_items.append(new_item)
            messagebox.showinfo("Success", "Product added successfully!")
        
        # Reset all entry fields and combobox
        id_entry.config(state="normal")
        id_entry.delete(0, END)
        id_entry.config(state="readonly")
        name_entry.delete(0, END)
        brand_entry.delete(0, END)
        stack_entry.delete(0, END)
        price_entry.delete(0, END)
        image_path_var.set("")
        type_var.set("MotherBoard")

        # update cart items
        display_computercase_items()
        display_motherboards_items()
        display_pcmonitor_items()
        display_rams_items()

Button(add_product_window, text="Done", bg="green", fg="white", font=("Arial", 15, "bold"), command=done_action).place(relx=0.5, y=370, width=100, height=30, anchor="center")

def open_close_add_product():
    if add_product_window.winfo_ismapped():
        add_product_window.place_forget()
    else:
        add_product_window.place(relx=0.5, rely=0.6, anchor="center", width=500, height=450)
        selected_items_frame.place_forget()
        cart_list_frame.place_forget()
        delete_product_window.place_forget()
        display_computercase_items()
        display_motherboards_items()
        display_pcmonitor_items()
        display_rams_items()

delete_product_window = Frame(main_frame, bg='#41566b', bd=2, relief="solid")

def open_close_delete_product():
    if delete_product_window.winfo_ismapped():
        delete_product_window.place_forget()
    else:
        delete_product_window.place(relx=0.5, rely=0.6, anchor="center", width=500, height=450)
        add_product_window.place_forget()
        selected_items_frame.place_forget()
        cart_list_frame.place_forget()
        purchase_table_frame.place_forget()
        refresh_delete_list()

Label(delete_product_window, text="Delete Product", font=("Arial", 16, "bold"), bg="#016279", fg="white").place(relx=0.5, y=20, anchor="center")

Label(delete_product_window, text="Type:", bg="#016279", fg="white", font=("Arial", 12, "bold")).place(x=50, y=60)
delete_type_var = StringVar(value="MotherBoard")  # Default value
delete_type_option = ttk.Combobox(delete_product_window, textvariable=delete_type_var, values=["MotherBoard", "Ram", "PC Monitor", "PC Case"], state="readonly", font=("Arial", 12))
delete_type_option.place(x=150, y=60, width=200, height=25)

delete_list_frame = Frame(delete_product_window, bg="#00A6D0", bd=2, relief="solid")
delete_list_frame.place(x=50, y=100, width=400, height=250)

delete_canvas = Canvas(delete_list_frame, bg="#00A6D0", highlightthickness=0)
delete_scrollbar = Scrollbar(delete_list_frame, orient=VERTICAL, command=delete_canvas.yview)
delete_scrollable_frame = Frame(delete_canvas, bg="#00A6D0")

delete_scrollable_frame.bind(
    "<Configure>",
    lambda e: delete_canvas.configure(scrollregion=delete_canvas.bbox("all"))
)

delete_canvas.create_window((0, 0), window=delete_scrollable_frame, anchor="nw")
delete_canvas.configure(yscrollcommand=delete_scrollbar.set)

delete_canvas.pack(side=LEFT, fill=BOTH, expand=True)
delete_scrollbar.pack(side=RIGHT, fill=Y)

delete_check_vars = []

def refresh_delete_list():
    for widget in delete_scrollable_frame.winfo_children():
        widget.destroy()
    delete_check_vars.clear()

    items = []
    if delete_type_var.get() == "MotherBoard":
        items = motherboard_items
    elif delete_type_var.get() == "Ram":
        items = ram_items
    elif delete_type_var.get() == "PC Monitor":
        items = pc_monitor_items
    elif delete_type_var.get() == "PC Case":
        items = pc_case_items

    for idx, item in enumerate(items):
        var = IntVar(value=0)
        delete_check_vars.append((var, item))
        Checkbutton(delete_scrollable_frame, text=f"{item['product']} (ID: {item['id']})", variable=var, bg="#00A6D0", fg="black", font=("Arial", 12), anchor="w").pack(fill="x", padx=5, pady=2)

def delete_selected_items():
    items = []
    if delete_type_var.get() == "MotherBoard":
        items = motherboard_items
    elif delete_type_var.get() == "Ram":
        items = ram_items
    elif delete_type_var.get() == "PC Monitor":
        items = pc_monitor_items
    elif delete_type_var.get() == "PC Case":
        items = pc_case_items

    for var, item in delete_check_vars:
        if var.get() == 1:
            items.remove(item)

    messagebox.showinfo("Success", "Selected items deleted successfully!")
    refresh_delete_list()

delete_button = Button(delete_product_window, text="Delete", command=delete_selected_items, bg="red", fg="white", font=("Arial", 12, "bold"))
delete_button.place(relx=0.5, y=380, width=100, height=30, anchor="center")

delete_type_option.bind("<<ComboboxSelected>>", lambda e: refresh_delete_list())
        
def logging_out():
    confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
    if confirm:
        bg_label.config(image=bg_image1)
        cart_frame.place_forget()
        purchasing_list_frame.place_forget()
        purchasing_table_frame.place_forget()
        cart_list_frame.place_forget()
        purchase_table_frame.place_forget()
        add_product_window.place_forget()
        delete_product_window.place_forget()
        title_label.config(text='Computer Shop', fg='#00D3FF', bg='#41566b')
        show_login.place(x=690, y=130, width=150, height=50)
        display_usernow.config(text="")
        menu_button.place_forget()
        open_login_window()

menu_button = ttk.Menubutton(main_window, text="options", style="TMenubutton")

# dropdown menu
menu = Menu(menu_button, tearoff=0, font=("Arial", 10))
def admin_menu():
    menu.delete(0, END)
    if display_usernow.cget('text') == "Current user: admin":
        menu.add_command(label="Add Product", command=open_close_add_product)
        menu.add_command(label="Remove Product", command=open_close_delete_product)
        menu.add_separator()
        menu.add_command(label="Log Out", command=logging_out)
    else:
        menu.delete(0, END)
        menu.add_command(label="Log Out", command=logging_out)
# menu to the button
menu_button["menu"] = menu

# ttk styling for menu
style = ttk.Style()
style.configure("TMenubutton", font=("Arial", 12), background="#197D7C", foreground="white")

# display the current date and time
time_label = Label(main_frame, font=('Arial', 15), fg='white', bg='black')  
time_label.place(x=1220, y=10)

# time and date update
def update_time():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    time_label.config(text=f"Date: {current_date} Time: {current_time}")
    time_label.after(1000, update_time)  # Update every 1 second

update_time()

# display usernow
display_usernow = Label(main_frame, font=('Arial', 15, "bold"), fg='white', bg='black')  
display_usernow.place(relx=0.5, y=20, anchor="center")
    
# label for the title
title_label = Label(main_frame, text='Computer Shop', font=('Arial', 30, "bold"), fg='#00D3FF', bg='#41566b') 
title_label.place(relx=0.5, rely=0.1, anchor='center', width=400, height=50)

# buttons for Cart, Purchasing, and Purchase Table
cart_frame = Frame(main_frame, bg="#82CDF9", highlightbackground="#39c8b1", highlightthickness=2)
cart_button = Button(cart_frame, text="Cart", bg='#39c8b1', fg='#101719', font=("Arial", 15, "bold"), bd=0, relief="flat")
cart_button.pack(fill=BOTH, expand=True)

purchasing_list_frame = Frame(main_frame, bg="#82CDF9", highlightbackground="#39c8b1", highlightthickness=2)
purchasing_list_button = Button(purchasing_list_frame, text="Purchase List", bg='#39c8b1', fg='#101719', font=("Arial", 15, "bold"), bd=0, relief="flat")
purchasing_list_button.pack(fill=BOTH, expand=True)

purchasing_table_frame = Frame(main_frame, bg="#82CDF9", highlightbackground="#39c8b1", highlightthickness=2)
purchasing_table_button = Button(purchasing_table_frame, text="Purchase Table", bg='#39c8b1', fg='#101719', font=("Arial", 15, "bold"), bd=0, relief="flat")
purchasing_table_button.pack(fill=BOTH, expand=True)

def cart_enter(event):
    cart_button.config(bg="#101719", fg="white")
def cart_leave(event):
    cart_button.config(bg="#39c8b1", fg="#101719")
def cart_action(event):
    cart_button.config(bg="#101719", fg="white")
    if cart_list_frame.winfo_viewable():
        cart_list_frame.place_forget()
    else:
        cart_list_frame.place(relx=0.5, y=500, anchor='center', width=1440, height=500)
        selected_items_frame.place_forget()
        refresh_selected_items(row, total_price)
        add_product_window.place_forget()
        delete_product_window.place_forget()
        purchase_table_frame.place_forget()
def purchasing_enter(event):
    purchasing_list_button.config(bg="#101719", fg="white")
def purchasing_leave(event):
    purchasing_list_button.config(bg="#39c8b1", fg="#101719")
def purchasing_action(event):
    if not selected_items:
        messagebox.showwarning("Error", "No items selected.")
    else:
        if selected_items_frame.winfo_viewable():
            print("undisplayed")
            selected_items_frame.place_forget()
            refresh_selected_items(row, total_price)
        else:
            print("displayed")
            selected_items_frame.place(relx=0.5, rely=0.6, anchor='center', width=800, height=400)
            refresh_selected_items(row, total_price)
            cart_list_frame.place_forget()
            add_product_window.place_forget()
            delete_product_window.place_forget()
            purchase_table_frame.place_forget()

def purchasing_table_enter(event):
    purchasing_table_button.config(bg="#101719", fg="white")
def purchasing_table_leave(event):
    purchasing_table_button.config(bg="#39c8b1", fg="#101719")

cart_button.bind("<Enter>", cart_enter)
cart_button.bind("<Leave>", cart_leave)
cart_button.bind("<Button-1>", cart_action)
purchasing_list_button.bind("<Enter>", purchasing_enter)
purchasing_list_button.bind("<Leave>", purchasing_leave)
purchasing_list_button.bind("<Button-1>", purchasing_action)
purchasing_table_button.bind("<Enter>", purchasing_table_enter)
purchasing_table_button.bind("<Leave>", purchasing_table_leave)

cart_list_frame = Frame(main_frame, bg='#39c8b1')

# canvas and a vertical scrollbar for scrolling
canvas = Canvas(cart_list_frame, bg='#39c8b1', highlightthickness=0)
v_scrollbar = Scrollbar(cart_list_frame, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas, bg='#39c8b1')

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Bind mouse wheel scrolling to the canvas
def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

# Bind mouse wheel scrolling to the canvas and its children
def bind_mouse_wheel_to_children(widget):
    widget.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mouse_wheel))
    widget.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
    for child in widget.winfo_children():
        bind_mouse_wheel_to_children(child)

bind_mouse_wheel_to_children(scrollable_frame)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=v_scrollbar.set)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
v_scrollbar.pack(side=RIGHT, fill=Y)

# Function to display motherboards items
def display_motherboards_items():
    check_buttons = []
    product_labels = []
    price_labels = []
    quantity_labels = []
    brand_labels = []
    checkb_vars = []
    
    for idx, item in enumerate(motherboard_items):
        # Load and resize the item image
        item_image = Image.open(item["image"])
        item_image = item_image.resize((100, 100))
        item_photo = ImageTk.PhotoImage(item_image)

        # Create a frame for each item
        item_frame = Frame(scrollable_frame, bg='#101719', bd=2, relief="solid")
        item_frame.grid(row=idx, column=0, pady=(35, 0), padx=15, sticky="w")

        # Display motherboards_items
        Label(scrollable_frame, text="MOTHERBOARD", font=("Arial", 14, "bold"), bg='#101719', fg='white').grid(row=0, column=0, sticky="n", padx=5, pady=(5, 0))

        # Display the id of the item
        id_label = Label(item_frame, text=f"ID: {item['id']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        id_label.grid(row=0, column=0, sticky="w", padx=5)

        # Display the item image
        image_label = Label(item_frame, image=item_photo, bg='#101719', fg='white')
        image_label.image = item_photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=1, column=0, rowspan=5, padx=5, pady=5)

        # Display the product name
        product_label = Label(item_frame, text=f"Product: {item['product']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        product_label.grid(row=1, column=1, sticky="w", padx=5)
        product_labels.append(product_label)

        # Display the price
        price_label = Label(item_frame, text=f"Price: {item['price']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        price_label.grid(row=2, column=1, sticky="w", padx=5)
        price_labels.append(price_label)

        # Display the quantity as a clickable label for updating
        label_var = StringVar()
        item['quantity'] = 0
        label_var.set(f"Quantity: {item['quantity']}")

        def create_update_function(item, label_var):
            def update_quantity(event):
                new_quantity = simpledialog.askinteger("Update Quantity", f"Enter new quantity for {item['product']}:")
                if new_quantity is not None:
                    if new_quantity < 0:
                        messagebox.showwarning("Error", "Quantity must be greater than 0.")
                    else:
                        if new_quantity > int(item['quantity']):  # Increasing quantity
                            difference = new_quantity - int(item['quantity'])
                            if difference > int(item['stack']):
                                messagebox.showwarning("Error", f"Only {item['stack']} available in stock.")
                                return
                            item['stack'] = str(int(item['stack']) - difference)  # Decrease the stack
                        elif new_quantity < int(item['quantity']):  # Decreasing quantity
                            difference = int(item['quantity']) - new_quantity
                            item['stack'] = str(int(item['stack']) + difference)  # Increase the stack

                        label_var.set(f"Quantity: {new_quantity}")
                        item['quantity'] = str(new_quantity)
                        motherboard_items[item['id'] - 1]['quantity'] = str(new_quantity)
                        stack_label.config(text=f"Stack: {item['stack']}")  # update stack label
                        motherboard_items[item['id'] - 1]['stack'] = item['stack']
                        print(f"Set Quantity = {motherboard_items[item['id'] - 1]['quantity']}, Remaining Stack = {motherboard_items[item['id'] - 1]['stack']}")
            return update_quantity

        def on_enter_function(label_var):
            def on_enter(event):
                label_var.set(f"Click me")
                event.widget.config(textvariable=label_var)
            return on_enter

        def on_leave_function(item, label_var):
            def on_leave(event):
                label_var.set(f"Quantity: {item['quantity']}")
                event.widget.config(textvariable=label_var)
            return on_leave

        update_function = create_update_function(item, label_var)
        on_enter = on_enter_function(label_var)
        on_leave = on_leave_function(item, label_var)
        quantity_label = Label(item_frame, textvariable=label_var, font=("Arial", 12), bg='#101719', fg='white', anchor='w', cursor="hand2")
        quantity_label.grid(row=3, column=1, sticky="w", padx=5)
        quantity_labels.append(quantity_label)
        quantity_label.bind("<Button-1>", update_function)
        quantity_label.bind("<Enter>", on_enter)
        quantity_label.bind("<Leave>", on_leave)

        # Display the brand
        brand_label = Label(item_frame, text=f"Brand: {item['brand']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        brand_label.grid(row=4, column=1, sticky="w", padx=5)
        brand_labels.append(brand_label)

        stack_label = Label(item_frame, text=f"Stack: {item['stack']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        stack_label.grid(row=5, column=1, sticky="w", padx=5)

        # Add a Checkbutton for each item to track selection
        var = IntVar(value=0)  # Initialize IntVar with a default value of 0
        motherboard_items[item['id'] - 1]['selected'] = var
        checkb_vars.append(var)

        checkout_checkbutton = Checkbutton(item_frame, text="Select", bg='#101719', font=("Arial", 13), fg='white', selectcolor='#4D0277', indicatoron=False)
        checkout_checkbutton.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
        check_buttons.append(checkout_checkbutton)

    def on_check(index):
        if int(motherboard_items[index]['stack']) == 0:
            messagebox.showwarning("Error", f"{motherboard_items[index]['product']} is out of stock.")
            checkb_vars[index].set(0)  # Uncheck the checkbox
        elif checkb_vars[index].get():
            selected_items.append({"product": motherboard_items[index]['product'], "quantity": motherboard_items[index]['quantity'], "price": motherboard_items[index]['price'], "brand": motherboard_items[index]['brand'], "type": "Motherboard", "id": motherboard_items[index]['id']})
            print(selected_items)
        else:
            for i, item in enumerate(selected_items):
                if item['id'] == motherboard_items[index]['id']:
                    selected_items.pop(i)
                    break
            print(selected_items)
        display_purchase_table(row_table)
        refresh_selected_items(row, total_price)
    for i in range(len(check_buttons)):
        check_buttons[i].config(command=lambda i=i: on_check(i), variable=checkb_vars[i])

    bind_mouse_wheel_to_children(scrollable_frame)

display_motherboards_items()

# Function to display rams items
def display_rams_items():
    check_buttons = []
    product_labels = []
    price_labels = []
    quantity_labels = []
    brand_labels = []
    checkb_vars = []

    for idx, item in enumerate(ram_items):
        # Load and resize the item image
        item_image = Image.open(item["image"])
        item_image = item_image.resize((100, 100))
        item_photo = ImageTk.PhotoImage(item_image)

        # Create a frame for each item
        item_frame = Frame(scrollable_frame, bg='#101719', bd=2, relief="solid")
        item_frame.grid(row=idx, column=1, pady=(35, 0), padx=15, sticky="nw")

        # Display rams_items
        Label(scrollable_frame, text="RAM", font=("Arial", 14, "bold"), bg='#101719', fg='white').grid(row=0, column=1, sticky="n", padx=5, pady=(5, 0))

        # Display the id of the item
        id_label = Label(item_frame, text=f"ID: {item['id']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        id_label.grid(row=0, column=0, sticky="w", padx=5)

        # Display the item image
        image_label = Label(item_frame, image=item_photo, bg='#101719', fg='white')
        image_label.image = item_photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=1, column=0, rowspan=5, padx=5, pady=5)

        # Display the product name
        product_label = Label(item_frame, text=f"Product: {item['product']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        product_label.grid(row=1, column=1, sticky="w", padx=5)
        product_labels.append(product_label)

        # Display the price
        price_label = Label(item_frame, text=f"Price: {item['price']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        price_label.grid(row=2, column=1, sticky="w", padx=5)
        price_labels.append(price_label)

        # Display the quantity as a clickable label for updating
        label_var = StringVar()
        label_var.set(f"Quantity: {item['quantity']}")

        def create_update_function(item, label_var):
            def update_quantity(event):
                new_quantity = simpledialog.askinteger("Update Quantity", f"Enter new quantity for {item['product']}:")
                if new_quantity is not None:
                    if new_quantity < 0:
                        messagebox.showwarning("Error", "Quantity must be greater than 0.")
                    else:
                        if new_quantity > int(item['quantity']):  # Increasing quantity
                            difference = new_quantity - int(item['quantity'])
                            if difference > int(item['stack']):
                                messagebox.showwarning("Error", f"Only {item['stack']} available in stock.")
                                return
                            item['stack'] = str(int(item['stack']) - difference)  # Decrease the stack
                        elif new_quantity < int(item['quantity']):  # Decreasing quantity
                            difference = int(item['quantity']) - new_quantity
                            item['stack'] = str(int(item['stack']) + difference)  # Increase the stack

                        label_var.set(f"Quantity: {new_quantity}")
                        item['quantity'] = str(new_quantity)
                        ram_items[item['id'] - 1]['quantity'] = str(new_quantity)
                        stack_label.config(text=f"Stack: {item['stack']}")  # update stack label
                        ram_items[item['id'] - 1]['stack'] = item['stack']
                        print(f"Set Quantity = {ram_items[item['id'] - 1]['quantity']}, Remaining Stack = {motherboard_items[item['id'] - 1]['stack']}")
            return update_quantity

        def on_enter_function(label_var):
            def on_enter(event):
                label_var.set(f"Click me")
                event.widget.config(textvariable=label_var)
            return on_enter

        def on_leave_function(item, label_var):
            def on_leave(event):
                label_var.set(f"Quantity: {item['quantity']}")
                event.widget.config(textvariable=label_var)
            return on_leave

        update_function = create_update_function(item, label_var)
        on_enter = on_enter_function(label_var)
        on_leave = on_leave_function(item, label_var)
        quantity_label = Label(item_frame, textvariable=label_var, font=("Arial", 12), bg='#101719', fg='white', anchor='w', cursor="hand2")
        quantity_label.grid(row=3, column=1, sticky="w", padx=5)
        quantity_labels.append(quantity_label)
        quantity_label.bind("<Button-1>", update_function)
        quantity_label.bind("<Enter>", on_enter)
        quantity_label.bind("<Leave>", on_leave)

        # Display the brand
        brand_label = Label(item_frame, text=f"Brand: {item['brand']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        brand_label.grid(row=4, column=1, sticky="w", padx=5)
        brand_labels.append(brand_label)

        # Display the stack
        stack_label = Label(item_frame, text=f"Stack: {item['stack']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        stack_label.grid(row=5, column=1, sticky="w", padx=5)

        # Add a Checkbutton for each item to track selection
        var = IntVar(value=0)  # Initialize IntVar with a default value of 0
        ram_items[item['id'] - 1]['selected'] = var
        checkb_vars.append(var)

        checkout_checkbutton = Checkbutton(item_frame, text="Select", bg='#101719', font=("Arial", 13), fg='white', selectcolor='#4D0277', indicatoron=False)
        checkout_checkbutton.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
        check_buttons.append(checkout_checkbutton)

    def on_check(index):
        if checkb_vars[index].get():
            selected_items.append({"product": ram_items[index]['product'], "quantity": ram_items[index]['quantity'], "price": ram_items[index]['price'], "brand": ram_items[index]['brand'], "type": "ram", "id": ram_items[index]['id']})
        else:
            for i, item in enumerate(selected_items):
                if item['id'] == ram_items[index]['id']:
                    selected_items.pop(i)
                    break
            print(selected_items)
        display_purchase_table(row_table)
        refresh_selected_items(row, total_price)
    for i in range(len(check_buttons)):
        check_buttons[i].config(command=lambda i=i: on_check(i), variable=checkb_vars[i])
    
    bind_mouse_wheel_to_children(scrollable_frame)

display_rams_items()

# Function to display pcmonitor items
def display_pcmonitor_items():
    check_buttons = []
    product_labels = []
    price_labels = []
    quantity_labels = []
    brand_labels = []
    checkb_vars = []

    for idx, item in enumerate(pc_monitor_items):
        # Load and resize the item image
        item_image = Image.open(item["image"])
        item_image = item_image.resize((100, 100))
        item_photo = ImageTk.PhotoImage(item_image)

        # Create a frame for each item
        item_frame = Frame(scrollable_frame, bg='#101719', bd=2, relief="solid")
        item_frame.grid(row=idx, column=2, pady=(35, 0), padx=15, sticky="ne")

        # Display pcmonitor_items
        Label(scrollable_frame, text="PC MONITOR", font=("Arial", 14, "bold"), bg='#101719', fg='white').grid(row=0, column=2, sticky="n", padx=5, pady=(5, 0))

        # Display the id of the item
        id_label = Label(item_frame, text=f"ID: {item['id']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        id_label.grid(row=0, column=0, sticky="w", padx=5)

        # Display the item image
        image_label = Label(item_frame, image=item_photo, bg='#101719', fg='white')
        image_label.image = item_photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=1, column=0, rowspan=5, padx=5, pady=5)

        # Display the product name
        product_label = Label(item_frame, text=f"Product: {item['product']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        product_label.grid(row=1, column=1, sticky="w", padx=5)
        product_labels.append(product_label)

        # Display the price
        price_label = Label(item_frame, text=f"Price: {item['price']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        price_label.grid(row=2, column=1, sticky="w", padx=5)
        price_labels.append(price_label)

        # Display the quantity as a clickable label for updating
        label_var = StringVar()
        label_var.set(f"Quantity: {item['quantity']}")

        def create_update_function(item, label_var):
            def update_quantity(event):
                new_quantity = simpledialog.askinteger("Update Quantity", f"Enter new quantity for {item['product']}:")
                if new_quantity is not None:
                    if new_quantity < 0:
                        messagebox.showwarning("Error", "Quantity must be greater than 0.")
                    else:
                        if new_quantity > int(item['quantity']):  # Increasing quantity
                            difference = new_quantity - int(item['quantity'])
                            if difference > int(item['stack']):
                                messagebox.showwarning("Error", f"Only {item['stack']} available in stock.")
                                return
                            item['stack'] = str(int(item['stack']) - difference)  # Decrease the stack
                        elif new_quantity < int(item['quantity']):  # Decreasing quantity
                            difference = int(item['quantity']) - new_quantity
                            item['stack'] = str(int(item['stack']) + difference)  # Increase the stack

                        label_var.set(f"Quantity: {new_quantity}")
                        item['quantity'] = str(new_quantity)
                        pc_monitor_items[item['id'] - 1]['quantity'] = str(new_quantity)
                        stack_label.config(text=f"Stack: {item['stack']}")  # update stack label
                        pc_monitor_items[item['id'] - 1]['stack'] = item['stack']
                        print(f"Set Quantity = {pc_monitor_items[item['id'] - 1]['quantity']}, Remaining Stack = {motherboard_items[item['id'] - 1]['stack']}")
            return update_quantity

        def on_enter_function(label_var):
            def on_enter(event):
                label_var.set(f"Click me")
                event.widget.config(textvariable=label_var)
            return on_enter

        def on_leave_function(item, label_var):
            def on_leave(event):
                label_var.set(f"Quantity: {item['quantity']}")
                event.widget.config(textvariable=label_var)
            return on_leave

        update_function = create_update_function(item, label_var)
        on_enter = on_enter_function(label_var)
        on_leave = on_leave_function(item, label_var)
        quantity_label = Label(item_frame, textvariable=label_var, font=("Arial", 12), bg='#101719', fg='white', anchor='w', cursor="hand2")
        quantity_label.grid(row=3, column=1, sticky="w", padx=5)
        quantity_labels.append(quantity_label)
        quantity_label.bind("<Button-1>", update_function)
        quantity_label.bind("<Enter>", on_enter)
        quantity_label.bind("<Leave>", on_leave)

        # Display the brand
        brand_label = Label(item_frame, text=f"Brand: {item['brand']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        brand_label.grid(row=4, column=1, sticky="w", padx=5)
        brand_labels.append(brand_label)

        stack_label = Label(item_frame, text=f"Stack: {item['stack']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        stack_label.grid(row=5, column=1, sticky="w", padx=5)

       # Add a Checkbutton for each item to track selection
        var = IntVar(value=0)  # Initialize IntVar with a default value of 0
        pc_monitor_items[item['id'] - 1]['selected'] = var
        checkb_vars.append(var)

        checkout_checkbutton = Checkbutton(item_frame, text="Select", bg='#101719', font=("Arial", 13), fg='white', selectcolor='#4D0277', indicatoron=False)
        checkout_checkbutton.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
        check_buttons.append(checkout_checkbutton)

    def on_check(index):
        if checkb_vars[index].get():
            selected_items.append({"product": pc_monitor_items[index]['product'], "quantity": pc_monitor_items[index]['quantity'], "price": pc_monitor_items[index]['price'], "brand": pc_monitor_items[index]['brand'], "type": "ram", "id": pc_monitor_items[index]['id']})
        else:
            for i, item in enumerate(selected_items):
                if item['id'] == pc_monitor_items[index]['id']:
                    selected_items.pop(i)
                    break
            print(selected_items)
        display_purchase_table(row_table)
        refresh_selected_items(row, total_price)
    for i in range(len(check_buttons)):
        check_buttons[i].config(command=lambda i=i: on_check(i), variable=checkb_vars[i])

    bind_mouse_wheel_to_children(scrollable_frame)

display_pcmonitor_items()

# Function to display computercase items
def display_computercase_items():
    check_buttons = []
    product_labels = []
    price_labels = []
    quantity_labels = []
    brand_labels = []
    checkb_vars = []

    for idx, item in enumerate(pc_case_items):
        # Load and resize the item image
        item_image = Image.open(item["image"])
        item_image = item_image.resize((100, 100))
        item_photo = ImageTk.PhotoImage(item_image)

        # Create a frame for each item
        item_frame = Frame(scrollable_frame, bg='#101719', bd=2, relief="solid")
        item_frame.grid(row=idx, column=3, pady=(35, 0), padx=15, sticky="es")

        # Display computercase_items
        Label(scrollable_frame, text="PC CASE", font=("Arial", 14, "bold"), bg='#101719', fg='white').grid(row=0, column=3, sticky="n", padx=5, pady=(5, 0))

        # Display the id of the item
        id_label = Label(item_frame, text=f"ID: {item['id']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        id_label.grid(row=0, column=0, sticky="w", padx=5)

        # Display the item image
        image_label = Label(item_frame, image=item_photo, bg='#101719', fg='white')
        image_label.image = item_photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=1, column=0, rowspan=5, padx=5, pady=5)

        # Display the product name
        product_label = Label(item_frame, text=f"Product: {item['product']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        product_label.grid(row=1, column=1, sticky="w", padx=5)
        product_labels.append(product_label)

        # Display the price
        price_label = Label(item_frame, text=f"Price: {item['price']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        price_label.grid(row=2, column=1, sticky="w", padx=5)
        price_labels.append(price_label)

        # Display the quantity as a clickable label for updating
        label_var = StringVar()
        label_var.set(f"Quantity: {item['quantity']}")

        def create_update_function(item, label_var):
            def update_quantity(event):
                new_quantity = simpledialog.askinteger("Update Quantity", f"Enter new quantity for {item['product']}:")
                if new_quantity is not None:
                    if new_quantity < 0:
                        messagebox.showwarning("Error", "Quantity must be greater than 0.")
                    else:
                        if new_quantity > int(item['quantity']):  # Increasing quantity
                            difference = new_quantity - int(item['quantity'])
                            if difference > int(item['stack']):
                                messagebox.showwarning("Error", f"Only {item['stack']} available in stock.")
                                return
                            item['stack'] = str(int(item['stack']) - difference)  # Decrease the stack
                        elif new_quantity < int(item['quantity']):  # Decreasing quantity
                            difference = int(item['quantity']) - new_quantity
                            item['stack'] = str(int(item['stack']) + difference)  # Increase the stack

                        label_var.set(f"Quantity: {new_quantity}")
                        item['quantity'] = str(new_quantity)
                        pc_case_items[item['id'] - 1]['quantity'] = str(new_quantity)
                        stack_label.config(text=f"Stack: {item['stack']}")  # update stack label
                        pc_case_items[item['id'] - 1]['stack'] = item['stack']
                        print(f"Set Quantity = {pc_case_items[item['id'] - 1]['quantity']}, Remaining Stack = {motherboard_items[item['id'] - 1]['stack']}")
            return update_quantity

        def on_enter_function(label_var):
            def on_enter(event):
                label_var.set(f"Click me")
                event.widget.config(textvariable=label_var)
            return on_enter

        def on_leave_function(item, label_var):
            def on_leave(event):
                label_var.set(f"Quantity: {item['quantity']}")
                event.widget.config(textvariable=label_var)
            return on_leave

        update_function = create_update_function(item, label_var)
        on_enter = on_enter_function(label_var)
        on_leave = on_leave_function(item, label_var)
        quantity_label = Label(item_frame, textvariable=label_var, font=("Arial", 12), bg='#101719', fg='white', anchor='w', cursor="hand2")
        quantity_label.grid(row=3, column=1, sticky="w", padx=5)
        quantity_labels.append(quantity_label)
        quantity_label.bind("<Button-1>", update_function)
        quantity_label.bind("<Enter>", on_enter)
        quantity_label.bind("<Leave>", on_leave)

        # Display the brand
        brand_label = Label(item_frame, text=f"Brand: {item['brand']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        brand_label.grid(row=4, column=1, sticky="w", padx=5)
        brand_labels.append(brand_label)

        stack_label = Label(item_frame, text=f"Stack: {item['stack']}", font=("Arial", 12), bg='#101719', fg='white', anchor='w')
        stack_label.grid(row=5, column=1, sticky="w", padx=5)

        # Add a Checkbutton for each item to track selection
        var = IntVar(value=0)  # Initialize IntVar with a default value of 0
        pc_case_items[item['id'] - 1]['selected'] = var
        checkb_vars.append(var)

        checkout_checkbutton = Checkbutton(item_frame, text="Select", bg='#101719', font=("Arial", 13), fg='white', selectcolor='#4D0277', indicatoron=False)
        checkout_checkbutton.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
        check_buttons.append(checkout_checkbutton)

    def on_check(index):
        if checkb_vars[index].get():
            selected_items.append({"product": pc_case_items[index]['product'], "quantity": pc_case_items[index]['quantity'], "price": pc_case_items[index]['price'], "brand": pc_case_items[index]['brand'], "type": "computercase", "id": pc_case_items[index]['id']})
        else:
            for i, item in enumerate(selected_items):
                if item['id'] == pc_case_items[index]['id']:
                    selected_items.pop(i)
                    break
            print(selected_items)
        display_purchase_table(row_table)
        refresh_selected_items(row, total_price)
    for i in range(len(check_buttons)):
        check_buttons[i].config(command=lambda i=i: on_check(i), variable=checkb_vars[i])

    bind_mouse_wheel_to_children(scrollable_frame)

display_computercase_items()

# Function to display the selected items
selected_items_frame = Frame(main_frame, bg='#101719', bd=2, relief="solid")

Label(selected_items_frame, text="Selected Items", font=("Arial", 18, "bold"), bg='#101719', fg='white').place(relx=0.5, y=25, anchor="center")

items_list_frame = Frame(selected_items_frame, bg='#39C8B1')
items_list_frame.place(relx=0.5, anchor='center', relwidth=0.98, y=200, relheight=0.7)

# Add a canvas and a scrollbar for scrolling
canvas2 = Canvas(items_list_frame, bg='#39C8B1', highlightthickness=0)
scrollbar2 = Scrollbar(items_list_frame, orient=VERTICAL, command=canvas2.yview)
scrollable_frame2 = Frame(canvas2, bg='#39C8B1')

# Configure the canvas and scrollbar
canvas2.create_window((0, 0), window=scrollable_frame2, anchor="nw")
canvas2.configure(yscrollcommand=scrollbar2.set)

# Pack the canvas and scrollbar
canvas2.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar2.pack(side=RIGHT, fill=Y)

# Bind mouse wheel scrolling to the canvas
def on_mouse_wheel2(event):
    canvas2.yview_scroll(-1 * (event.delta // 120), "units")

# Bind mouse wheel scrolling to the canvas and its children
def bind_mouse_wheel_to_children2(widget):
    widget.bind("<Enter>", lambda e: canvas2.bind_all("<MouseWheel>", on_mouse_wheel2))
    widget.bind("<Leave>", lambda e: canvas2.unbind_all("<MouseWheel>"))
    for child in widget.winfo_children():
        bind_mouse_wheel_to_children2(child)

bind_mouse_wheel_to_children2(scrollable_frame2)

# Update the scroll region when the frame's content changes
scrollable_frame2.bind(
    "<Configure>",
    lambda e: canvas2.configure(scrollregion=canvas2.bbox("all"))
)

total_price = 0
row = 0
display_labels_selected_frame = []

def refresh_selected_items(row, total_price):
    row = 0
    for widget in display_labels_selected_frame:
        widget.destroy()  # Clear all widgets in the frame

    if selected_items:
        for items in selected_items:
            print(items)
    else:
        print("No items selected.")

    for item in selected_items:
        print(selected_items)
        item_frame = Frame(scrollable_frame2, bg='#101719', width=750, height=120)  # Set the width to match other item frames
        item_frame.grid(row=row, column=0, sticky="n", padx=5, pady=5)
        item_frame.grid_propagate(False)  # Prevent the frame from resizing to its content

        display_product_id = Label(item_frame, text=f"ID: {item['id']}", font=("Arial", 14, "bold"), bg='#101719', fg='white')
        display_product_id.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        display_product_name = Label(item_frame, text=f"Product: {item['product']}", font=("Arial", 14, "bold"), bg='#101719', fg='white')
        display_product_name.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        display_product_type = Label(item_frame, text=f"Type: {item['type']}", font=("Arial", 14), bg='#101719', fg='white')
        display_product_type.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        display_product_brand = Label(item_frame, text=f"Brand: {item['brand']}", font=("Arial", 14), bg='#101719', fg='white')
        display_product_brand.grid(row=1, column=2, sticky="w", padx=10, pady=5)
        display_product_price = Label(item_frame, text=f"Price: {item['price']}", font=("Arial", 14), bg='#101719', fg='white')
        display_product_price.grid(row=1, column=3, sticky="w", padx=10, pady=5)
        display_product_quantity = Label(item_frame, text=f"Quantity: {item['quantity']}", font=("Arial", 14), bg='#101719', fg='white')
        display_product_quantity.grid(row=1, column=4, sticky="n", padx=10, pady=5)

        display_labels_selected_frame.append(item_frame)

        total_price += (float(item['price'].replace("$", "")) * int(item['quantity']))
        row += 1
        display_total_price.config(text=f"Overall Price: ${total_price}")

    bind_mouse_wheel_to_children2(scrollable_frame2)

display_total_price = Label(selected_items_frame, text=f"Overall Price: ${total_price}", font=("Arial", 14, "bold"), bg='#101719', fg='white')
display_total_price.place(relx=0.5, rely=0.95, anchor='center')

refresh_selected_items(row, total_price)

# Purchase Table Frame
purchase_table_frame = Frame(main_frame, bg='#101719', bd=2, relief="solid")

Label(purchase_table_frame, text="Purchase Table", font=("Arial", 18, "bold"), bg='#101719', fg='white').place(relx=0.5, y=25, anchor="center")

purchase_items_frame = Frame(purchase_table_frame, bg='#39C8B1')
purchase_items_frame.place(relx=0.5, anchor='center', relwidth=0.98, y=230, relheight=0.7)

# Add a canvas and a scrollbar for scrolling
canvas3 = Canvas(purchase_items_frame, bg='#39C8B1', highlightthickness=0)
scrollbar3 = Scrollbar(purchase_items_frame, orient=VERTICAL, command=canvas3.yview)
scrollable_frame3 = Frame(canvas3, bg='#39C8B1')

# Configure the canvas and scrollbar
canvas3.create_window((0, 0), window=scrollable_frame3, anchor="nw")
canvas3.configure(yscrollcommand=scrollbar3.set)

# Pack the canvas and scrollbar
canvas3.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar3.pack(side=RIGHT, fill=Y)

# Bind mouse wheel scrolling to the canvas
def on_mouse_wheel3(event):
    canvas3.yview_scroll(-1 * (event.delta // 120), "units")

# Bind mouse wheel scrolling to the canvas and its children
def bind_mouse_wheel_to_children3(widget):
    widget.bind("<Enter>", lambda e: canvas3.bind_all("<MouseWheel>", on_mouse_wheel3))
    widget.bind("<Leave>", lambda e: canvas3.unbind_all("<MouseWheel>"))
    for child in widget.winfo_children():
        bind_mouse_wheel_to_children3(child)

bind_mouse_wheel_to_children3(scrollable_frame3)

# Update the scroll region when the frame's content changes
scrollable_frame3.bind(
    "<Configure>",
    lambda e: canvas3.configure(scrollregion=canvas3.bbox("all"))
)

row_table = 0
display_labels_purchase_table = []

def display_purchase_table(row_table):
    row_table = 0 #reset row table
    for widget in display_labels_purchase_table:
        widget.destroy()  # Clear widgets
    display_labels_purchase_table.clear()

    total_price = 0
    for item in selected_items:
        item_frame = Frame(scrollable_frame3, bg='#101719', width=750, height=120)  # Set the width to match other item frames
        item_frame.grid(row=row_table, column=0, sticky="n", padx=5, pady=5)
        item_frame.grid_propagate(False)  # Prevent the frame from resizing to its content

        display_label_id = Label(item_frame, text=f"ID: {item['id']}", font=("Arial", 14, "bold"), bg='#101719', fg='white')
        display_label_id.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        display_label_product = Label(item_frame, text=f"Product: {item['product']}", font=("Arial", 14, "bold"), bg='#101719', fg='white')
        display_label_product.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        display_label_type = Label(item_frame, text=f"Type: {item['type']}", font=("Arial", 14), bg='#101719', fg='white')
        display_label_type.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        display_label_brand = Label(item_frame, text=f"Brand: {item['brand']}", font=("Arial", 14), bg='#101719', fg='white')
        display_label_brand.grid(row=1, column=2, sticky="w", padx=10, pady=5)
        display_label_price = Label(item_frame, text=f"Price: {item['price']}", font=("Arial", 14), bg='#101719', fg='white')
        display_label_price.grid(row=1, column=3, sticky="w", padx=10, pady=5)
        display_label_quant = Label(item_frame, text=f"Quantity: {item['quantity']}", font=("Arial", 14), bg='#101719', fg='white')
        display_label_quant.grid(row=1, column=4, sticky="n", padx=10, pady=5)

        display_labels_purchase_table.append(item_frame)

        total_price += (float(item['price'].replace("$", "")) * int(item['quantity']))
        row_table += 1
        display_total_price_table.config(text=f"Total Price: ${total_price:.2f}")
        
        print(f"Selected Items: {selected_items}")
        print(f"Row Table: {row_table}")

    bind_mouse_wheel_to_children3(scrollable_frame3)

display_total_price_table = Label(purchase_table_frame, text=f"Total Price: ${total_price:.2f}", font=("Arial", 14, "bold"), bg='#101719', fg='white')
display_total_price_table.place(relx=0.5, rely=0.95, anchor='center')

display_purchase_table(row_table)

# Function to generate receipt
def generate_receipt():
    if not selected_items:
        messagebox.showwarning("Error", "No items selected for purchase.")
        return

    receipt_window = Toplevel(main_window)
    receipt_window.title("Receipt")
    receipt_window.configure(bg='#101719')
    receipt_window.geometry("350x600")
    receipt_window.resizable(False, False)

    # Center the receipt window on the screen
    receipt_window.update_idletasks()
    screen_width = receipt_window.winfo_screenwidth()
    screen_height = receipt_window.winfo_screenheight()
    x = (screen_width // 2) - (350 // 2)
    y = (screen_height // 2) - (600 // 2)
    receipt_window.geometry(f"350x600+{x}+{y}")

    Label(receipt_window, text="Receipt", font=("Arial", 18, "bold"), bg='#101719', fg='white').pack(pady=10)

    receipt_text = Text(receipt_window, bg='#101719', fg='white', font=("Arial", 15), wrap=WORD)
    receipt_text.pack(fill=BOTH, expand=True, padx=10, pady=10)

    receipt_text.tag_configure("center", justify='center')
    receipt_text.insert(END, "Computer Shop\n", "center")
    receipt_text.insert(END, "09053928374\n", "center")
    receipt_text.insert(END, "IT COMPANY\n", "center")
    receipt_text.insert(END, "----------------------------------------------\n")
    total_price = 0
    for item in selected_items:
        receipt_text.insert(END, f"ID: {item['id']}\n")
        receipt_text.insert(END, f"Product: {item['product']}\n")
        receipt_text.insert(END, f"Type: {item['type']}\n")
        receipt_text.insert(END, f"Brand: {item['brand']}\n")
        receipt_text.insert(END, f"Price: {item['price']}\n")
        receipt_text.insert(END, f"Quantity: {item['quantity']}\n")
        receipt_text.insert(END, "----------------------------------------------\n")
        total_price += (float(item['price'].replace("$", "")) * int(item['quantity']))

    receipt_text.insert(END, f"Total Price: ${total_price:.2f}\n")
    receipt_text.insert(END, "Thank you for your purchase!\n")

    receipt_text.config(state=DISABLED)

    Button(receipt_window, text="Close", command=receipt_window.destroy, bg='red', fg='white', font=("Arial", 12, "bold")).pack(pady=10)

# Button to generate receipt
btn_generate = Button(purchase_table_frame, text="Generate Receipt", command=generate_receipt, bg='green', fg='white', font=("Arial", 12, "bold"))
btn_generate.place(relx=0.5, rely=0.88, anchor='center')

# Bind purchasing table button to display purchase table
def purchasing_table_action(event):
    if purchase_table_frame.winfo_ismapped():
        purchase_table_frame.place_forget()
    else:
        purchase_table_frame.place(relx=0.5, rely=0.6, anchor='center', width=800, height=500)
        display_purchase_table(row_table)
        cart_list_frame.place_forget()
        selected_items_frame.place_forget()
        add_product_window.place_forget()
        delete_product_window.place_forget()

purchasing_table_button.bind("<Button-1>", purchasing_table_action)

# ---------

login_window = None  # Variable to track the login window

def open_login_window():
    global login_window
    if login_window is None or not Toplevel.winfo_exists(login_window):  # Check if the window exists
        login_window = Toplevel(main_window)
        login_window.title("Login")
        login_window.configure(bg='#010e38')
        login_window.resizable(False, False)
        login_window.overrideredirect(True)

        login_window.update_idletasks()
        screen_width = login_window.winfo_screenwidth()
        screen_height = login_window.winfo_screenheight()
        window_width = 500
        window_height = 400
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        frame = Frame(login_window, bd=3, relief="solid", padx=10, pady=10, bg='#41566b')
        frame.place(x=0, y=0, relwidth=1, relheight=1)

        Label(frame, text="Login", font=("Arial", 20), fg='White', bg='#41566b').place(x=200, y=20)

        Label(frame, text="Username", font=("Arial", 15), fg='White', bg='#41566b').place(x=100, y=80)
        username_entry = Entry(frame, width=30, bg='#D5DCE0', font=("Arial", 12), justify='center', bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94")
        username_entry.place(x=100, y=110, height=30)

        Label(frame, text="Password", font=("Arial", 15), fg='White', bg='#41566b').place(x=100, y=150)
        password_entry = Entry(frame, width=30, bg='#D5DCE0', font=("Arial", 12), justify='center', bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", show="*")
        password_entry.place(x=100, y=180, height=30)

        forgotpass = Label(frame, text="Forgot Password?", cursor="hand2", font=("Arial", 10), fg='White', bg='#41566b')
        forgotpass.place(x=100, y=210)
        signup = Label(frame, text="Sign Up", font=("Arial", 10), fg='White', bg='#41566b', cursor="hand2")
        signup.place(x=310, y=210)

        def forgotpass_enter():
            forgotpass.config(fg="#D4B0FF")
        def forgotpass_leave():
            forgotpass.config(fg="white")
        def signup_enter():
            signup.config(fg="aqua")
        def signup_leave():
            signup.config(fg="white")
        def signup_action():
            close_login_window()
            close_signup_window()
            open_signup_window()
            show_login.config(text='Back to Login')
        def forgotpass_action():
            close_login_window()
            close_forgot_password_window()
            open_forgot_password_window()
            show_login.config(text='Back to Login')

        forgotpass.bind("<Enter>", lambda event: forgotpass_enter())
        forgotpass.bind("<Leave>", lambda event: forgotpass_leave())
        forgotpass.bind("<Button-1>", lambda event: forgotpass_action())
        signup.bind("<Enter>", lambda event: signup_enter())
        signup.bind("<Leave>", lambda event: signup_leave())
        signup.bind("<Button-1>", lambda event: signup_action())

        def login_action():
            username = username_entry.get()
            password = password_entry.get()
            if not username or not password:
                messagebox.showerror("Error", "All fields are required.")
                close_login_window()
                open_login_window()
            else:
                user_found = next((user for user in users if user["usernamed"] == username and user["passcode"] == password), None)
                if not user_found:
                    messagebox.showerror("Error", "Invalid username or password.")
                    close_login_window()
                    open_login_window()
                else:
                    messagebox.showinfo("Success", "Login successful.")
                    if username == "admin":
                        menu_button.place(x=5, y=5)
                        show_login.place_forget()
                        close_login_window()
                        display_usernow.config(text=f"Current user: {username}")
                        admin_menu()
                    else:
                        bg_label.config(image=bg_image2)
                        cart_frame.place(relx=0.2, rely=0.2, anchor='center', width=250, height=50)
                        purchasing_list_frame.place(relx=0.5, rely=0.2, anchor='center', width=250, height=50)
                        purchasing_table_frame.place(relx=0.8, rely=0.2, anchor='center', width=250, height=50)
                        title_label.config(text='Computer Shop', fg='#101719', bg='#39c8b1')
                        display_usernow.config(text=f"Current user: {username}")
                        menu_button.place(x=5, y=5)
                        admin_menu()
                        show_login.place_forget()
                        close_login_window()

        login_b = Button(frame, text="Login", command=login_action, bg='green', fg='white', font=("Arial", 12, "bold"))
        login_b.place(x=180, y=260, height=30, width=100)

        def login_enter():
            login_b.config(bg="darkgreen")
        def login_leave():
            login_b.config(bg="green")

        login_b.bind("<Enter>", lambda event: login_enter())
        login_b.bind("<Leave>", lambda event: login_leave())

def close_login_window():
    global login_window
    if login_window is not None:
        login_window.destroy()
        login_window = None  # Reset the variable when the window is closed

signup_window = None  # Variable to track the signup window

def open_signup_window():
    global signup_window
    if signup_window is None or not Toplevel.winfo_exists(signup_window):  # Check if the window exists
        signup_window = Toplevel(main_window)
        signup_window.title("Sign Up")
        signup_window.configure(bg='#010e38')
        signup_window.resizable(False, False)
        signup_window.overrideredirect(True)

        signup_window.update_idletasks()
        screen_width = signup_window.winfo_screenwidth()
        screen_height = signup_window.winfo_screenheight()
        window_width = 500
        window_height = 400
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        signup_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        frame = Frame(signup_window, bd=3, relief="solid", padx=10, pady=10, bg='#41566b')
        frame.place(x=0, y=0, relwidth=1, relheight=1)

        Label(frame, text="Sign Up", font=("Arial", 20), fg='White', bg='#41566b').place(x=200, y=20)

        Label(frame, text="Username", font=("Arial", 15), fg='White', bg='#41566b').place(x=100, y=80)
        username_entry = Entry(frame, width=30, bg='#D5DCE0', font=("Arial", 12), justify='center', bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94")
        username_entry.place(x=100, y=110, height=30)

        Label(frame, text="Password", font=("Arial", 15), fg='White', bg='#41566b').place(x=100, y=150)
        password_entry = Entry(frame, width=30, bg='#D5DCE0', font=("Arial", 12), justify='center', bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", show="*")
        password_entry.place(x=100, y=180, height=30)

        Label(frame, text="Confirm Password", font=("Arial", 15), fg='White', bg='#41566b').place(x=100, y=220)
        confirm_password_entry = Entry(frame, width=30, bg='#D5DCE0', font=("Arial", 12), justify='center', bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94", show="*")
        confirm_password_entry.place(x=100, y=250, height=30)

        def signup_action():
            input_username = username_entry.get()
            input_password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            if not input_username or not input_password or not confirm_password:
                messagebox.showerror("Error", "All fields are required.")
                close_signup_window()
                open_signup_window()
            elif input_password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match.")
                close_signup_window()
                open_signup_window()
            elif any(user['usernamed'] == input_username for user in users):
                messagebox.showerror("Error", "Username already exists.")
                close_signup_window()
                open_signup_window()
            else:
                add_user(input_username, input_password)
                messagebox.showinfo("Success", "Sign up successful. Please log in.")
                close_signup_window()
                open_login_window()
                show_login.config(text="Close Login")
                    
        signup_b = Button(frame, text="Sign Up", command=signup_action, bg='green', fg='white', font=("Arial", 12, "bold"))
        signup_b.place(x=180, y=300, height=30, width=100)

        backto_login = Label(frame, text="Back to Login", cursor="hand2", font=("Arial", 10, "bold"), fg='White', bg='#41566b')
        backto_login.place(x=180, y=350)

        def signup_enter():
            signup_b.config(bg="darkgreen")
        def signup_leave():
            signup_b.config(bg="green")
        def backto_login_enter():
            backto_login.config(fg="#D4B0FF")
        def backto_login_leave():
            backto_login.config(fg="white")
        def backto_login_action():
            close_signup_window()
            close_login_window()
            open_login_window()
            show_login.config(text="Close Login")

        signup_b.bind("<Enter>", lambda event: signup_enter())
        signup_b.bind("<Leave>", lambda event: signup_leave())
        backto_login.bind("<Enter>", lambda event: backto_login_enter())
        backto_login.bind("<Leave>", lambda event: backto_login_leave())
        backto_login.bind("<Button-1>", lambda event: backto_login_action())

def close_signup_window():
    global signup_window
    if signup_window is not None:
        signup_window.destroy()
        signup_window = None  # Reset the variable when the window is closed

forgot_password_window = None  # Variable to track the forgot password window

def open_forgot_password_window():
    global forgot_password_window
    if forgot_password_window is None or not Toplevel.winfo_exists(forgot_password_window):  # Check if the window exists
        forgot_password_window = Toplevel(main_window)
        forgot_password_window.title("Forgot Password")
        forgot_password_window.configure(bg='#010e38')
        forgot_password_window.resizable(False, False)
        forgot_password_window.overrideredirect(True)

        forgot_password_window.update_idletasks()
        screen_width = forgot_password_window.winfo_screenwidth()
        screen_height = forgot_password_window.winfo_screenheight()
        window_width = 500
        window_height = 300
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        forgot_password_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        frame = Frame(forgot_password_window, bd=3, relief="solid", padx=10, pady=10, bg='#41566b')
        frame.place(x=0, y=0, relwidth=1, relheight=1)

        Label(frame, text="Forgot Password", font=("Arial", 20), fg='White', bg='#41566b').place(x=150, y=20)

        Label(frame, text="Username", font=("Arial", 15), fg='White', bg='#41566b').place(x=100, y=80)
        username_entry = Entry(frame, width=30, bg='#D5DCE0', font=("Arial", 12), justify='center', bd=1, highlightthickness=2, highlightbackground="#3BB6F9", highlightcolor="#005E94")
        username_entry.place(x=100, y=110, height=30)

        def reset_password_action():
            username = username_entry.get()
            if not username:
                messagebox.showerror("Error", "Username is required.")
                close_forgot_password_window()
                open_forgot_password_window()
            else:
                user_found = next((user for user in users if user["usernamed"] == username), None)
            if not user_found:
                messagebox.showerror("Error", "Username does not exist.")
                close_forgot_password_window()
                open_forgot_password_window()
            else:
                messagebox.showinfo("Success", f"Password for {username} is: {user_found['passcode']}")
                close_forgot_password_window()
                close_login_window()
                open_login_window()

        reset_password_b = Button(frame, text="Reset Password", command=reset_password_action, bg='green', fg='white', font=("Arial", 12, "bold"))
        reset_password_b.place(x=180, y=180, height=30, width=150)

        def reset_password_enter():
            reset_password_b.config(bg="darkgreen")
        def reset_password_leave():
            reset_password_b.config(bg="green")

        reset_password_b.bind("<Enter>", lambda event: reset_password_enter())
        reset_password_b.bind("<Leave>", lambda event: reset_password_leave())

        back_to_login = Label(frame, text="Back to Login", cursor="hand2", font=("Arial", 10, "bold"), fg='White', bg='#41566b')
        back_to_login.place(x=200, y=240)

        def back_to_login_enter():
            back_to_login.config(fg="#D4B0FF")
        def back_to_login_leave():
            back_to_login.config(fg="white")
        def back_to_login_action():
            close_forgot_password_window()
            open_login_window()
            show_login.config(text="Close Login")

        back_to_login.bind("<Enter>", lambda event: back_to_login_enter())
        back_to_login.bind("<Leave>", lambda event: back_to_login_leave())
        back_to_login.bind("<Button-1>", lambda event: back_to_login_action())

def close_forgot_password_window():
    global forgot_password_window
    if forgot_password_window is not None:
        forgot_password_window.destroy()
        forgot_password_window = None  # Reset the variable when the window is closed

def iftrueornot():
    if show_login.cget("text") == "Login":
        if login_window is None:
            open_login_window()
            show_login.config(text="Close Login")
    elif show_login.cget("text") == "Close Login":
        close_login_window()
        show_login.config(text="Login")
    elif show_login.cget("text") == "Back to Login":
        close_signup_window()
        close_forgot_password_window()
        open_login_window()
        show_login.config(text="Close Login")

# Add a button to open the login window
show_login = Button(main_window, text="Login", command=iftrueornot, bg='#41566b', fg='#00D3FF', font=("Arial", 14, "bold"), bd=2, relief="solid", cursor="hand2")
show_login.place(x=690, y=130, width=150, height=50)
# show_login.place_forget()
# cart_frame.place(relx=0.2, rely=0.2, anchor='center', width=250, height=50)
# purchasing_list_frame.place(relx=0.5, rely=0.2, anchor='center', width=250, height=50)
# purchasing_table_frame.place(relx=0.8, rely=0.2, anchor='center', width=250, height=50)
# title_label.config(text='Computer Shop', fg='#101719', bg='#39c8b1')
# bg_label.config(image=bg_image2)
# menu_button.place(x=5, y=5)
main_window.mainloop()
