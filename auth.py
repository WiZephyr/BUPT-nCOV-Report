import os
import json
from helium import *
from pathlib import Path

start_firefox('https://auth.bupt.edu.cn/authserver/login', headless=True)

wait_until(Button('账号登录').exists)

click(S('#username'))
write(os.getenv('USERNAME'))
click(S('#password'))
write(os.getenv('PASSWORD'))
click(Button('账号登录'))

Path('cookies.txt').write_text(json.dumps(get_driver().get_cookies()))

kill_browser()
