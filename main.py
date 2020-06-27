import tkinter as tk
from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self):
        login = str(entry_field1.get())
        pw = str(entry_field2.get())
        self.driver = webdriver.Firefox()
        self.username = login
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(login)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Nie teraz')]")\
            .click()
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        #     .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Nie teraz')]") \
            .click()
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        #     .click()
        sleep(4)

    def get_unfollowers(self):
        username = str(entry_field1.get())
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/"+username+"/following')]") \
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/"+username+"/followers')]") \
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        return not_following_back

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]") \
            .click()
        return names


def phrase_display():
    my_bot = InstaBot()
    message = my_bot.get_unfollowers()
    message_display = tk.Text(master=window, height=10, width=30)
    message_display.grid(column=0, row=5, columnspan=3)
    for x in range(len(message)):
        message_display.insert(tk.END, message[x] + '\n')


window = tk.Tk()

window.title("InstagramSpyBot")

window.geometry("400x400")

window.configure(bg='white')

# LABEL
title = tk.Label(text="", height=3, width=50, bg='white')
title.grid(column=0, row=0, columnspan=3)

# LABEL
title = tk.Label(text="Username:", bg='white')
title.grid(column=0, row=2)

# Entry field
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=2)

# LABEL
title = tk.Label(text="Password:", bg='white')
title.grid(column=0, row=3)

# Entry field
entry_field2 = tk.Entry(show="*")
entry_field2.grid(column=1, row=3)

# BUTTON
button1 = tk.Button(text="Search", command=phrase_display)
button1.grid(column=0, row=4, columnspan=2, padx=10, pady=10)


window.mainloop()
