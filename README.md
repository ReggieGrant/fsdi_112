open terminal and create a folder to store the project (e.g.Code/SDGKU/blog)
move to folder (make sure you are on tthe right location)
create a virtural environment
install django (pip install django)
save packages into requirements.txt file (pip freeze > requirements.txt)
create the project (django-admin startproject config .)
finish the structure:
-create the static, templates, img, css and js folders
-create the .gitignore, README.md (optional files)
link everthing to the settings.py

# Important notes for DTL - Jinja
{% %} - basic structure for all tags
{% block NAME_OF_THE_BLOCK %}{% endblock %} - portion of code
{% load static %} - load static files
{% extends 'filename' %} - Inheritance through htmls
{% include 'filename' %} - Insert html code into the desired one
{% static 'PATH_FOR_THE_FILE' %} - Load any static file (css, js, img)
{% url 'NAME_OF_THE_URL' %} - Travel through htmls