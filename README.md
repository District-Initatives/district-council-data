致公眾及地區組織：如果你在尋找區議會資料，請下載 master-release.csv.
此專案還在初步階段，資料或不齊存，請給我們的 IT 狗多一點時間搜尋資料。敬請見諒。
你也可以看看 /source-data 和 /raw-data 和 /others 的檔案，可能會有你想找的資料。

To public and district organizations: If you are looking for district council election data, "master-release.csv" is the file you want to download.
This project is in prelimary stage and some of the important data may be missing, please give more time to our IT dogs to develope the project. Thank you.
Also, you may find some useful stuffs in either /source-data, /raw-data or /others

Forewords
====================

If you're reading this file, I'd like to first welcome you to Project Hebb,
a mini-research project under District Initiative Hongkong (DisInit).

The purpose of project is to objectively examine the environment of district
politics in Hongkong through, e.g. statistical analysis and web scraping. The
results will be available to other members of DisInit.

Helps are welcome. Please don't have fear that you're incapable to join this
project if you're a totally newbie to statistics/computer science. I'll provide
tutorials to introduce you to the fundamental knowledge and skills needed. If
you have any question, please feel free to ask me (contact see bottom).

Navigation
====================

/master-release.csv
  * The current release of organized data.
/Scraper
  ./dcdata
  * A scrapy project that gather election data from the internet
  ./excel-parser
  * Excel reader that deal with excel files
/raw-data
  * Contains scraped data. Must be in .json format. Each json file must contains a "districtNum" key.
  ./aggregates.py
  * aggregates all the json files in this folder into the "master-release.csv"
/source-data
  ./excels
  * Contains xls or xlsx files gather from external source
  ./sources.csv
  * Documents related information sources, can be website or resporities, must also record the source for excel files
/others
  * For unclassified stuff


License
====================
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.