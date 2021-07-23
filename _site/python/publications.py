#coding=utf-8

import pandas as pd
data = pd.read_excel('../excel/publish_info.xls')
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
                        <li><a href="people.html">People</a></li>
<!--                        <li><a href="research.html">Research</a></li>-->
                        <li class="active"><a href="publications.html">Publications</a></li>
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
               <li><a href="#published">已发表论文</a></li>
""".format(school, expriment, pic_path)
html += tab

##构建发表的论文索引
paper_times = sorted(set(data[data['type'] == 'paper']['time'].reset_index(drop=True).T.to_dict().values()), reverse=True)
index_public = """
                  <li><a class="subhead" href="#{0}"> {0} </a></li>
"""
for time in paper_times:
    html += index_public.format(time)


project_head = """
              <li><a href="#refereed"> 项目和基金</a></li>
"""
html += project_head

##构建项目时间索引
project_times = sorted(set(data[data['type'] == 'project']['time'].reset_index(drop=True).T.to_dict().values()), reverse = True)
index_project = """
              <li><a class="subhead" href="#{0}c"> {0} </a></li>
"""
for time in project_times:
    html += index_project.format(time)

index_end = """
              </ul>
            </div>
            <div class="span8 offset1">
"""
html += index_end

##构建已发表的论文展示结构
publised_selection = """
               <section id="published">
                  <div class="page-header">
                     <h3>已发表论文</h3>
                  </div>
                  {0}
               </section>
               <hr>
"""

publics_paper_time = """
                  <section id="{0}">
                     <h3>{0}</h3>
                     <br/>
                     {1}
                  </section>
                  <hr>
"""

publised_paper = """
                   <div class="row-fluid">
                        <div class="span3">
                           <a href="{0}" class="thumbnail">
                           <img class="publications-thumb" src="{1}" alt="{2}"/>
                           </a>
                        </div>
                        <div class="span9">
                           <h4>{2}</h4>
                           <br/>
                           <p>{3}</p>
                           <a href="{0}">{4}</a>
                        </div>
                     </div>
                     <hr>
"""

whole_publics_paper_time = ""
for time in paper_times:
    items = data[(data['type'] == 'paper') & (data['time'] == time)].reset_index(drop=True).T.to_dict()
    tmp_publised_paper = ""
    for key, value in items.items():
        publish_time = value['time']
        title = value['title']
        paper_web = value['paper_web']
        pic_path = value['pic_path']
        authors = value['authors']
        joural_and_time = value['joural_time']
        tmp_publised_paper += publised_paper.format(paper_web, pic_path, title, authors, joural_and_time)

    whole_publics_paper_time += publics_paper_time.format(time, tmp_publised_paper)

html += (publised_selection.format(whole_publics_paper_time))


project_selection = """
               <section id="refereed">
                  <div class="page-header">
                     <h3>项目和基金</h3>
                  </div>
                  {0}
               </section>
            </div>
         </div>
      </div>
"""

project_time = """
                  <section id="{0}c">
                     <br/>
                     <h3>{0}</h3>
                     <br/>
                     <ol>
                         {1}
                     </ol>
                  </section>
"""
project = """
                        <li class="publication">{0}</li>
"""

whole_project_time = ""
for time in project_times:
    items = data[(data['type'] == 'project') & (data['time'] == time)].reset_index(drop=True).T.to_dict()
    tmp_project = ""
    for key, value in items.items():
        title = value['title']
        tmp_project += project.format(title)
    whole_project_time += project_time.format(time, tmp_project)
html += (project_selection.format(whole_project_time))

end = """
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

html += (end.format(first_web, email, pic_path, address))

f = open('../publications.html', 'w')
f.write(html)
f.close()


