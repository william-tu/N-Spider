# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute(['scrapy','crawlall'])

execute(['scrapy','crawl','zhihu'])
#execute(['scrapy','crawl','douban'])
#execute(['scrapy','crawl','guoke'])
