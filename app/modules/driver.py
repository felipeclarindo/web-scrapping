# from utils.validations import validate_broser
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.edge.service import Service as ServiceEdge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def create_driver(browser: str) -> webdriver.Remote:
    try:
        # if validate_broser(browser):
            browser = browser.strip().lower()
            if browser == "chrome":
                chrome_service = ServiceChrome()
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--disable-web-security')
                chrome_options.add_argument('--disable-site-isolation-trials')
                chrome_options.add_argument('--ignore-certificate-errors')
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--window-size=1920,1080")
                chrome_options.add_argument('--log-level=3')
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
                return driver
            
            elif browser == "edge":
                edge_service = ServiceEdge()
                edge_options = webdriver.EdgeOptions()
                edge_options.add_argument('--disable-web-security')
                edge_options.add_argument('--disable-site-isolation-trials')
                edge_options.add_argument('--ignore-certificate-errors')
                edge_options.headless = True
                edge_options.add_argument("--window-size=1920,1080")
                edge_options.add_argument('--log-level=3')
                driver = webdriver.Edge(service=edge_service, options=edge_options)
                return driver
            
            elif browser == "firefox":
                firefox_service = ServiceFirefox()
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.set_preference("dom.security.https_only_mode", False)
                firefox_options.set_preference("dom.security.https_only_mode_ever_enabled", False)
                firefox_options.set_preference("network.websocket.allowInsecureFromHTTPS", True)
                firefox_options.set_preference("security.csp.enable", False)
                firefox_options.add_argument('--disable-web-security')
                firefox_options.add_argument('--ignore-certificate-errors')
                firefox_options.add_argument("--headless")
                firefox_options.add_argument("--disable-gpu")
                firefox_options.add_argument("--width=1920")
                firefox_options.add_argument("--height=1080")
                firefox_options.add_argument('--log-level=3')
                driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
                return driver
            else:
                raise Exception("Browser not found")
        # else:
        #     raise Exception("Invalid browser")
    except ValueError as v:
        print(v)
    except Exception as e:
        print(e)
    return ""

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