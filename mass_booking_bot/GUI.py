import tkinter
from tkinter import END
from random import randint
import customtkinter as ct
from PIL import Image
from tkinter import messagebox
from massbookBOT import Backend
from datetime import datetime
import os
import pyclip


backend = Backend()
CONTENT_FONT = ()

month_reps = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
    "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November",
               "December"]

# TODO: Button Functions

which = None                  # TODO which mass during the week
sundaymasstime = None         # TODO which mass on sunday


class BotInterface:
    def __init__(self):
        self.start_day = None
        self.stop_day = None
        self.stop_mn = None
        self.start_mn = None
        self.days = None
        self.thePetition = None
        self.keeprunning = True

        ct.set_appearance_mode("dark")
        self.interface = ct.CTk()
        self.interface.title("MASS BOOKING BOT")
        self.interface.geometry("1333x7500")
        TITLE_FONT = ct.CTkFont(family="cambria", size=19, weight="bold")

        # TODO: Left & Right Frame
        self.frame1 = ct.CTkFrame(master=self.interface, height=700, width=400)
        self.frame1.grid(row=0, column=0)

        frame2 = ct.CTkFrame(master=self.interface, height=720, width=800)
        frame2.grid(row=0, column=1)

        # TODO: 3sects in Right Frame
        section1 = ct.CTkFrame(master=frame2, width=1200, height=240, border_width=0, border_color="white")
        section2 = ct.CTkFrame(master=frame2, width=800, height=240)
        section3 = ct.CTkFrame(master=frame2, width=800, height=240)

        section1.grid(row=0, column=0, padx=10, pady=6)
        section2.grid(row=1, column=0, padx=10, pady=6)
        section3.grid(row=2, column=0, padx=10, pady=6)

        # TODO: Images
        self.file = os.listdir("img")
        self.f = randint(1, len(self.file))
        self.my_image = ct.CTkImage(dark_image=Image.open(f"img/{self.f}.jpg"), size=(400, 700))


        # TODO: Labels
        self.image_label = ct.CTkLabel(self.frame1, image=self.my_image, text="")  # display image with a CTkLabel
        # text_label = ct.CTkLabel(master=section1, text="", text_color="white", bg_color="#573752", anchor="w", width=100)
        self.weekdaysLabel = ct.CTkLabel(master=section1, text="WEEKDAYS", width=390, font=TITLE_FONT, anchor="w")
        self.sundayLabel = ct.CTkLabel(section1, text="SUNDAYS", width=390, font=TITLE_FONT, anchor='w')
        dateLabel = ct.CTkLabel(section2, text="DATE", font=TITLE_FONT, anchor="w")
        self.intentionLabel = ct.CTkLabel(section2, text="PRAYER INTENTIONS")
        summaryLabel = ct.CTkLabel(section3, text="SUMMARY", width=100, font=TITLE_FONT)
        sum_nameLabel = ct.CTkLabel(section3, text="Name: ", width=100, anchor="w")
        sum_intentLabel = ct.CTkLabel(section3, text="Intention: ", width=100, anchor="w")
        sum_wdayLabel = ct.CTkLabel(section3, text="Weekday Time: ", width=100, anchor="w")
        sum_sdayLabel = ct.CTkLabel(section3, text="Sunday Time: ", width=100, anchor="w")
        sum_dateLabel = ct.CTkLabel(section3, text="Date:", width=100, anchor="w")

        self.sum_name = ct.CTkLabel(section3, text="")
        self.sum_intent = ct.CTkLabel(section3, text="")
        self.sum_wday = ct.CTkLabel(section3, text="")
        self.sum_sday = ct.CTkLabel(section3, text="")
        self.sum_date = ct.CTkLabel(section3, text=f"START To FINISH", width=600, anchor="w")

        # TODO: Entry
        self.entry = ct.CTkEntry(master=section1, width=800, height=40, text_color="white", font=TITLE_FONT)

        week_Button = ct.CTkSegmentedButton(master=section1, values=["Morning", "Evening"], command=self.morning_evening_button, width=392)

        # TODO: Radio Button
        self.time_variable = tkinter.IntVar(value=0)
        self.am6 = ct.CTkRadioButton(section1, text="6.00am", width=392, variable=self.time_variable, value=1, command=self.sunday_mass_button)
        self.am8 = ct.CTkRadioButton(section1, text="8.00am", width=392, variable=self.time_variable, value=2, command=self.sunday_mass_button)
        self.am10 = ct.CTkRadioButton(section1, text="10.00am", width=392, variable=self.time_variable, value=3, command=self.sunday_mass_button)
        self.pm6 = ct.CTkRadioButton(section1, text="6.00pm", width=392, variable=self.time_variable, value=4, command=self.sunday_mass_button)

        self.prayer_variable = tkinter.IntVar(value=0)
        self.rip = ct.CTkRadioButton(section2, text="Rip", variable=self.prayer_variable, value=1, width=170, command=self.petition_button)
        self.petition = ct.CTkRadioButton(master=section2, text="Petition", variable=self.prayer_variable, value=2, width=170, command=self.petition_button)
        self.thanksgiving = ct.CTkRadioButton(master=section2, text="Thanksgiving", variable=self.prayer_variable,width=170, value=3, command=self.petition_button)
        self.B_thanksgiving = ct.CTkRadioButton(master=section2, text="Birthday Thanksgiving", variable=self.prayer_variable, width=170, value=4, command=self.petition_button)
        self.O_Thanksgiving = ct.CTkRadioButton(master=section2, text="Open Thanksgiving", variable=self.prayer_variable, value=5, width=500, command=self.petition_button)
        self.O_Thanksgiving_Birthday = ct.CTkRadioButton(master=section2, text="Open Thanksgiving(Birthday)", variable=self.prayer_variable, value=8, width=500, command=self.petition_button)
        self.O_Thanksgiving_Anniversary = ct.CTkRadioButton(master=section2, text="Open Thanksgiving(Anniversary)", variable=self.prayer_variable, value=9, width=500, command=self.petition_button)
        self.O_Thanksgiving_Burial = ct.CTkRadioButton(master=section2, text="Open Thanksgiving(successful Burial)", variable=self.prayer_variable, value=6, width=500, command=self.petition_button)
        self.O_Thanksgiving_Wedding = ct.CTkRadioButton(master=section2, text="Open Thanksgiving(Successful Wedding)", variable=self.prayer_variable, value=7, width=500, command=self.petition_button)
        self.O_Thanksgiving_Presentation = ct.CTkRadioButton(master=section2, text="Open Thanksgiving(Child's Presentation)", variable=self.prayer_variable, value=10, width=500, command=self.petition_button)

        # TODO: Drop Downs
        self.from_month_menu = ct.CTkOptionMenu(section2, values=["Start Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                  "December"], command=self.from_date_by_month_button,)
        self.from_day_menu = ct.CTkOptionMenu(section2, values=["Start Days"], command=self.from_date_by_days_button)

        self.to_month_menu = ct.CTkOptionMenu(section2, values=["Stop Month"], command=self.to_date_by_month_button)
        self.to_day_menu = ct.CTkOptionMenu(section2, values=["Stop Day"], command=self.to_date_by_days_button)
        self.yearLabel = ct.CTkLabel(section2, text="2025")

        self.bookMass_button = ct.CTkButton(section3, text="BOOK THE MASS", fg_color="grey", command=self.book_the_mass_function_button, state=tkinter.DISABLED)
        self.summarize_button = ct.CTkButton(section2, text="SUMMARIZE", command=self.summarize_button, )
        self.copy_button = ct.CTkButton(section3, text="copy", width=50, command=self.copy())

        # TODO: Positioning using the grid Placement
        # text_label.grid(row=0, column=0)
        self.entry.grid(row=0, column=0, columnspan=3,pady=4, padx=4)
        self.weekdaysLabel.grid(row=1, column=0, pady=2)
        week_Button.grid(row=2, column=0)

        self.sundayLabel.grid(row=3, column=0, pady=2)
        self.am6.grid(row=4, column=0, padx=0)
        self.am8.grid(row=4, column=1, padx=0)
        self.am10.grid(row=5, column=0, padx=0)
        self.pm6.grid(row=5, column=1, padx=0,pady=10)

        dateLabel.grid(row=0, column=0)
        self.from_month_menu.grid(row=0, column=1)
        self.from_day_menu.grid(row=0, column=2)
        self.yearLabel.grid(row=0, column=3, padx=10)
        dateLabel.grid(row=0, column=0)
        self.to_month_menu.grid(row=1, column=1)
        self.to_day_menu.grid(row=1, column=2)

        self.intentionLabel.grid(row=1, column=0, pady=5, padx=5)
        self.rip.grid(row=2, column=0, pady=5, padx=5)
        self.petition.grid(row=3, column=0, pady=5, padx=5)
        self.thanksgiving.grid(row=4, column=0, pady=5, padx=5)
        self.B_thanksgiving.grid(row=5, column=0, pady=5, padx=5)
        self.O_Thanksgiving.grid(row=2, column=1, pady=5)
        self.O_Thanksgiving_Burial.grid(row=3, column=1, pady=5)
        self.O_Thanksgiving_Wedding.grid(row=4, column=1, pady=5)
        self.O_Thanksgiving_Birthday.grid(row=5, column=1, pady=5)
        self.O_Thanksgiving_Anniversary.grid(row=6, column=1, pady=5)
        self.O_Thanksgiving_Presentation.grid(row=7, column=1, pady=5)

        summaryLabel.grid(row=0, column=0, padx=2)
        sum_nameLabel.grid(row=1, column=0, padx=2)
        sum_intentLabel.grid(row=2, column=0, padx=2)
        sum_wdayLabel.grid(row=3, column=0, padx=2)
        sum_sdayLabel.grid(row=4, column=0, padx=2)
        sum_dateLabel.grid(row=5, column=0, padx=2)

        self.sum_name.grid(row=1, column=1)
        # self.copy_button.grid(row=1, column=2)
        self.sum_intent.grid(row=2, column=1)
        self.sum_wday.grid(row=3, column=1)
        self.sum_sday.grid(row=4, column=1)
        self.sum_date.grid(row=5, column=1)

        self.bookMass_button.grid(row=5, column=4)
        self.summarize_button.grid(row=8, column=2, columnspan=2)

        self.image_label.grid(row=0, column=0)
        # optionmenu.grid(row=2, column=1)

        self.interface.mainloop()

    def morning_evening_button(self, value):
        global which
        which = value

    def sunday_mass_button(self,):
        times = [0, self.am6, self.am8, self.am10, self.pm6]
        time = times[self.time_variable.get()].cget("text")
        global sundaymasstime
        sundaymasstime = time

    def from_date_by_month_button(self, from_month):
        if from_month != 'Start Month':
            self.days = backend.month_date_list(working_month=from_month, working_month_digit=month_reps[from_month])
            self.from_day_menu.configure(values=['Start Days'])
            initial_list_value = self.from_day_menu.cget("values")
            self.from_day_menu.configure(values=initial_list_value+self.days) #add both list[]
            self.start_mn = from_month

        elif from_month == "Start Month":
            self.from_day_menu.configure(values=["Start Month"])


    def from_date_by_days_button(self, day_value):
        if day_value != "Start Days":
            self.to_month_menu.configure(values=["Stop Month"])
            initial_list_value = self.to_month_menu.cget("values")
            self.to_month_menu.configure(values=initial_list_value+months)
            self.start_day = day_value

    def to_date_by_month_button(self, to_month):
        if to_month != "Stop Month":
            self.days = backend.month_date_list(working_month=to_month, working_month_digit=month_reps[to_month])
            self.to_day_menu.configure(values=['Stop Days'])
            initial_list_value = self.to_day_menu.cget("values")
            self.to_day_menu.configure(values=initial_list_value+self.days)  # add both list[]
            self.stop_mn = to_month

    def to_date_by_days_button(self, day_value):
        if day_value != "Stop Days":
            self.stop_day = day_value
        pass

    def petition_button(self,):
        prayers = [0, self.rip, self.petition, self.thanksgiving, self.B_thanksgiving, self.O_Thanksgiving, self.O_Thanksgiving_Burial, self.O_Thanksgiving_Wedding, self.O_Thanksgiving_Birthday, self.O_Thanksgiving_Anniversary, self.O_Thanksgiving_Presentation]
        prayer = prayers[self.prayer_variable.get()]
        self.thePetition = prayer.cget("text")

    def summarize_button(self,):
        must = {self.start_mn: self.from_month_menu.cget("values")[0], self.start_day: self.from_day_menu.cget("values")[0],
                self.stop_day: self.to_day_menu.cget("values")[0], self.stop_mn: self.to_month_menu.cget("values")[0],
                self.thePetition: self.intentionLabel.cget("text"), sundaymasstime: self.sundayLabel.cget("text"),
                which: self.weekdaysLabel.cget("text")
                    }
        requires = [self.stop_day, self.start_mn, self.start_day, self.stop_mn, self.thePetition, which, sundaymasstime]
        for require in requires:
            if require is None:
                messagebox.showerror(message=f"{must[require]} section can't be can't be blank")
                self.keeprunning = False
                break
            else:
                self.keeprunning = True

        value = self.entry.get()  # TODO Holding entry value
        if value == '':
            messagebox.showerror(message=f"Name Space Can't be Blank")
            self.keeprunning = False

        elif self.keeprunning is True:
            self.sum_name.configure(text=value)
            self.copy_button.grid(row=1, column=2)
            self.sum_wday.configure(text=which)
            self.sum_sday.configure(text=sundaymasstime)
            self.sum_intent.configure(text=self.thePetition)
            yr = int(self.yearLabel.cget("text"))
            starrrr = datetime(year=yr, month=month_reps[self.start_mn], day=int(self.start_day))
            stooooo = datetime(year=yr, month=month_reps[self.stop_mn], day=int(self.stop_day))
            START = starrrr.strftime(f"{'%d'}-{'%b'}-{'%Y'}")
            FINISH = stooooo.strftime(f"{'%d'}-{'%b'}-{'%Y'}")
            self.sum_date.configure(text=f"{START} TO {FINISH}")
            self.entry.delete(0, END)
            self.bookMass_button.configure(state=tkinter.NORMAL, fg_color="green", hover_color="#097969", corner_radius=20)
            backend.time_schedule_form(f_month=self.start_mn, s_month=self.stop_mn,
                                       startday=self.start_day, stopday=self.stop_day, sundaymass=sundaymasstime,
                                       weekdaymass=which, booker=value, prayer=self.thePetition)
            self.f = randint(1, len(self.file))
            self.my_image = ct.CTkImage(dark_image=Image.open(f"img/{self.f}.jpg"), size=(400, 700))

            # TODO: Labels
            self.image_label.configure(image=self.my_image)  # display image with a CTkLabel


    def copy(self):
        pass
    #     text = pyclip.copy(self)

    def book_the_mass_function_button(self, ):
        backend.login_passge()
        messagebox.askyesno(message='Mass Booked successfully.\nDo you want to Book another')
        if "yes":
            self.bookMass_button.configure(fg_color="grey", state=tkinter.DISABLED)
        else:
            self.interface.quit()

j = BotInterface()
