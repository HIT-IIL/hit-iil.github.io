#coding=utf-8
import pandas as pd


data = pd.read_excel('../excel/news.xls').reset_index(drop=True).T.to_dict()

#head
html = """
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="utf-8">
      <title>{0}</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="description" content="{0}">
      <meta name="author" content="">
      <!-- Le styles -->
      <link href="css/bootstrap.min.css" rel="stylesheet">
      <link href="css/bootstrap-responsive.min.css" rel="stylesheet">
      <link href="css/theme.css" rel="stylesheet">
   </head>
"""
index_data = pd.read_excel('../excel/index.xls')
head_title = index_data[index_data['type'] == 'head_title'].reset_index(drop=True).T.to_dict()[0]['content']
print(head_title)
html = html.format(head_title)

#生成学校和实验室
item = index_data[index_data['type'] == 'title'].reset_index(drop=True).T.to_dict()[0]
school = item['title']
expriment = item['content']
pic_path = item['pic_path']
print(school, expriment, pic_path)
tab = """
   <body>
      <div class="container">
         <header class="jumbotron subhead" id="overview">
            <img src="{2}">
<!--            <p class="lead"> {0} </p>  -->
<!--            <h1> {1} </h1>  -->
         </header>
         <div class="masthead">
            <div class="navbar">
               <div class="navbar-inner">
                  <div class="container">
                     <ul class="nav">
                        <li class="active"><a href="index.html">Home</a></li>
                        <li><a href="people.html">People</a></li>
<!--                        <li><a href="research.html">Research</a></li>-->
                        <li><a href="publications.html">Publications</a></li>
<!--                        <li><a href="gallery.html">Gallery</a></li>-->
                        <li><a href="news.html">News</a></li>
<!--                        <li><a href="teaching.html">Teaching</a></li>-->
<!--                        <li><a href="contact.html">Contact</a></li>-->
                     </ul>
                  </div>
               </div>
            </div>
         </div>
         <hr>
         <div id="media">
""".format(school, expriment, pic_path)
html += tab

##构建消息体
news_start = """
<div class="row-fluid post_row">
"""

news_main = """
<div class="span6 post">
                  <div class="text">
                     <h5><a href="{0}">{1}</a></h5>
                     <br/>
                     <span class="date">{2}</span>
                  </div>
                  <div class="img">
                     <a href="{0}">
                     <img src="{3}" alt="{1}">
                     </a>
                  </div>
                  <div class="text">
                     <p> {4} </p>
                  </div>
                  <div class="author_box">
                     <h6>{5}</h6>
                  </div>
               </div>
"""

news_end = """
     </div>
"""

j = 0
tmp = ""
for key, value in data.items():
    title = value['title']
    url = value['url']
    pic_path = value['pic_path']
    content = value['content']
    time = value['time']
    author = value['author']
    print(title, url, pic_path, time, content, author)
    if j < 2:
        tmp += news_main.format(url, title, time, pic_path, content, author)
    else:
        j = 0
        html += (news_start + tmp + news_end)
        tmp = news_main.format(url, title, time, pic_path, content, author)
    j += 1

html += (news_start + tmp + news_end)

end = """
  </div>
      </div>
      <footer id="footer">
         <div class="container-fluid">
            <div class="row-fluid">
               <div class="span5">
                  <h3>Contact Information</h3>
                  <p><b>Homepage: </b><a href="{0}">{0}</a></p>
                  <p><b>Email: </b><a href="mailto:{1}">{1}</a></p>
               </div>
               <div class="span2">
                  <a href="/"><img src = "{2}" alt="research-lab-logo"/></a>
               </div>
               <div class="span5">
                  <h3>Address</h3>
                  <p>{3}
                  </p>
                  <!-- <a href="http://maps.google.com/">Show Map</a> -->
               </div>
            </div>
         </div>
      </footer>

      <!-- Javascript files -->
      <script src="js/jquery-1.9.1.min.js"></script>
      <script src="js/bootstrap.min.js"></script>
      <script> $('#main-carousel').carousel(); </script>
   </body>
</html>
"""
item = index_data[index_data['type'] == 'footer'].reset_index(drop=True).T.to_dict()[0]
first_web = item['title']
address = item['content']
email = item['url']
pic_path = item['pic_path']

html += (end.format(first_web, email, pic_path, address))

f = open('../news.html', 'w')
f.write(html)
f.close()
