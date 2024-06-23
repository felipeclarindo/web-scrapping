from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

def install_driver(browser:str) -> str:
    try:
        browser = browser.strip().lower()
        if browser:
            if browser == "chrome":
                return ChromeDriverManager().install()
            elif browser == "edge":
                return EdgeChromiumDriverManager().install()
            elif browser == "firefox":
                return GeckoDriverManager().install()
            else:
                raise Exception("Browser not found.")
        else:
            raise Exception("Invalid Browser")
    except Exception as e:
        print(f"Error installing driver: {e}")
    return ""

if __name__ == "__main__":
    pass
