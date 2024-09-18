import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置 Edge 浏览器驱动
service = Service(executable_path='msedgedriver.exe')
driver = webdriver.Edge(service=service)
# number = 0

try:
    driver.start_client()
    driver.get("https://wj.qq.com/s2/15350207/5331/")

    # 第一题 单选题
    option_1 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='是']"))
    )
    # start_time = time.perf_counter()
    option_1.click()
    # number += 1

    # 第二题 图片选择题
    option_1 = driver.find_element(By.XPATH, "//p[text()='C']")
    option_1.click()
    # number += 1

    # 第三题 单选题
    option_1 = driver.find_element(By.XPATH, "//p[text()='222']")
    option_1.click()
    # number += 1

    # 第四题 多级联动题
    option_1 = driver.find_element(By.XPATH, "//span[text()='电饭锅']")
    option_1.click()
    option_1 = driver.find_element(By.XPATH, "//span[text()='瓦尔哈拉']")
    option_1.click()
    option_1 = driver.find_element(By.XPATH, "//span[text()='二万人']")
    option_1.click()
    # number += 1

    # 第五题 填空题
    input_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入地名']")
    input_field.send_keys("欧洲")
    # number += 1

    # 第六题 多级联动题
    option_1 = driver.find_element(By.XPATH, "//span[text()='欧克']")
    option_1.click()
    option_1 = driver.find_element(By.XPATH, "//span[text()='风格化']")
    option_1.click()
    # number += 1

    # 第七题 填空题
    input_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入中文']")
    input_field.send_keys("不知道")
    # number += 1

    # 第八题 单选题
    option_1 = driver.find_element(By.XPATH, "//p[text()='大学本科']")
    option_1.click()
    # number += 1

    # 选择同意协议
    check_box = driver.find_element(By.CLASS_NAME, "t-checkbox__input")
    check_box.click()

    # 提交问卷
    submit_button = driver.find_element(By.CLASS_NAME, "btn-submit")
    submit_button.click()

    # end_time = time.perf_counter()
    # elapsed_time = end_time - start_time
    # print(f"脚本运行时间: {elapsed_time} 秒")

# except :
#     print(f"执行错误{number}")
# else:
#     print("成功")

finally:
    time.sleep(3)
    driver.quit()