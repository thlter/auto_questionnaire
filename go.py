import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置 Edge 浏览器驱动
service = Service(executable_path='msedgedriver.exe')
driver = webdriver.Edge(service=service)

try:
    driver.start_client()
    # start_time = time.perf_counter()
    driver.get("https://wj.qq.com/s2/15350207/5331/")

    # 填空题
    input_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inputs-input"))
    )
    input_field.send_keys("测试员1")

    # 多项单选题
    option_1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='222']"))
    )
    option_1.click()

    # 多级联动题
    link_option = driver.find_element(By.XPATH, "//span[text()='电饭锅']")
    link_option.click()
    link_option = driver.find_element(By.XPATH, "//span[text()='瓦尔哈拉']")
    link_option.click()
    link_option = driver.find_element(By.XPATH, "//span[text()='二万人']")
    link_option.click()

    # 选择同意协议
    check_box = driver.find_element(By.CLASS_NAME, "t-checkbox__input")
    check_box.click()

    submit_button = driver.find_element(By.CLASS_NAME, "btn-submit")
    submit_button.click()

    # end_time = time.perf_counter()
    # elapsed_time = end_time - start_time
    # print(f"脚本运行时间: {elapsed_time} 秒")

# except :
#     print("执行错误")
# else:
#     print("成功")

finally:
    time.sleep(3)
    driver.quit()