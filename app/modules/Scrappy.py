import openpyxl.workbook
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .drivers.create_driver import create_driver
from selenium.webdriver.common.by import By
import openpyxl

class Scrappy:
    def __init__(self, browser:str, url:str) -> None:
        # Creating list of names
        self.companies_names = []
        # Creating list of values
        self.companies_values = []
        # Validating browser
        browser = browser.strip().lower()
        if browser in ["chrome", "edge", "firefox"]:
            self.driver = create_driver(browser)
            self.driver.get(url)
        else:
            raise ValueError("Invalid Browser")

    # Getting names
    def get_names_of_companies(self):
        # Adding wait to loading page
        wait = WebDriverWait(self.driver, 30)

        # Getting name of companies
        names_companies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mn_merchName")))

        # Adding interator
        for name in names_companies:
            name = name.text.strip()
            if name:
                self.companies_names.append(name)
        return self.companies_names

    # Getting values
    def get_values_of_companies(self):
        # Adding wait to loading page
        wait = WebDriverWait(self.driver, 50)

        # Getting value of companies
        values_companies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mn_rebate")))

        # Adding interator
        for value_companie in values_companies:
            value = value_companie.text.strip()[5:]
            if value:
                value = value.split("\n")[0]
                if " " in value:
                    values_split = value.split(" ")
                    if len(values_split) > 2:
                        value_list = [values_split[-1]]
                        value_split = values_split[-2]
                        value_list.insert(0, value_split)
                        value = " ".join(value_list)

        return self.companies_values

    def generate_plan(self):
        index = 2
        plan = openpyxl.workbook()
        companies = plan["Sheet"]
        companies.title("Companies")
        companies["A1"] = "Names"
        companies["B1"] = "Values"
        for name, value in zip(self.companies_names, self.companies_values):
            companies.cell(column=1, row=index, value=name)
            companies.cell(column=2, row=index, value=value)
            index += 1
        plan.save("companies_infos.xlsx")

if __name__ == "__main__":
    scrap = Scrappy("chrome", "https://www.aadvantageeshopping.com/b____.htm")
    names = scrap.get_names_of_companies()
    values = scrap.get_values_of_companies()

    for name, value in zip(names, values):
        print(f"{name} -> {value}")