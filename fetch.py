from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import csv
from itertools import zip_longest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
# Converting datetime object to string
iz=0
def err(url,no):
    if no<5:
        try:
            time.sleep(100)
            result = requests.get(url,headers=headers)
            print(result.status_code)
            print('why')
            return result.status_code
        except:
            print("error")
            time.sleep(100)
            return 2
            
    else:
        return 3
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}

acura=['ilx', 'mdx', 'nsx', 'rdx', 'rlx', 'tlx', 'cl', 'ilx-hybrid', 'integra', 'legend', 'rl', 'rsx', 'slx', 'tl', 'tsx', 'tsx-sport-wagon', 'vigor', 'zdx']
hyundai=['accent', 'azera', 'elantra', 'elantra-gt', 'ioniq-electric', 'ioniq-hybrid', 'ioniq-plug-in-hybrid', 'kona', 'kona-electric', 'nexo', 'palisade', 'santa-fe', 'santa-fe-sport', 'santa-fe-xl', 'sonata', 'sonata-hybrid', 'sonata-plug-in-hybrid', 'tucson', 'veloster', 'venue', 'elantra-coupe', 'elantra-touring', 'entourage', 'equus', 'excel', 'genesis', 'genesis-coupe', 'scoupe', 'tiburon', 'veracruz', 'xg300', 'xg350']
kia=['cadenza', 'forte', 'k900', 'niro', 'niro-ev', 'niro-plug-in-hybrid', 'optima', 'optima-hybrid', 'optima-plug-in-hybrid', 'rio', 'sedona', 'seltos', 'sorento', 'soul', 'soul-ev', 'sportage', 'stinger', 'telluride', 'amanti', 'borrego', 'rondo', 'sephia', 'spectra']
mazda=['3', '6', 'cx-3', 'cx-30', 'cx-5', 'cx-9', 'mx-5-miata', 'mx-5-miata-rf', '2', '323', '5', '626', '929', 'b-series', 'b-series-pickup', 'b-series-truck', 'cx-7', 'mazdaspeed-3', 'mazdaspeed-6', 'mazdaspeed-mx-5-miata', 'mazdaspeed-protege', 'millenia', 'mpv', 'mx-3', 'mx-6', 'navajo', 'protege', 'protege5', 'rx-7', 'rx-8', 'tribute', 'tribute-hybrid', 'truck']
nissan=['370z', 'altima', 'armada', 'frontier', 'gt-r', 'kicks', 'leaf', 'maxima', 'murano', 'nv-cargo', 'nv-passenger', 'nv200', 'pathfinder', 'rogue', 'rogue-sport', 'sentra', 'titan', 'titan-xd', 'versa', 'versa-note', '200sx', '240sx', '300zx', '350z', 'altima-hybrid', 'axxess', 'cube', 'juke', 'murano-crosscabriolet', 'nv', 'nx', 'pulsar', 'quest', 'rogue-select', 'stanza', 'truck', 'van', 'xterra']
mitsubishi=['eclipse-cross', 'mirage', 'mirage-g4', 'outlander', 'outlander-phev', 'outlander-sport', '3000gt', 'diamante', 'eclipse', 'eclipse-spyder', 'endeavor', 'expo', 'galant', 'i-miev', 'lancer', 'lancer-evolution', 'lancer-sportback', 'mighty-max-pickup', 'montero', 'montero-sport', 'precis', 'raider', 'sigma', 'vanwagon']
volvo=['s60', 's60-cross-country', 's90', 'v60', 'v60-cross-country', 'v90', 'v90-cross-country', 'xc40', 'xc60', 'xc90', '240', '740', '760', '780', '850', '940', '960', 'c30', 'c70', 'coupe', 's40', 's70', 's80', 'v40', 'v50', 'v70', 'xc', 'xc70']
suzuki=['select-model', 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7', 'select-model', 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7', 'select-model', 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7']

options = Options()
#'coupe','wagon','sedan','hatchback','suv','type-s','32-type-s','hybrid','type-r'}
car_year=[
       '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
       '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'
       ]
options = Options()
 # Last I checked this was necessary.
driver = webdriver.Chrome()
comps=[]
sum=0
ifi=0
companies=['acura','hyundai','kia','mazda','nissan','mitsubishi','volvo','suzuki']
for comp in companies:
       time.sleep(5)
       models=[]
       years=[]
       page_count=0
       review=[]
       heading=[]
       rating=[]
       reviewer=[]
       date=[]
       car_model=eval(comp)

       for model in car_model:
        sum+=1
        print("**************************************"+str(sum)+"*****************************************")
        for year in car_year:
            for i in range(1,5):
                
              url= "https://www.edmunds.com/"+comp+"/"+model+"/"+year+"/consumer-reviews/?pagenum="+str(i)+"&pagesize=50"
              print(page_count)
              page_count+=1
              print(url)
              try:
                 result = requests.get(url,headers=headers)
                 print(result.status_code)
                 ifi=0
              except:
                 print("error")
                 b=err(url,ifi)
                 if b==2:
                     ifi+=1
                     print("try again")
                     b=err(url,ifi)
                 elif b==200:
                     result.status_code=b
                     print("found after sleep")
                 elif b==3:
                     print("skip this, not found")
                     break
              if result.status_code==200:
                driver.get(url)
                time.sleep(1)
                revdate=driver.find_elements_by_xpath("/html/body/div/div/main/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div[1]")
                if revdate==[]:
                      # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$=============next year=============$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                       break
       
                for it in range (1,60):
                        hed=driver.find_elements_by_xpath("/html/body/div/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/h3")
                        revdate=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[1]/div[1]")
                        rev=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[4]")
                        srev=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[4]/div[2]")
                        rat=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/span")

                        if srev==[]:
                               srev=driver.find_elements_by_xpath("/html/body/div/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[4]/div")
                               
                        if revdate==None:
                               iz+=1
                               if iz==5:
                                     # print("This page has been scraped, moving to the next page")
                                      break
                        else:
                            iz=0

                            if len(revdate)!=0:
                                   for redtape in revdate:
                                          if len(redtape.text)!=0:
                                                 if srev==[]:
                                                        #print("how stupid can you be?????????????????????????????????????????????????????????")
                                                        review.append(" ")
                        
                               
                            for hedr in hed:
                                   hedre=hedr.text
                                   heading.append(hedre)
                            for snance in revdate:
                                redat=snance.text
                                reed=redat.split(',')
                                if reed==['']:
                                    print(".")
                                else:
                                    #print("acceptable")
                                    reviewer.append(reed[0])
                                    date.append(reed[1])
                                    models.append(model)
                                    years.append(year)
                                    
                                    
                                           
                            for (jheff,jeff) in zip(srev,rev):
                                revi=jeff.text
                                srevi=jheff.text
                                if revi!=srevi:
                                       rev1 = revi.replace(srevi, '')
                                else:
                                       rev1=revi
                                review.append(rev1)
                            for nyess in rat:
                                boss=nyess.get_attribute('aria-label')
                                rating.append(boss[0])
                                


                print("------------------------sleep----------------------------")
                time.sleep(10)
              else:
                    # print("__________________________________________go to next year____________________________________")
                     break
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            print('Current Timestamp : ', timestampStr)
       d = [models,years,reviewer,date,heading,rating,review]
       export_data = zip_longest(*d, fillvalue = '')
       with open(comp+'.csv', 'w',encoding="utf-8",  newline='') as myfile:
             wr = csv.writer(myfile)
             print("writing")
             wr.writerow(("Model", "Year","Reviewer","Date","Title","Rating","Review"))
             time.sleep(2)
             wr.writerows(export_data)
       myfile.close()              

       print(len(models))
       print(len(years))
       print(len(reviewer))
       print(len(date))
       print(len(rating))
       print(len(review))
       print(len(heading))

driver.quit()
print("done")


