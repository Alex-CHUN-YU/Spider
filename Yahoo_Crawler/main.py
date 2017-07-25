__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"

from yahoo_crawler import Crawler

def main():
	crawler = Crawler()
	crawler.crawl(board = "運動")

if __name__ == '__main__':
	main()