#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Desc: Obtenez les dernières statistiques du Bénin sur le coronavirus directement en ligne de commande
# Author: https://twitter.com/dilag_luc
                                                                  
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import wget 
from PIL import Image
import ClientForm
from bs4 import BeautifulSoup
import datetime
class cli_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
response=urllib2.urlopen(urllib2.Request("http://www.officedubacbenin.bj/site/spip.php?page=resultats_bac2"))
forms = ClientForm.ParseResponse(response)
response.close()
form =forms[1]
#print form
resultat=raw_input("Numéro de table : ")
form["id_table"]=resultat
re=raw_input("Année d'obtention : ")
form["annee"]=[re]
#request2= form.click()
response2=urllib2.urlopen(form.click())
document= urllib2.urlopen(response2.geturl())
bs=BeautifulSoup(document.read(),"lxml")
search=bs.find_all('font')

def sysout(output=''):
    sys.stdout.write(output + '\n')
    
case = []
for i in range(len(search)):
    hh=search[i].string
    case.append(hh)


sysout("\n")
sysout(cli_colors.OKBLUE + 'Noms et prénoms\t: ' + '{}'.format(case[1]))
sysout(cli_colors.WARNING + 'Numéro de table\t: ' + '{}'.format(case[2]))
sysout(cli_colors.OKGREEN + 'Série\t\t: ' + '{}'.format(case[3]))
sysout(cli_colors.HEADER + 'Jury\t\t: ' + '{}'.format(case[4]))
sysout(cli_colors.FAIL + 'Décision\t: ' + '{}'.format(case[5]))
sysout(cli_colors.ENDC + 'Lien\t\t: ' + '{}'.format(response2.geturl()))
sysout("\nSource: www.officedubacbenin.bj ---- Date : {}".format(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
hh=bs.find_all('img')
url="http://www.officedubacbenin.bj"+hh[1]['src']
p=wget.download(url)

img = Image.open(p)
img.show()
os.remove(p)


#end
