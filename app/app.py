from modules.Scrappy import Scrappy
from utils.utils import clear
from time import sleep

class Main:
    def __init__(self, browser:str, url: str) -> None:
        self.scrappy = Scrappy(browser, url)

    def menu(self) -> None:
        self.banner()
        print("[1] Start Scrappy")
        print("[2] Install Drivers")
        print("[3] Exit")


    def banner(self) -> None:
        clear()
        print(r"""
  _________                                               
 /   _____/ ________________  ______ ______   ___________ 
 \_____  \_/ ___\_  __ \__  \ \____ \\____ \_/ __ \_  __ \
 /        \  \___|  | \// __ \|  |_> >  |_> >  ___/|  | \/
/_______  /\___  >__|  (____  /   __/|   __/ \___  >__|   
        \/     \/           \/|__|   |__|        \/           
                                    𝘣𝘺 𝘍𝘦𝘭𝘪𝘱𝘦 𝘊𝘭𝘢𝘳𝘪𝘯𝘥𝘰""")
    
    def run(self) -> None:
        try:
            exit = False
            while not exit:
                self.banner()
                input("PRESS ENTER TO CONTINUE...")
                self.menu()
                choice = input("Choice one option: ")
                match choice:
                    case "1":
                        self.banner()
                        print("Starting Scrapper...")
                        sleep(1)
                    case "2":
                        pass
                    case "3":
                        self.banner()
                        confirm = str(input("Do you want exit to the program? [Yes/No]"))
                        if confirm.lower() == "yes":
                            exit = True
                    case _:
                        print("Invalid option, Choose another option.")
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        finally:
            if exit:
                self.banner()
                print("Finish Program!")
            else:
                self.banner()
                input("PRESS ENTER TO CONTINUE...")
                
                

if __name__ == "__main__":
    main = Main("chrome", "https://www.aadvantageeshopping.com/b____.htm")
    main.run()
