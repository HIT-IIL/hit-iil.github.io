# coding=utf-8

import pandas as pd

data = pd.read_excel('../excel/people.xls')

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
                        <li><a href="index.html">Home</a></li>
                        <li class="active"><a href="people.html">People</a></li>
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
         <div class="row-fluid">
            <div class="span3 bs-docs-sidebar" id="navparent">
               <ul class="nav nav-list bs-docs-sidenav" data-spy="affix" data-offset-top="200" data-offset-bottom="260">
                  <li><a href="#principalinvestigator"> 实验室老师 </a></li>
                  <li><a href="#docter"> 博士研究生 </a></li>
                  <li><a href="#graduate">硕士研究生</a></li>
                  <li><a href="#undergraduate">本科生</a></li>
               </ul>
            </div>
            <div class="span8 offset1">
               <section id="principalinvestigator">
                  <div class="page-header">
                     <h3>实验室老师</h3>
                  </div>
""".format(school, expriment, pic_path)
html += tab

##老师信息
teacher = """
                  <div class="row-fluid">
                     <div class="span3">
                        <a href="{0}" class="thumbnail">
                        <img src="{1}" alt="{2}"/>
                        </a>
                     </div>
                     <div class="span9">
                        <h4>{2}</h4>
                        <p>{3}</p>
                        <p>{4}</p>
                        <p><b>Phone: </b>{5} </p>
                        <p><b>Email: </b><a href="mailto:{6}">{6}</a></p>
                        <p><b>Address: </b>{7}</p>
                        <p><b>{8}</b></p>
                     </div>
                  </div>
                  <hr>
"""
item = data[data['type'] == 'teacher'].reset_index(drop=True).T.to_dict()
for key, value in item.items():
       personal_web = value['personal_web']
       pic_path = value['pic_path']
       name = value['name']
       title = value['title']
       intro = value['intro']
       phone = value['phone']
       email = value['email']
       address = value['address']
       direction = value['direction']
       print(personal_web, pic_path, name, title, intro, phone, email, address, direction)
       html += teacher.format(personal_web, pic_path, name, title, intro, phone, email, address, direction)

docter_head = """
               </section>
               <hr>
               <section id="docter">
                  <div class="page-header">
                     <h3>博士研究生</h3>
                  </div>
"""
html += docter_head

##添加博士信息
docter = """
<div class="row-fluid">
                     <div class="span3">
                        <a href="{0}" class="thumbnail">
                        <img src="{1}" alt="{2}"/>
                        </a>
                     </div>
                     <div class="span9">
                        <h4><a href="{0}">{2}</a></h4>
                        <p>{3}</p>
                        <p><b>Email: </b><a href="mailto:{4}">{4}</a></p>
                        <p><b>Address: </b>{5}</p>
                     </div>
                  </div>
                  <hr>
"""
item = data[data['type'] == 'phd'].reset_index(drop=True).T.to_dict()
for key, value in item.items():
       personal_web = value['personal_web']
       pic_path = value['pic_path']
       name = value['name']
       title = value['title']
       intro = value['intro']
       phone = value['phone']
       email = value['email']
       address = value['address']
       direction = value['direction']
       print(personal_web, pic_path, name, intro, email, address)
       html += docter.format(personal_web, pic_path, name, intro, email, address)

graduate_head = """
             </section>
               <hr>
               <section id="graduate">
                  <div class="page-header">
                     <h3>硕士研究生</h3>
                  </div>
"""
html += graduate_head
##添加硕士信息
item = data[data['type'] == 'graduate'].reset_index(drop=True).T.to_dict()
for key, value in item.items():
       personal_web = value['personal_web']
       pic_path = value['pic_path']
       name = value['name']
       title = value['title']
       intro = value['intro']
       phone = value['phone']
       email = value['email']
       address = value['address']
       direction = value['direction']
       print(personal_web, pic_path, name, intro, email, address)
       html += docter.format(personal_web, pic_path, name, intro, email, address)

undergraduate_head = """
            </section>
               <hr>
               <section id="undergraduate">
                  <div class="page-header">
                     <h3>本科生</h3>
                  </div>
"""
html += undergraduate_head
##添加本科生信息
item = data[data['type'] == 'undergraduate'].reset_index(drop=True).T.to_dict()
for key, value in item.items():
       personal_web = value['personal_web']
       pic_path = value['pic_path']
       name = value['name']
       title = value['title']
       intro = value['intro']
       phone = value['phone']
       email = value['email']
       address = value['address']
       direction = value['direction']
       print(personal_web, pic_path, name, intro, email, address)
       html += docter.format(personal_web, pic_path, name, intro, email, address)


foot = """
</section>
            </div>
         </div>
      </div>
      <div class="container">
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
      </div>

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

html += (foot.format(first_web, email, pic_path, address))

f = open("../people.html", 'w')
f.write(html)
f.close()