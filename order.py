from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options

restaurant_names = {'Midnight Oil', 'Ctrl Alt DELi', 'RITz', 'Petals (RIT Inn)', 'Café and Market at Crossroads', 
                     'Brick City Café', 'The College Grind', 'The Commons', 'Nathan\'s Soup and Salad', 
                     'Artesano Bakery & Café', 'Global Village Cantina & Grille'}
curr_restaurant = ''
url = 'https://ondemand.rit.edu/'

def find_matching_element(options: set, abbrev: str) -> str:
    abbrev = abbrev.lower()
    best_match = None

    for option in options:
        if option.lower().startswith(abbrev):
            if best_match is None or len(option) < len(best_match):
                best_match = option

    if best_match and all(not other.lower().startswith(abbrev) or other == best_match for other in options):
        return best_match

    return None

class OrderManager:
    def __init__(self):
        self.driver = None
        self.curr_restaurant = ''
        self.initialization_successful = self._initialize_driver()

    def _initialize_driver(self) -> bool:
        try:
            options = Options()
            options.headless = False
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(url)
            return True
        except WebDriverException:
            return False

    def new_order(self, order) -> str:
        order = order.lower()
        order = [token.strip() for token in order.split(',')]

        if order[0].startswith('restaurant='):
            restaurant_name = order[0][len('restaurant='):].strip()
            self.curr_restaurant = find_matching_element(set(restaurants.keys()), restaurant_name)
            if not self.curr_restaurant:
                return "Restaurant not found."

        if not self.curr_restaurant:
            return "Please select a restaurant first."

        for item in order[1:]:
            try:
                element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{item}')]")
                button = element.find_element(By.TAG_NAME, 'button')
                button.click()
            except NoSuchElementException:
                return f"Item not found: {item}"

        return "Order processed."

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None