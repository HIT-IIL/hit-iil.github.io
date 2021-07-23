# coding=utf-8

import pandas as pd

data = pd.read_excel('../excel/index.xls')

head_title = data[data['type'] == 'head_title'].reset_index(drop=True).T.to_dict()[0]['content']
print(head_title)

#首页头部title
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
""".format(head_title)

#生成学校和实验室
item = data[data['type'] == 'title'].reset_index(drop=True).T.to_dict()[0]
school = item['title']
expriment = item['content']
pic_path = item['pic_path']
print(school, expriment)
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
         <div class="row-fluid">
            <div class="span12">
               <div id="main-carousel" class="carousel slide">
                  <div class="carousel-inner">
""".format(school, expriment, pic_path)
html += tab

#生成第一个激活页flash
item = data[data['type'] == 'active_img'].reset_index(drop=True).T.to_dict()[0]
pic_content = item['content']
pic_path = item['pic_path']
print(pic_content, pic_path)
active_flu_img = """
                     <div class="item active">
                        <img src="{0}" class="carousel-image" alt="">
                        <div class="carousel-caption">
                           <h4>{1}</h4>
                           <!-- -->
                           <p></p>
                        </div>
                     </div>
""".format(pic_path, pic_content)
html += active_flu_img

#生成后续循环图片
item = data[data['type'] == 'img'].reset_index(drop=True).T.to_dict()
for key, value in item.items():
    pic_content = value['content']
    pic_path = value['pic_path']
    print(pic_path, pic_content)
    flu_img = """
                     <div class="item">
                        <img src="{0}" class="carousel-image" alt="">
                        <div class="carousel-caption">
                           <h4>{1}</h4>
                           <p></p>
                        </div>
                     </div>
    """.format(pic_path, pic_content)
    html += flu_img

div_1 = """
         <a class="left carousel-control" href="#main-carousel" data-slide="prev">‹</a>
                  <a class="right carousel-control" href="#main-carousel" data-slide="next">›</a>
               </div>
            </div>
         </div>
         <hr>
"""
html += div_1

intro = data[data['type'] == 'main_intro'].reset_index(drop=True).T.to_dict()[0]['content']
print(intro)
index_main_tab = """
         <div class="container-fluid">
            <div class="row-fluid marketing">
               <div class="span12">
                  <p>
                     {0}
                  </p>
                  <br/>
               </div>
""".format(intro)
html += index_main_tab

# #生成消息
# item = data[data['type'] == 'news'].reset_index(drop=True).T.to_dict()

# if len(item.keys()) > 0:
#     html += """
#                <div class="row-fluid">
#                   <hr>
#                   <h2 class="centered">最新消息</h2>
#                   <hr>
#                </div>
#     """

# for key, value in item.items():
#     title = value['title']
#     content = value['content']
#     pic_path = value['pic_path']
#     time = value['time']
#     url = value['url']
#     print(title, content, pic_path, time, url)
#     news = """
#         <div class="span4 feature-item">
#                   <h5> <span class="date"> {0} </span> </h5>
#                   <h4 class="feature-heading">
#                      <a href="{1}">
#                      {2}
#                      </a>
#                      <br/>
#                   </h4>
#                   <hr>
#                   <div class="centered">
#                      <a href="{1}">
#                      <img src="{3}" alt=""></a>
#                   </div>
#                   <hr>
#                   <p>
#                      {4} <a href="{1}">here</a>.
#                   </p>
#                   <br/>
#                   <br/>
#                </div>
#     """.format(time, url, title, pic_path, content)
#     html += news

end = """
            </div>
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
# format('first_web', 'email', 'pic_path', 'Room J1615, TIB, No. 92, West Dazhi Street <br> Harbin Institute of Technology, Harbin, China')

item = data[data['type'] == 'footer'].reset_index(drop=True).T.to_dict()[0]
first_web = item['title']
address = item['content']
email = item['url']
pic_path = item['pic_path']

html += (end.format(first_web, email, pic_path, address))

f = open('../index.html', 'w')
f.write(html)
f.close()

