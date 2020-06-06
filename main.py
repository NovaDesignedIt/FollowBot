from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

class InstaBot:
        def __init__(self, username, pw):
               self.username = username
               self.driver = webdriver.Chrome(ChromeDriverManager().install())
               self.driver.get("https://instagram.com")
               sleep(2)                

               self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)

               self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)

               self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()

               sleep(2) 
               self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')\
                .click()
               sleep(2)

        
               
        def homePage(self):
                self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
                        .click()
        
        def following(self):
                self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                        .click() 
        
        def followers(self):
                self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
                        .click() 
                _see_all_followers()

        def close(self):
                self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
                        .click()
                
        def feed(self):
                self.driver.find_element_by_xpath('//a[@href="/"]')\
                        .click()

        def _see_all_followers(self):
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/a')\
                        .click()

        def Not_Now(self):
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
                        .click()

        def _get_names_follower(self):
                sleep(2)
                suggestions = self.driver.find_element_by_xpath('//h4[contains(text(),Suggestions)]')
                self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)
                sleep(1)
                scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
                h1,h2 = 0,1
                while h1 != h2:
                        h1 = h2
                        sleep(1)
                        ht = self.driver.execute_script(""" 
                         arguments[0].scrollTo(0,arguments[0].scrollHeight);
                         return arguments[0].scrollHeight;
                         """, scroll_box)    
                links = scroll_box.find_elements_by_tag_name('a')                    
                names = [name.text for name in links  if name.text != '']
                #close button 
                self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
                        .click()
        
        def _get_names(self):
                sleep(3)
                scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
                h1,h2 = 0,1
                while h1 != h2:
                        h1 = h2
                        sleep(2)
                        ht = self.driver.execute_script(""" 
                                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight;
                                """, scroll_box)  
                        sleep(1)  
                links = scroll_box.find_elements_by_tag_name('a')                    
                names = [name.text for name in links  if name.text != '']
                print(names)
                #close button 
                self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
                        .click()
                return names

        def search(self):
                search = input("Search for >> ")
                self.driver.find_element_by_xpath('//input[@placeholder=\"Search\"]')\
                .send_keys(search)
                sleep(2)
                self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(search))\
                        .click()
                
bot = InstaBot('jpegcrack','Kabuasa1997')
sleep(3)





