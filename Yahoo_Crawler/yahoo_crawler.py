__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import json
import os
import time
import random

# Yahoo 爬蟲者
class Crawler(object):
	
	def __init__(self):
		self.session = requests.session()
		self.root = 'https://tw.answers.yahoo.com'
		# 抓取頁面的時間間隔
		self.sleep_time = 0.4
		self.start_page = 1
		self.proxy_ips = ['120.27.113.72:8888', '121.8.98.201:9999', '222.92.141.250:80', '123.160.31.71:8080']

	def crawl(self, board = '運動'):
		# 判斷是否為第一頁旗標
		flag = 0
		for board_page_url in self.get_board_pages_url(board):
			while 1:
				if(flag != 0):
					try:
						# 如果有下一頁就會一直尋找下去
						for board_next_page_url in self.get_board_next_page_url(next_page):
							next_page = board_next_page_url
					except Exception as e:
						print(e)
						break
				else:
					next_page = board_page_url
					flag = 1
				res = []
				#print("下一頁" + next_page)
				for board_page_article_url in self.get_board_page_articles_url(next_page):
					res.append(self.parser_article(board_page_article_url))
				if len(res) == 0:
					break
				# 休息一下在換下個頁面吧
				time.sleep(self.sleep_time)
				# 每個頁面所有文章，輸出JSON格式
				self.ouput_board_page_articles_json(board, res, self.start_page)
				print("Finish crawl Yahoo %s %d page " %(board,self.start_page))
				self.start_page += 1

	# 取得所要爬取 board 的所有頁面之 URL(Ex:https://tw.answers.yahoo.com/dir/index?sid=396545018)
	def get_board_pages_url(self, board = None):
		#ip = random.choice(self.proxy_ips)
		#print('Use', ip)
		res = self.session.get(self.root + '/dir/index')#, proxies = {'http': 'http://' + ip})
		soup = BeautifulSoup(res.text, "lxml")
		try:
			for target_board in soup.select('#ya-cat-all')[0].select('a'):
				if target_board.text == board:
					yield self.root + target_board['href']
		except Exception as e:
		# Board Pages Is Not Exist
			print(e)
			pass

	# 取得所要爬取 board 的下一個頁面之 URL(Ex:https://tw.answers.yahoo.com/dir/index/answer?offset=r1496718937%7Er%3A0&sid=396545213&isCategory=1)
	def get_board_next_page_url(self, page_url):
		#ip = random.choice(self.proxy_ips)
		#print('Use', ip)
		res = self.session.get(page_url)#, proxies = {'http': 'http://' + ip})
		# html.parser or lxml
		soup = BeautifulSoup(res.text, 'lxml')
		try:
			for next_page in soup.select('a[href^="/answer?offset"]'):
				yield (self.root + "/dir/index/" + next_page['href'])
		except Exception as e:
			print(e)
			pass
		
	# 取得頁面每篇文章之 URL(Ex:https://tw.answers.yahoo.com/question/index?qid=20170607044528AA3EMXA)
	def get_board_page_articles_url(self, page_url = None):
		res = self.session.get(page_url)
		# html.parser or lxml
		soup = BeautifulSoup(res.text, 'lxml')
		try:
			for article in soup.select('a[href^="/question/index?qid="]'):
				yield self.root + article['href']
		except Exception as e:
			print(e)
			pass
		
	# 解析每篇文章所要爬取的部分
	def parser_article(self, article_url = None):
		res = self.session.get(article_url)
		# html.parser or lxml
		soup = BeautifulSoup(res.text,'lxml')
		try:
			# Save Article
			article = {}
			# Extract Title
			article['Title'] = soup.select('title')[0].text.strip(' | Yahoo奇摩知識+')
			# Extract Conttent
			article['Content'] = soup.select('.ya-q-text')[0].text
			# Extract respond
			article['respond'] = soup.select('.ya-q-full-text')[0].text

		except Exception as e:
			#print(e)
			#print("Analysis %s occur Error" %article_url )
			pass
		# Show Result
		return article

	# 輸出 JSON 格式
	def ouput_board_page_articles_json(self, filename = None, res = None, start_page = None):
		if not os.path.exists("Yahoo_Crawl_Result"):
			os.makedirs("Yahoo_Crawl_Result")
		with open("Yahoo_Crawl_Result/" + filename + str(start_page) +".json" , 'wb') as f:
			f.write(json.dumps(res, indent = 4, ensure_ascii = False).encode('utf-8'))
