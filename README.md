
## IIL使用介绍  

###重点目录结构：

excel文件夹下面存放的是对应修改网页名的excel文件，注意对于每个excel中都有不可删除的行，列名不能更改，已经做了标记，文件名不可以更改

index.xls: 首页的展示信息，也包含所有网页页眉和页脚的信息，对应生成index.html

news.xls: 新闻的信息，对应news.html

people.xls：人员信息，对应people.html

publis_info.xls: 论文发表和项目信息，对应publications.html


logo文件夹下面存放着logo文件

python文件夹下面存放的是生成不同网页的python脚本

关于图片文件的说明：图片文件在网页中使用的是相对路径，因此在维护excel时，注意也要写清楚相对网页的路径

###使用说明：

直接执行脚本start.sh

bash start.sh

也可以单独执行每一个python脚本，这种方式不建议，有可能导致网页页眉和页脚不一致

###项目实现方式
总体采用字符串拼接的方式实现，没有使用复杂的python报等等，因此对于新手可以快速的构建新的网页，python代码也是浅显易懂
以来的包和python版本

python3.5+

python包：pandas、xlrd

## License

The work is licensed under The MIT License.
