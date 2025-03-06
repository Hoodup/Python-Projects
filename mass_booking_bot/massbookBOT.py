
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import calendar
import re


class Backend:
    def __init__(self):
        self.no = None #webdriver.EdgeOptions()
         #self.no.add_experimental_option('detach', True)
        self.driver = None #webdriver.Edge(options=self.no)

        self.day = None
        self.month = None
        self.booker = None
        self.prayer = None
        self.booking_amount = 100
        print("Hi! this is LaZy, Samuel's friend\n")

        self.starting_mon = None # "January"  # input("What month are we booking from? ").title()
        self.start_day = None # "1"  # input("What day are we starting ")
        self.stopping_month = None # "January"  # input("What month are we booking to? ").title()
        self.stop_day = None # "4"  # input("What day are we stopping? ")
        self.sundayMass = None # "8.00am"  # input("\nWhat mass on sunday (THIS FORMAT: 6.00am/10.00am)? ").lower()
        self.weekdayMass = None # "Morning"  # input("What mass during the week (Morning/evening)? ").title()
        # self.starting_mon = "January"  # input("What month are we booking from? ").title()
        # self.start_day = "1"  # input("What day are we starting ")
        # self.stopping_month = "January"  # input("What month are we booking to? ").title()
        # self.stop_day = "4"  # input("What day are we stopping? ")
        # self.sundayMass = "8.00am"  # input("\nWhat mass on sunday (THIS FORMAT: 6.00am/10.00am)? ").lower()
        # self.weekdayMass = "Morning"  # input("What mass during the week (Morning/evening)? ").title()
        self.auto_login = "yes"  # input("Do you want me to login for you? ").lower()
        self.total_masses_perSession = 0
        self.month_reps = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
            "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
        }

        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November",
                  "December"]

    def login(self):
        self.no = webdriver.EdgeOptions()
        self.no.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=self.no)
        self.driver.get("https://stpaulebutemetta.org/parisheasy/login_e.php?")
        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys("Username.Root")
        password.send_keys("PasswordedEnc", Keys.ENTER)


    def book_a_mass(self, day_num, sunday_mass, weekday_mass):
        # self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")

        # TODO: Check if I am working on the expected working month, If not switch to the next
        trigger = self.driver.find_element(By.ID, value="trigger")
        trigger.click()
        check_mon = self.driver.find_element(By.CSS_SELECTOR, value="tr .title")
        working_title = check_mon.text.split(",")
        if working_title[0] == self.month:
            # TODO: Please create a function for the block of code below for the if statement above.... For a clean code
            # trigger = self.driver.find_element(By.ID, value="trigger")
            # trigger.click()
            days_to_book = self.driver.find_elements(By.CLASS_NAME, value="day")
            jacob = []
            for day_to_book in days_to_book:
                # print(day_to_book.text)
                if day_to_book.text == day_num:
                    print(day_to_book.text)
                    day_to_book.click()
                    time_of_Masses = self.driver.find_elements(By.CSS_SELECTOR, value="#mass option")
                    for n in time_of_Masses:
                        jacob.append(n.text)
                    for time_of_mass in jacob:
                        if time_of_mass == f"Sunday Mass - {sunday_mass}":
                            index = jacob.index(time_of_mass)
                            time_of_Masses[index].click()
                            check_the_date = self.driver.find_element(By.ID, value="buttoner")
                            check_the_date.click()
                            self.fill_booking_form()
                            time.sleep(1)

                            # print(time_of_mass)
                        elif time_of_mass == f"Weekday Mass - {weekday_mass}":
                            index = jacob.index(time_of_mass)
                            time_of_Masses[index].click()
                            print(f"ehen na {time_of_mass} Mass")
                            check_the_date = self.driver.find_element(By.ID, value="buttoner")
                            check_the_date.click()
                            self.fill_booking_form()
                            time.sleep(2)
                    break
        elif working_title[0] != self.month:
            nav_btns = self.driver.find_elements(By.CSS_SELECTOR, value=".headrow .nav")
            nav_btn = nav_btns[2]
            print(nav_btn.text)
            print(self.day, "about to trigger")
            nav_btn.click()
            time.sleep(2)
            print('sleeping')
            self.book_a_mass1(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())

    def book_a_mass1(self, day_num, sunday_mass, weekday_mass):
        # self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
        print(day_num)
        # TODO: Check if i am working on the expected working month, If not switch to the next
        # trigger = self.driver.find_element(By.ID, value="trigger")
        # trigger.click()
        check_mon = self.driver.find_element(By.CSS_SELECTOR, value="tr .title")
        working_title = check_mon.text.split(",")
        if working_title[0] == self.month:
            print(self.month, working_title[0])
            # TODO: Please create a function for the block of code below for the if statement above.... For a clean code
            # trigger = self.driver.find_element(By.ID, value="trigger")
            # trigger.click()
            days_to_book = self.driver.find_elements(By.CLASS_NAME, value="day")

            jacob = []
            for day_to_book in days_to_book:
                # time.sleep(3)
                if day_to_book.text == day_num:

                    print(day_num, f"vs {day_to_book.text}")
                    day_to_book.click()
                    time_of_Masses = self.driver.find_elements(By.CSS_SELECTOR, value="#mass option")
                    for n in time_of_Masses:
                        jacob.append(n.text)                                                #Mrs. Ebere Isabella Egbosionu
                    for time_of_mass in jacob:
                        print(time_of_mass)
                        if time_of_mass == f"Sunday Mass - {sunday_mass}":
                            index = jacob.index(time_of_mass)
                            time_of_Masses[index].click()
                            print("yes. na de mass")
                            check_the_date = self.driver.find_element(By.ID, value="buttoner")
                            check_the_date.click()
                            self.fill_booking_form()
                            time.sleep(1)

                            print(time_of_mass)
                        elif time_of_mass == f"Weekday Mass - {weekday_mass}":
                            index = jacob.index(time_of_mass)
                            time_of_Masses[index].click()
                            print(f"ehen na {time_of_mass} Mass")
                            check_the_date = self.driver.find_element(By.ID, value="buttoner")
                            check_the_date.click()
                            self.fill_booking_form()
                            time.sleep(1)
                    break
        elif working_title[0] != self.month:
            print(self.day, "heading to elso")
            self.elso(day_num=self.day)


    def elso(self, day_num):
        print(self.day, "elso")
        nav_btns = self.driver.find_elements(By.CSS_SELECTOR, value=".headrow .nav")
        print(nav_btns)
        nav_btn = nav_btns[2]
        print(nav_btn.text, f"thils block want to hit {self.day}", day_num)
        nav_btn.click()
        time.sleep(1)
        self.book_a_mass1(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())

    def fill_booking_form(self):
        requested_by = self.driver.find_element(By.ID, value="who")
        requested_by.send_keys(self.booker)
        intention = self.driver.find_element(By.ID, value="intention")
        intention.send_keys(self.prayer)
        amount = self.driver.find_element(By.ID, value="amount")
        amount.send_keys(self.booking_amount)
        add_mass_booking = self.driver.find_element(By.ID, value="button")
        add_mass_booking.click()
        print(f"Mass booked for {self.day}")
        self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
        self.total_masses_perSession += 1

    def time_schedule_form(self, f_month, s_month, startday, stopday, sundaymass, weekdaymass, booker, prayer):
        self.starting_mon = f_month  # "January"  # input("What month are we booking from? ").title()
        self.start_day = startday  # "1"  # input("What day are we starting ")
        self.stopping_month = s_month  # "January"  # input("What month are we booking to? ").title()
        self.stop_day = stopday  # "4"  # input("What day are we stopping? ")
        self.sundayMass = sundaymass  # "8.00am"  # input("\nWhat mass on sunday (THIS FORMAT: 6.00am/10.00am)? ").lower()
        self.weekdayMass = weekdaymass  # "Morning"  # input("What mass during the week (Morning/evening)? ").title()
        self.booker = booker
        self.prayer = prayer
        print(self.starting_mon, self.stopping_month, self.stop_day)

    # --------------------------------------------------------------------------------------------------------------------



    def month_date_list(self, working_month, working_month_digit):
        poster = calendar.month(2024, working_month_digit)
        one = poster.strip()
        two = re.sub(f'{working_month} 2024', '', one)
        three = re.sub('Mo Tu We Th Fr Sa Su', '', two)
        four = three.strip()
        five = re.sub("\n", ' ', four)
        six = list(five.split(" "))
        for i in six:
            if i == "":
                six.remove(i)
        return six

    def printmass(self):
        self.login()
        self.driver.get("https://stpaulebutemetta.org/parisheasy/bookings.php")
        day = self.driver.find_element(By.NAME, value='dday')
        day.send_keys('e')
        months = self.driver.find_elements(By.CSS_SELECTOR, value='#dmonth options')
        year = self.driver.find_element(By.NAME, value='dyear')
        masses = self.driver.find_element(By.CSS_SELECTOR, value='#dmass options')


    def login_passge(self):
        # TODO: Log in Passage
        if self.auto_login == "yes":
            self.login()
            print('login succesful')

            # TODO More than a month
            if self.starting_mon != self.stopping_month:
                for self.month in self.months[self.months.index(self.starting_mon):self.months.index(self.stopping_month) + 1]:
                    days = self.month_date_list(self.month, self.month_reps[self.month])
                    if self.month == self.starting_mon:
                        for self.day in days[days.index(self.start_day):len(days) + 1]:
                            self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
                            self.book_a_mass(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())
                    elif self.month != self.stopping_month and self.month != self.starting_mon:
                        for self.day in days[:]:
                            self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
                            print(self.day, "------------------------")
                            self.book_a_mass(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())
                    elif self.month == self.stopping_month:
                        for self.day in days[:days.index(self.stop_day)+1]:
                            self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
                            self.book_a_mass(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())

            # tODO FOR ONE MONTH
            elif self.starting_mon == self.stopping_month:  # CHECK TO SEE IF IT ENDS IN SSME MONTH
                for self.month in self.months:
                    if self.starting_mon == self.month:  # PICK OUT WHATEVER MONTH IT IS AND WORK WITH IT ALONE
                        print(self.starting_mon)
                        days = self.month_date_list(self.month, self.month_reps[self.month])
                        if self.stop_day == days[-1]:  # TODO cHECK IF THE LAST DAY TO BOOK IS THE LAST DAY OF THAT MONTH
                            for self.day in days[days.index(self.start_day):len(days) + 1]:
                                self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
                                self.book_a_mass(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())

                        # TODO cHECK IF same day mass
                        elif self.stop_day == self.start_day:
                            self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
                            self.book_a_mass(day_num=self.start_day, sunday_mass=self.sundayMass,
                                             weekday_mass=self.weekdayMass.title())
                        # TODO cHECK IF THE LAST DAY TO BOOK IS THE  NOT LAST DAY OF THAT MONTH AND NOT SAME DAY MASS
                        elif self.stop_day != days[-1]:  # cHECK IF THE LAST DAY TO BOOK IS NOT THE LAST DAY OF THAT MONTH
                            for self.day in days[days.index(self.start_day):days.index(self.stop_day) + 1]:
                                self.driver.get("https://stpaulebutemetta.org/parisheasy/addmass.php?")
                                self.book_a_mass(day_num=self.day, sunday_mass=self.sundayMass, weekday_mass=self.weekdayMass.title())

        self.driver.close()
        # elif self.auto_login == "no":
        #     self.driver.close()

        print(f"\n\nAll mass successfully booked: A total of {self.total_masses_perSession} masses Booked ")
        self.total_masses_perSession = 0


# B = Backend()
#
# B.printmass()
