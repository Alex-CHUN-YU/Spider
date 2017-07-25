__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"

from ptt_crawler import Crawler

def main():
	crawler = Crawler()
	crawler.crawl(board = "Beauty", start_page = 1, end_page = 4)

if __name__ == '__main__':
	main()