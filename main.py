from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from pathlib import Path

from tests.test_renderers import test_ssr_speed, test_router_speed

BASE_DIR = Path().resolve()
TEST_COUNTS = 10

service = Service(executable_path=str(BASE_DIR / "geckodriver.exe"))
driver = webdriver.Firefox(service=service)

try:
    test_ssr_speed(driver, TEST_COUNTS)
    test_router_speed(driver, TEST_COUNTS)
except Exception as e:
    print(e)
finally:
    driver.quit()
