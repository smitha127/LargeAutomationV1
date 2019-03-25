from LargeAutomationV1.Scrapy import Scrapy
from LargeAutomationV1.config import config

con = config()
scrapy = Scrapy()
scrapy.login(con.session(), con.Headers(), con.credintials())
scrapy.boards(con.session())
s1 = scrapy.scrapyparser(con.session(), scrapy.scrapyparser())
print(s1)

# print()
