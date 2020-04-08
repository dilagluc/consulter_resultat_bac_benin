#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Desc: Obtenez votre résultat directement en ligne de commande
# Author: https://twitter.com/dilag_luc
                                                                  
import sys,os, datetime
import urllib2,wget,ClientForm
from PIL import Image
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
class cli_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def response(url):
    response=urllib2.urlopen(urllib2.Request(url))
    forms = ClientForm.ParseResponse(response)
    response.close()
    form =forms[1]
    #print form
    nt=raw_input("Numéro de table : ")
    form["id_table"]=nt
    year=raw_input("Année d'obtention : ")
    form["annee"]=[year]
    #request2= form.click()
    response2=urllib2.urlopen(form.click())
    return urllib2.urlopen(response2.geturl())
    
def sysout(output=''):
    sys.stdout.write(output + '\n')
    
def showIm(url):
    p=wget.download(url)
    img = Image.open(p)
    img.show()
    os.remove(p)
    
def case(search):
    cas = []
    for i in range(len(search)):
        hh=search[i].string
        cas.append(hh)
    return cas 

url="http://www.officedubacbenin.bj/site/spip.php?page=resultats_bac2"
document = response (url)
bs=BeautifulSoup(document.read(),"lxml")
search=bs.find_all('font')
case= case(search)   
sysout("\n")
sysout(cli_colors.OKBLUE + 'Noms et prénoms\t: ' + '{}'.format(case[1]))
sysout(cli_colors.WARNING + 'Numéro de table\t: ' + '{}'.format(case[2]))
sysout(cli_colors.OKGREEN + 'Série\t\t: ' + '{}'.format(case[3]))
sysout(cli_colors.HEADER + 'Jury\t\t: ' + '{}'.format(case[4]))
sysout(cli_colors.FAIL + 'Décision\t: ' + '{}'.format(case[5]))
sysout(cli_colors.ENDC + 'Lien\t\t: ' + '{}'.format(document.geturl()))
sysout("\nSource: www.officedubacbenin.bj ---- Date : {}".format(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))

hh=bs.find_all('img')
url2="http://www.officedubacbenin.bj"+hh[1]['src']
showIm(url2)
#end
