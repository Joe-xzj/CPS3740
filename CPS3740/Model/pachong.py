from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

# 保存文件
COURSE_FILE = "courses.json"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# 打开课程搜索页面（需要已登录才能看到数据）
driver.get("https://selfservice.kean.edu/Student/Courses/Search?keyword=")

# 如果需要登录，需要你手动输入或者使用自动化输入账号密码
# driver.find_element(By.ID, "UserName").send_keys("你的用户名")
# driver.find_element(By.ID, "Password").send_keys("你的密码")
# driver.find_element(By.ID, "LoginButton").click()

# 等待页面加载
time.sleep(5)

# 抓取课程标题
titles_elements = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/section/section/ul/li/div/div/h3/span")

# 获取文本并存入列表
titles = [t.text.strip() for t in titles_elements if t.text.strip()]

# 保存到 JSON 文件
with open(COURSE_FILE, "w", encoding="utf-8") as f:
    json.dump(titles, f, ensure_ascii=False, indent=4)

print(f"已爬取 {len(titles)} 门课程，并保存到 {COURSE_FILE}")

driver.quit()
