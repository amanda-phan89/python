#!/usr/local/bin/python3

"""
command start local server: python -m http.server --cgi 8080
"""
import cgitb
import cgi
import os
cgitb.enable() #This will show any errors on your web
print("Content-Type: text/html;charset=utf-8")    # HTML is following
print()                             # blank line, end of headers

form = cgi.FieldStorage()
if os.environ['REQUEST_METHOD'] == 'GET':
    searchTerm = form.getvalue('searchbox')
    print("<pre>")
    print(searchTerm)
    print("</pre>")
elif os.environ['REQUEST_METHOD'] == 'POST':
    postValue = form.getvalue('postname')
    print("<pre>")
    print(postValue)
    print("</pre>")
