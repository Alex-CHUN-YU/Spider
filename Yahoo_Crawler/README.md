# Yahoo_Crawler
Yahoo_Crawler 是一個以 Yahoo 知識家為爬蟲對象的運用實例，由於每次載入頁面不一，故目前爬取頁數無法設定，如有解決方法歡迎來信討論。

## 使用方式
Input:</br>
```
1. 執行 main.py
2. 可更改此模版 crawler.crawl(board = 看版)
3. Ex:crawler.crawl(board = "運動")
```
Output:</br>
Yahoo_Crawl_Result 資料夾中可看到所爬取的看板頁面，每個頁面的文章都透過 JSON 格式表示
```
輸出格式範例:
[
    {
	"Title": "男人腎虛腎虧的治愈方法?",
	"Content": "男人腎虛腎虧的治愈方法",
        "respond": " 腎虛腎虧食療： http://www.man-tw.com \n益腎壯陽膏 \n由淫羊霍、蛇床子、當歸、仙茅、肉蓯蓉、丁香、細辛等組成，具有補腎壯陽、活血通酪的功效。用於陰莖勃起功能障礙，腎虛，陽痿早泄，性功能障礙，中醫辨證屬陽性腎虛者 \n仙靈脾 \n也稱淫羊藿，有補腎壯陽，強筋骨，祛風濕的作用，用於陽痿，婦人宮冷不孕，腎陽虛性高血壓，更年期癥候群，腰膝無力，牙齒松動，頭發脫落以及風濕筋骨疼痛等癥。根據現代研究，仙靈脾主要含有淫羊藿?等，仙靈脾提取液有雄性激素洋作用，能促進精液分泌、降血糖;有提高垂體--腎上腺皮質系統功能的作用，並能促進抗體形成。本品煎湯內服壹日量5克--15克。
    },
	...
]
```

## 開發環境
Python 3.5.2</br>
pip install requests</br>
pip install bs4</br>
pip install json</br>
pip install lxml</br>


