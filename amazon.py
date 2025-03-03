from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_product_data(url):
    # Set up the Chrome driver
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("--enable-unsafe-swiftshader")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36"
        )

    service = Service("C:\\webdrivers\\chromedriver.exe")  
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "productTitle")))

        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')

        product_title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)

        price = soup.find("span", {"class": "a-price-whole"}).get_text(strip=True)

        return {"product_name": product_title, "price": price}

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.amazon.in/Lenovo-IdeaPad-i5-12450H-Warranty-83ER008DIN/dp/B0CNVH114V/ref=sr_1_1_sspa?crid=2NRS4NECTWJPU&dib=eyJ2IjoiMSJ9.I5mIyDlx6QhpMhd-cuInCZZLKg2OV-A7o9wasSyGTnkf9GUYRGC220iZ2wP1_q0YpJMIWK_CaoaN0EKL-jZu5S0OUME6ZwX7C04dUeVvulMS2xvTH8pYISdlgU3RJltWjzrEBRWuez0ZQZjF_NL7Z9eOq-cn_Q1T5ZUEwsbFsS9VzWnnPhv5uTO_dnGACJyoluGKzJ2_S5hGjJZ2kGUY7GKN5YKFTxOnpJ5fo8yPDd8.WS7q6jDy05q0XeyRNh8RBB4_fefY8nhUaF_Gf2XeLBA&dib_tag=se&keywords=lenovo%2Bideapad%2B3&nsdOptOutParam=true&qid=1740837880&sprefix=lenovo%2Bideapad%2B3%2Caps%2C559&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
    data = scrape_product_data(url)
    print(data)