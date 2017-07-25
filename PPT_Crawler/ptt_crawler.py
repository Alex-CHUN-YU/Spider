__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import json
import os
import time

# PPT 爬蟲者
class Crawler(object):

	def  __init__(self):
		# To Disable Warnings In Requests
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		self.session = requests.session()
		# 爬取 PTT
		self.root = "https://www.ptt.cc"
		# 抓取文章時間間隔
		self.sleep_time = 0.4
		# Over 18 agree
		self.session.post("https://www.ptt.cc/ask/over18", data={"yes": "yes"})

	def crawl(self, board = "graduate", start_page = 1, end_page = 1):
		# 使用者想要爬取的頁數
		crawl_range = range(start_page, end_page + 1)
		# 取得所要爬取 board 的所有頁面之 URL
		for board_page_url in self.get_board_pages_url(board, crawl_range):
			res = []
			# 取得頁面每篇文章之 URL
			for board_page_article_url in self.get_board_page_articles_url(board_page_url):
				# 分析每篇文章
				res.append(self.parser_article(board_page_article_url))
				# 休息一下在換下篇文章吧
				time.sleep(self.sleep_time)
			# 每個頁面所有文章，輸出 JSON 格式
			self.ouput_board_page_articles_json(board, res, start_page)
			print("Finish crawl PTT %s %d page " %(board,start_page))
			start_page += 1

	# 取得所要爬取 board 的所有頁面之 URL(Ex:https://www.ptt.cc/bbs/board/index150.html)
	def get_board_pages_url(self, board = None, index_range = None):
		target_page = self.root + "/bbs/" + board + "/index"
		if index_range is not None:
			for index in index_range:
				yield target_page + str(index) + ".html" 
		else:
			# Board Pages Is Not Exist
			pass

	# 取得頁面每篇文章之 URL(Ex:https://www.ptt.cc/bbs/board/M.1075948736.A.56E.html)
	def get_board_page_articles_url(self, page_url = None):
		res = self.session.get(page_url)
		# html.parser or lxml
		soup = BeautifulSoup(res.text, 'html.parser')
		try:
			for article in soup.select('.r-ent'):
				yield self.root + article.select('.title')[0].select('a')[0]['href']
		except Exception as e:
			print(e)
			# Article Is Not Exist
			pass

	# 解析每篇文章所要爬取的部分
	def parser_article(self, article_url = None):
		res = self.session.get(article_url)
		# html.parser or lxml
		soup = BeautifulSoup(res.text, 'html.parser')
		try:
			# Save Article
			article = {}
			# Extract Author
			article['Author'] = soup.select('.article-meta-value')[0].text
			# Extract Title
			article['Title'] = soup.select('.article-meta-value')[2].text
			# Extract Content
			content = ""
			# (# for id)(. for label)
			for tag in soup.select("#main-content")[0]:
				if type(tag) is NavigableString and tag !='\n':
					content += tag
					break
			article["Content"] = content
			# Extract Response Information
			response_list = []
			uppush = 0
			downpush = 0
			nopush = 0
			for response_struct in soup.select(".push"):
				# 跳脫「檔案過大！部分文章無法顯示」的 push class
				#if "warning-box" not in response_struct['class']:
					response_dic = {}
					response_dic["User"]  = response_struct.select(".push-userid")[0].text
					response_dic["Content"] = response_struct.select(".push-content")[0].text.strip(': ')
					response_dic["Vote"]  = response_struct.select(".push-tag")[0].text.strip()
					response_list.append(response_dic)
					if response_dic["Vote"] == "推":
						uppush += 1
					elif response_dic["Vote"] == "噓":
						downpush += 1
					else:
						nopush += 1
			article["Responses"] = response_list
			article["UpPush"] = uppush
			article["DownPush"] = downpush
			article["NoPush"] = nopush
		except Exception as e:
			#print(e)
			print("Analysis %s occur Error" %article_url )
		# Show Result
		return article

	# 輸出 JSON 格式
	def ouput_board_page_articles_json(self, filename = None, res = None, start_page= None):
		if not os.path.exists("PPT_Crawl_Result"):
			os.makedirs("PPT_Crawl_Result")
		with open("PPT_Crawl_Result/" + filename + str(start_page) + ".json" , 'wb') as f:
			f.write(json.dumps(res, indent = 4, ensure_ascii = False).encode('utf-8'))
