import os
import json
from helium import *
from pathlib import Path

start_firefox('https://app.bupt.edu.cn/site/ncov/xisudailyup', headless=True)

wait_until(Button('账号登录').exists)

click(S('#username'))
write(os.getenv('USERNAME'))
click(S('#password'))
write(os.getenv('PASSWORD'))
click(Button('账号登录'))

wait_until(Text('除每日填报，午晚检在此填报。').exists)

Path('cookies.txt').write_text(json.dumps(get_driver().get_cookies()))

kill_browser()
