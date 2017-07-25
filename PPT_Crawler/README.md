# PPT_Crawler
PPT_Crawler 是一個以 PPT 為爬蟲對象的運用實例。

## 使用方式
Input:</br>
```
1. 執行 main.py
2. 可更改此模版 crawler.crawl(board = 看版, start_page = 抓取起始頁面, end_page = 抓取結束頁面)
3. Ex:crawler.crawl(board = "Beauty", start_page = 2000, end_page = 2005)
```
Output:</br>
PPT_Crawl_Result 資料夾中可看到所爬取的看板頁面，每個頁面的文章都透過 JSON 格式表示
```
輸出格式範例:
[
    {
	"Title": "猜古代美女 (12)",
	"Author": "pcmangood (pcman好)",
	"Content": " 好像那個年代都流行這種髮型\n  ",
	"NoPush": 1,
	"UpPush": 14,
	"DownPush": 0,
	"Responses": [
            {
                "User": "kissahping",
                "Vote": "推",
                "Content": "蕭芳芳"
            },
            {
                "User": "TransXenos",
                "Vote": "推",
                "Content": "真得蠻美的"
            },
            {
                "User": "hsnu98251",
                "Vote": "推",
                "Content": "推芳姨1"
            },
            {
                "User": "inglee",
                "Vote": "推",
                "Content": "方世玉他媽~~"
            },
            {
                "User": "djdotut",
                "Vote": "推",
                "Content": "真的很漂亮"
            },
            {
                "User": "s50342",
                "Vote": "推",
                "Content": "看了這一系列 真的覺得無名的表特都不表特了啦!!  (扭)"
            },
            {
                "User": "geninhuang",
                "Vote": "推",
                "Content": "蕭芳芳"
            },
            {
                "User": "pcmangood",
                "Vote": "推",
                "Content": "因為這裡是批踢踢表特 (？)"
            },
            {
                "User": "hgame",
                "Vote": "推",
                "Content": "苗可秀年輕時也超正的"
            },
            {
                "User": "aquapengu",
                "Vote": "推",
                "Content": "牛的傳人!"
            },
            {
                "User": "Telumendil",
                "Vote": "推",
                "Content": "是阿B喜歡的牛家拳傳人??"
            },
            {
                "User": "pcmangood",
                "Vote": "推",
                "Content": "答對了"
            },
            {
                "User": "causeMX",
                "Vote": "→",
                "Content": "我理髮都去尖東roger阿"
            },
            {
                "User": "ncumango",
                "Vote": "推",
                "Content": "蕭芳芳6...60歲了（震驚）"
            },
            {
                "User": "Federeco",
                "Vote": "推",
                "Content": "我好喜歡這個系列喔!"
            }
        ]
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


