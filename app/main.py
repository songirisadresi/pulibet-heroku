from flask import *
from flask_cors import CORS
from flask import Response
import requests
import re
from os.path import exists
from requests.structures import CaseInsensitiveDict

global domain
domain=""


    
app= Flask(__name__)


CORS(app)

def send_static(path):
    return send_from_directory('other', path)
    
'''    
def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results
'''    
    

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
   fname = u_path
   if not fname:
    return send_file("index.html", mimetype='text/html; charset=utf-8')
   if exists("app/"+fname):
    if ".png" in fname:
        return send_file(fname, mimetype='image/png')
    elif ".html" in fname:
        return send_file(fname, mimetype='text/html; charset=utf-8')
    elif ".css" in fname:
        return send_file(fname, mimetype='text/css; charset=utf-8') 
    elif ".xml" in fname:
        return send_file("sitemap.xml", mimetype='application/xml')        
    elif ".js" in fname:
        return send_file(fname, mimetype='text/js; charset=utf-8')   
    elif ".svg" in fname:
        return send_file(fname, mimetype='image/svg+xml')
   else:
        return redirect("app/index.html", code=302)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''if ".html" in fname:
            firma = fname;
            firma = firma.split("-")
            sayi = firma[2]
            firma = firma[3]
            
            
            if firma:
                find = search_string_in_file("firmalist.txt",firma)
                index = find[0][0]
                if index > 0:
                    firmadi = open("firmalist2.txt").readlines()
                    firma = firmadi[index-1]
                    firma = firma.replace("\n","")
                    firmakucuk = find[0][1]
                    firmakucuk = firmakucuk.replace("\n","")
                    sayi = sayi.replace("\n","")
                    temp = open("template.html").read()
                    print(firma+sayi+' | '+firma+' '+sayi+' | '+firma+' Yeni Giriş Adresi')
                    temp = temp.replace("%title",firma+sayi+' | '+firma+' '+sayi+' | '+firma+' Yeni Giriş Adresi')
                    html = open(fname,"w+")
                    html.write(temp)
                    html.close()
                    return firma
                else:
                    return send_file("index.html", mimetype='text/html; charset=utf-8')
            else:
                return send_file("index.html", mimetype='text/html; charset=utf-8')'''
    
    
   