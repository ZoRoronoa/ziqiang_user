import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()
#
#
#def main():
from blog.models import Blog
f = open("oldblog.txt", 'r', encoding='utf-8')
#all_data = f.readline()
#print(all_data)
a = 0
for line in f:
    if a == 0:
        title = line
        a = 1
    else:
        content = line
        a = 0
        Blog.objects.create(title=title, content=content)
        #print(Blog.title)



