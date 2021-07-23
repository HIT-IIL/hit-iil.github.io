#!/bin/sh
echo "开始处理"
cd $(pwd)
cd python
echo "生成手页～"
python index.py
echo "生成新闻页"
python news.py
echo "生成人员页"
python people.py
echo '生成成果页'
python publications.py