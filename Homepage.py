import customtkinter, os, time
from tkinter import messagebox
from PIL import Image
from Utilities import Validity_Checker
import main

class Home_page ():
    
    def go_to_location (self):
        get_started.forget()
        location_frame.pack(pady = 20, padx = 60, fill='both', expand = True)
    
    def submit_location (self):
        utility_manager = Validity_Checker()
        if city_txt.get() == "" or province_box.get() == "":
            messagebox.showerror("NULL ERROR", "Error: Enter a valid input.")
        else:
            temp = city_txt.get()
            if (utility_manager.checkCity(temp)):
                global city_input
                city_input = city_txt.get()
                
                temp = province_box.get()
                province_dict = {
                    'Ontario':'ON',
                    'Quebec':'QC',
                    'British Columbia':'BC',
                    'Alberta':'AB',
                    'Manitoba':'MB',
                    'Saskatchewan':'SK',
                    'Nova Scotia':'NS',
                    'Newfoundland and Labrador':'NL',
                    'Northwest Territories':'NT',
                    'Nunavut':'NU',
                    'Prince Edward Island':'PE',
                    'Yukon Territories':'YT'
                }
                global province_input
                province_input = province_dict[temp]
                location_frame.forget()
                recreation_frame.pack(pady = 20, padx = 60, fill='both', expand = True)
            else:
                messagebox.showerror("Invalid City", "Error: Enter a city in Canada.")
    
    def submit_info (self):
        if religion_box.get() == "" or sport_box.get() == "":
            messagebox.showerror("NULL ERROR", "Error: Enter a valid input.")
        else:
            global religion_input
            religion_input = religion_box.get()
            global sport_input
            sport_input = sport_box.get()
            # recreation_frame.forget()
            # root.destroy()
            # main.func(city_input, province_input.lower())
            
    def __init__ (self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        global root
        root = customtkinter.CTk()
        root.geometry("800x600")
        root.title('Workable')
        root.config(bg="#FAF9F6")
        root.resizable(False,False)
        file_path = os.path.dirname(os.path.realpath(__file__))

        global get_started
        get_started = customtkinter.CTkFrame(master=root, fg_color="#FAF9F6")
        get_started.pack(pady = 20, padx = 60, fill= "both", expand = True)

        logo = customtkinter.CTkImage(Image.open(file_path + "/logo.png"), size=(400,400))
        image = customtkinter.CTkLabel(get_started, image=logo, text=" ")
        image.place(x = 150, y = 80)

        get_started_button = customtkinter.CTkButton(master=get_started, text="Get Started", command= self.go_to_location, border_width=1, border_color='black')
        get_started_button.place(x = 275, y = 300)

        global location_frame
        location_frame = customtkinter.CTkFrame(root, fg_color='#FAF9F6')
        location_lbl = customtkinter.CTkLabel(location_frame, text="Please Enter Your Location", bg_color ='blue', text_color= "#FFBD59", fg_color="#FAF9F6", width=200, height=50, font=('Modern', 35, 'bold'))
        location_lbl.place(x=120, y=80)
        global city_txt
        city_txt = customtkinter.CTkEntry(location_frame, placeholder_text="Enter Your City: ", text_color="black", width = 250, height = 50, font=('Modern', 15, 'bold'), fg_color='white')
        city_txt.place(x=50,y=175)
        provinces=["Provinces", "Ontario", "Alberta", "Quebec", "Manitoba", "Saskatchewan", "British Columbia", "Nova Scotia", "Prince Edward Island", "New Brunswick", 'Newfoundland and Labrador', "Yukon Terroritories", "Northwest Territories", 'Nunavut']
        global province_box
        province_box = customtkinter.CTkComboBox(location_frame,values=provinces, fg_color='#FAF9F6', text_color='black', dropdown_fg_color='#FAF9F6', dropdown_hover_color='blue', dropdown_text_color='#FAF9F6', width=275, height=50, state='readonly')
        province_box.place(x=350, y=175)
        location_button = customtkinter.CTkButton(location_frame, text="Confirm Location", command=self.submit_location)
        location_button.place(x=250, y=250)

        global recreation_frame
        recreation_frame = customtkinter.CTkFrame(root, fg_color = '#FAF9F6')
        recreation_lbl = customtkinter.CTkLabel(recreation_frame, bg_color = 'blue', text="Please Enter The Information: ", text_color='#FFBD59', fg_color='#FAF9F6', width=200, height=50, font=('Modern', 35, 'bold'))
        recreation_lbl.place(x=120,y=80)
        religions = ['Hinduism', 'Islam', 'Christianity', 'Judaism', 'Sikkhism']
        
        global religion_box
        religion_box = customtkinter.CTkComboBox(recreation_frame, values=religions, fg_color='#FAF9F6', text_color='black', dropdown_fg_color='#FAF9F6', dropdown_hover_color='blue', dropdown_text_color='#FAF9F6', width=275, height=50, state='readonly')
        religion_box.place(x=50, y=175)
        sports = ['Soccer', 'Football', 'Basketball', 'Cricket', 'Baseball', 'Rugby']
        
        global sport_box
        sport_box = customtkinter.CTkComboBox(recreation_frame, values=sports,fg_color='#FAF9F6', text_color='black', dropdown_fg_color='#FAF9F6', dropdown_hover_color='blue', dropdown_text_color='#FAF9F6', width=275, height=50, state='readonly')
        sport_box.place(x=350, y=175)
        submit_recreation = customtkinter.CTkButton(recreation_frame, text='Click to find Jobs and Housing near your area', command=self.submit_info)
        submit_recreation.place(x=150,y=250)

        time.sleep(4)
        root.mainloop()

Home_page()
main.func(city_input, province_input.lower())