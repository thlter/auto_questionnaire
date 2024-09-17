from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 指定 msedgedriver.exe 的路径
service = Service(executable_path='msedgedriver.exe')

# 使用 Service 来启动 Edge 浏览器
driver = webdriver.Edge(service=service)

# 打开一个网页
driver.get("https://www.google.com")

# 关闭浏览器
driver.quit()
