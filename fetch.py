from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime

restaurants = {
    "Artesano Bakery & Café": "https://www.rit.edu/dining/location/artesano-bakery-cafe",
    "Beanz": "https://www.rit.edu/dining/location/beanz",
    "Ben and Jerry's": "https://www.rit.edu/dining/location/ben-and-jerrys",
    "Brick City Café": "https://www.rit.edu/dining/location/brick-city-cafe",
    "Bytes": "https://www.rit.edu/dining/location/bytes",
    "Café and Market at Crossroads": "https://www.rit.edu/dining/location/cafe-and-market-crossroads",
    "Global Village Cantina & Grille": "https://www.rit.edu/dining/location/cantina-and-grille-global-village",
    "Ctrl Alt DELi": "https://www.rit.edu/dining/location/ctrl-alt-deli",
    "Gracie's": "https://www.rit.edu/dining/location/gracies",
    "Java's": "https://www.rit.edu/dining/location/javas",
    "Loaded Latke": "https://www.rit.edu/dining/location/loaded-latke",
    "Midnight Oil": "https://www.rit.edu/dining/location/midnight-oil",
    "Nathan's Soup & Salad": "https://www.rit.edu/dining/location/nathans-soup-salad",
    "Petals (RIT Inn)": "https://www.rit.edu/dining/location/petals",
    "RITz": "https://www.rit.edu/dining/location/ritz",
    "The College Grind": "https://www.rit.edu/dining/location/college-grind",
    "The Commons": "https://www.rit.edu/dining/location/commons",
    "The Corner Store": "https://www.rit.edu/dining/location/corner-store",
    "The Market at Global Village": "https://www.rit.edu/dining/location/market-global-village"
}


def find_matching_restaurant(abbrev: str) -> str:
    abbrev = abbrev.lower()
    best_match = None

    for key in restaurants:
        lowered_key = key.lower()
        if lowered_key.startswith(abbrev):
            if best_match is None or len(lowered_key) < len(best_match):
                best_match = lowered_key

    if best_match:
        for original_key in restaurants:
            if original_key.lower() == best_match:
                return original_key

    return None


def fetch_hours(restaurant: str):
    url = restaurants[find_matching_restaurant(restaurant)]
    if not url:
        return "Restaurant not found."

    driver = webdriver.Chrome()
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 10)
        
        fixed_height = 1300
        driver.execute_script(f"window.scrollTo(0, {fixed_height});")
        
        day_columns = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "day-column")))
        return extract_hours(day_columns)
    except TimeoutException:
        return "Failed to find hours information."
    finally:
        driver.quit()

def extract_hours(day_columns):
    hours_info = ""
    for column in day_columns:
        day_name = column.find_element(By.CLASS_NAME, "day-name").text.strip()
        day_hours = column.find_element(By.CLASS_NAME, "day-hours").text.strip()
        
        if day_name and day_hours:
            hours_info += f"{day_name}: {day_hours}\n"
    
    return hours_info

def fetch_menus(restaurant):
    restaurant_name = find_matching_restaurant(restaurant)
    if not restaurant_name:
        return "Restaurant not found."

    driver = webdriver.Chrome()
    driver.get("https://www.rit.edu/fa/diningservices/netnutrition/")

    try:
        wait = WebDriverWait(driver, 10)

        restaurant_links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cbo_nn_unitNameLink")))

        for link in restaurant_links:
            if link.text.strip() == restaurant_name:
                link.click()
                break

        today = datetime.datetime.today()
        date_title = today.strftime("%A, %B %d, %Y")
        
        menu_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'menu_link_identifier')))
        menu_link.click()

        menu_items = driver.find_elements(By.XPATH, "//*[@role='treeitem' or contains(@class, 'cbo_nn_itemHover')]")
        menu_text = [item.text for item in menu_items]

        return '\n'.join(menu_text)

    except TimeoutException:
        return "Failed to find menu information."
    finally:
        driver.quit()