from selenium.webdriver.support.wait import WebDriverWait
import datetime
from selenium.webdriver.common.by import By


def test_ssr_speed(driver, counts: int) -> None:
    # try:
    lst = {"dynamic": [], "static": []}
    for test in range(counts):
        driver.get("http://localhost:3000/")
        el = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.ID, "vue-btn"))
        start = datetime.datetime.now()
        el.click()
        WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CLASS_NAME, "v-card__title"))
        end = datetime.datetime.now()
        res = end - start
        lst["dynamic"].append(res.microseconds)
        # print("SSR dynamic data mode:", res)

    for test in range(counts):
        driver.get("http://localhost:3000/")
        el = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.ID, "vue-btn2"))
        start = datetime.datetime.now()
        el.click()
        WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CLASS_NAME, "placer"))
        end = datetime.datetime.now()
        res = end - start
        lst["static"].append(res.microseconds)
        # print("SSR static data mode:", res)
    print("SSR:", lst)
    # except Exception as e:
    #     print(e)
    # finally:
    #     driver.quit()


def test_router_speed(driver, counts: int) -> None:
    # try:
    lst = {"dynamic": [], "static": []}
    for test in range(counts):
        driver.get("http://localhost:5500/")
        el = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.ID, "vue-btn"))
        start = datetime.datetime.now()
        el.click()
        WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CLASS_NAME, "v-card__title"))
        end = datetime.datetime.now()
        res = end - start
        lst["dynamic"].append(res.microseconds)
        # print("VUE-ROUTER dynamic data mode:", res)

    for test in range(counts):
        driver.get("http://localhost:5500/")
        el = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.ID, "vue-btn2"))
        start = datetime.datetime.now()
        el.click()
        WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CLASS_NAME, "placer"))
        end = datetime.datetime.now()
        res = end - start
        lst["static"].append(res.microseconds)
        # print("VUE-ROUTER static data mode:", res)
    print("VUE-ROUTER:", lst)
    # except Exception as e:
    #     print(e)
    # finally:
    #     driver.quit()
