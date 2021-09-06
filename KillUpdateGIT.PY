################################################################
#############Created by PhillyBoi                  #############
#############For RapidOne&SAP Software             #############
#############Build 1.0.4                           #############
################################################################
import os
import requests # pip install requests
import zipfile
import sys
import subprocess
from requests.sessions import dispatch_hook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

#Chromedriver URL, choices, change to cwd path
Durl = 'https://chromedriver.storage.googleapis.com/92.0.4515.43/chromedriver_win32.zip'
chromedriver = requests.get(Durl)
yesChoice = ['y', 'Y', 'ye', 'Ye', 'Yes', 'yes', 'YES', 'YE']
noChoice = ['n', 'N', 'no', 'No', 'Nah', 'nah', 'NAH', 'NO']
FileName = chromedriver.url[Durl.rfind('/')+1:]
path = os.getcwd()

#Download Yes or No and extract from ZIP (Not required if file presant on PC)
print('Made by Philip from RapidOne SupportTeam')
print('Build 1.0.4')
while True:
        DownloadFile = input("Download required files? (Y/N): ").lower()
        if DownloadFile not in yesChoice or noChoice:
            print("Please Enter Valid Input!!")
    
        if DownloadFile in yesChoice:
            with open(FileName, 'wb') as f:
                for chunk in chromedriver.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        print('Downloading...')            

        if DownloadFile in yesChoice:
            with zipfile.ZipFile('chromedriver_win32.zip', 'r') as zip_ref:
                zip_ref.extract('chromedriver.exe')
            print('Extracting...')
            break

        elif DownloadFile in noChoice:
            print('Ok..Skipping.')
            break

#Server Selection for SAP Kill
while True:
    ChooseServer = input("Choose Server: [ROTS1==1, ROTS2==2, ROTS3==3, M4U-IIS==4]:")
    ROTS1 = '1'
    ROTS2 = '2'
    ROTS3 = '3'
    M4U = '4'

#ROTS1 Config
    if ChooseServer in ROTS1:
        ROTS1_LIST = ["CUSTOMER ID:", "All == 0, alevy == 1, amattra == 2, amirg == 3, assutat == 4, baston == 5", "berkoyar == 6, goder == 7, hairm == 8, hanic == 9, heart4u == 10", "idith == 11, idithtest == 12, infinity == 13, koren == 14, kraussclinic == 15", "lifet == 16, liliam == 17, maxia == 18, michaele == 19, miller == 20", "mirih == 21, morom == 22, naderb == 23, olgao == 24, oxypro == 25", "refaelc == 26, refuahvezrah == 27, ro1 == 28, ronia == 29, roniatest == 30", "roron == 31, rots1 == 32, saritd == 33, schein == 34, sharona == 35", "time4s == 36, uvneh == 37,nn yaffac == 38, yosefn == 39"]
        All = '0'
        alevy = '1'
        amattra = '2'
        amirg = '3'
        assutat = '4'
        baston = '5'
        berkoyar = '6'
        goder = '7'
        hairm = '8'
        hanic = '9'
        heart4u = '10'
        idith = '11'
        idithtest = '12'
        infinity = '13'
        koren = '14'
        kraussclinic = '15'
        lifet = '16'
        liliam = '17'
        maxia = '18'
        michaele = '19'
        miller = '20'
        mirih = '21'
        morom = '22'
        naderb = '23'
        olgao = '24'
        oxypro = '25'
        refaelc = '26'
        refuahvezrah = '27'
        ro1 = '28'
        ronia = '29'
        roniatest = '30'
        roron = '31'
        rots1 = '32'
        saritd = '33'
        schein = '34'
        sharona = '35'
        time4s = '36'
        uvneh = '37'
        yaffac = '38'
        yosefn = '39'
        alevy1 = 'alevy'
        amattra1 = 'amattra'
        amirg1 = 'amirg'
        assutat1 = 'assutat'
        baston1 = 'baston'
        berkoyar1 = 'berkoyar'
        goder1 = 'goder'
        hairm1 = 'hairm'
        hanic1 = 'hanic'
        heart4u1 = 'heart4u'
        idith1 = 'idith'
        idithtest1 = 'idithtest'
        infinity1 = 'infinity'
        koren1 = 'koren'
        kraussclinic1 = 'kraussclinic'
        lifet1 = 'lifet'
        liliam1 = 'liliam'
        maxia1 = 'maxia'
        michaele1 = 'michaele'
        miller1 = 'miller'
        mirih1 = 'mirih'
        morom1 = 'morom'
        naderb1 = 'naderb'
        olgao1 = 'olgao'
        oxypro1 = 'oxypro'
        refaelc1 = 'refaelc'
        refuahvezrah1 = 'refuahvezrah'
        ro11 = 'ro1'
        ronia1 = 'ronia'
        roniatest1 = 'roniatest'
        roron1 = 'roron'
        rots11 = 'rots1'
        saritd1 = 'saritd'
        schein1 = 'schein'
        sharona1 = 'sharona'
        time4s1 = 'time4s'
        uvneh1 = 'uvneh'
        yaffac1 = 'yaffac'
        yosefn1 = 'yosefn'
        for item in ROTS1_LIST:
            print(item)
        Customer1 = input("Select Customer ID:")
        if Customer1 in (All):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            KillButton = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/a[1]')
            Do = ActionChains(driver)
            Do.click(KillButton)
            Do.perform()

        if Customer1 in (alevy, amattra, amirg, assutat, baston, berkoyar, goder, hairm, hanic, heart4u, idith, idithtest, infinity, koren, kraussclinic, lifet, liliam, maxia, michaele, miller, mirih, morom, naderb, olgao, oxypro, refaelc, refuahvezrah, ro1, ronia, roniatest, roron, rots1, saritd, schein, sharona, time4s, uvneh, yaffac, yosefn):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            search = driver.find_element_by_xpath('/html/body/div/main/div/div/div[1]/form/p/input[1]')
            if Customer1 in (alevy):
                search.send_keys(alevy1)
            elif Customer1 in (amattra):
                search.send_keys(amattra1)
            elif Customer1 in (amirg):
                search.send_keys(amirg1)
            elif Customer1 in (assutat):
                search.send_keys(assutat1)
            elif Customer1 in (baston):
                search.send_keys(baston1)
            elif Customer1 in (berkoyar):
                search.send_keys(berkoyar1)
            elif Customer1 in (goder):
                search.send_keys(goder1)
            elif Customer1 in (hairm):
                search.send_keys(hairm1)
            elif Customer1 in (hanic):
                search.send_keys(hanic1)
            elif Customer1 in (heart4u):
                search.send_keys(heart4u1)
            elif Customer1 in (idith):
                search.send_keys(idith1)
            elif Customer1 in (idithtest):
                search.send_keys(idithtest1)
            elif Customer1 in (infinity):
                search.send_keys(infinity1)
            elif Customer1 in (koren):
                search.send_keys(koren1)
            elif Customer1 in (kraussclinic):
                search.send_keys(kraussclinic1)
            elif Customer1 in (lifet):
                search.send_keys(lifet1)
            elif Customer1 in (liliam):
                search.send_keys(liliam1)
            elif Customer1 in (maxia):
                search.send_keys(maxia1)
            elif Customer1 in (michaele):
                search.send_keys(michaele1)
            elif Customer1 in (miller):
                search.send_keys(miller1)
            elif Customer1 in (mirih):
                search.send_keys(mirih1)
            elif Customer1 in (morom):
                search.send_keys(morom1)
            elif Customer1 in (naderb):
                search.send_keys(naderb1)
            elif Customer1 in (olgao):
                search.send_keys(olgao1)
            elif Customer1 in (oxypro):
                search.send_keys(oxypro1)
            elif Customer1 in (refaelc):
                search.send_keys(refaelc1)
            elif Customer1 in (refuahvezrah):
                search.send_keys(refuahvezrah1)
            elif Customer1 in (ro1):
                search.send_keys(ro11)
            elif Customer1 in (ronia):
                search.send_keys(ronia1)
            elif Customer1 in (roniatest):
                search.send_keys(roniatest1)
            elif Customer1 in (roron):
                search.send_keys(roron1)
            elif Customer1 in (rots1):
                search.send_keys(rots11)
            elif Customer1 in (saritd):
                search.send_keys(saritd1)
            elif Customer1 in (schein):
                search.send_keys(schein1)
            elif Customer1 in (sharona):
                search.send_keys(sharona1)
            elif Customer1 in (time4s):
                search.send_keys(time4s1)
            elif Customer1 in (uvneh):
                search.send_keys(uvneh1)
            elif Customer1 in (yaffac):
                search.send_keys(yaffac1)
            elif Customer1 in (yosefn):
                search.send_keys(yosefn1)

            search.send_keys(Keys.RETURN)
            sleep(2)
            elem = driver.find_element_by_xpath('/html/body/div/main/div/table/thead/tr/th[1]/input')
            kill = driver.find_element_by_xpath('/html/body/div/main/div/div/div[4]/form/p/input[1]')
            actions = ActionChains(driver)
            actions.click(elem)
            actions.click(kill)
            actions.perform()
            
#ROTS2 Config
    if ChooseServer in ROTS2:
        ROTS2_LIST = ["CUSTOMER ID:", "All == 0, abudi == 1, aradu == 2, avib == 3, babezone == 4, barmeir == 5", "biton ==6, boazo == 7, bodyr == 8, celia == 9, clevermed == 10", "demo == 11, eichut == 12, eidelman == 13, hairclinic == 14, hdi == 15", "heyman == 16, iao == 17, ispa == 18, jbarr == 19, korenm == 20", "lam == 21, langer == 22, marcusb == 23, mauricio == 24, medplus == 25", "mitt == 26, moscona == 27, mydoctor == 28, ocd == 29, oneman == 30", "orenk == 31, perfection == 32, persona == 33, ramac == 34, rivkaz == 34, rosel == 35", "rots2 == 36, sela == 37, shine-mac == 38, talkoren == 39, tanyac == 40", "tautest == 41, theta == 42, tilia == 43, vaknint == 44, websmile == 45, wesmile == 46"]
        All = '0'
        abudi = '1'
        aradu = '2'
        avib = '3'
        babezone = '4'
        barmeir = '5'
        biton = '6'
        boazo = '7'
        bodyr = '8'
        celia = '9'
        clevermed = '10'
        demo = '11'
        eichut = '12'
        eidelman = '13'
        hairclinic = '14'
        hdi = '15'
        heyman = '16'
        iao = '17'
        ispa = '18'
        jbarr = '19'
        korenm = '20'
        lam = '21'
        langer = '22'
        marcusb = '23'
        mauricio = '24'
        medplus = '25'
        mitt = '26'
        moscona = '27'
        mydoctor = '28'
        ocd = '29'
        oneman = '30'
        orenk = '31'
        perfection = '32'
        persona = '33'
        ramac = '34'
        rivkaz = '35'
        rosel = '36'
        rots2 = '37'
        sela = '38'
        shinemac = '39'
        talkoren = '40'
        tanyac = '41'
        tautest = '42'
        theta = '43'
        tilia = '44'
        vaknint = '45'
        websmile = '46'
        wesmile = '47'
        abudi1 = 'abudi'
        aradu1 = 'aradu'
        avib1 = 'avib'
        babezone1 = 'babezone'
        barmeir1 = 'barmeir'
        biton1 = 'biton'
        boazo1 = 'boazo'
        bodyr1 = 'bodyr'
        celia1 = 'celia'
        clevermed1 = 'clevermed'
        demo1 = 'demo'
        eichut1 = 'eichut'
        eidelman1 = 'eidelman'
        hairclinic1 = 'hairclinic'
        hdi1 = 'hdi'
        heyman1 = 'heyman'
        iao1 = 'iao'
        ispa1 = 'ispa'
        jbarr1 = 'jbarr'
        korenm1 = 'korenm'
        lam1 = 'lam'
        langer1 = 'langer'
        marcusb1 = 'marcusb'
        mauricio1 = 'mauricio'
        medplus1 = 'medplus'
        mitt1 = 'mitt'
        moscona1 = 'moscona'
        mydoctor1 = 'mydoctor'
        ocd1 = 'ocd'
        oneman1 = 'oneman'
        orenk1 = 'orenk'
        perfection1 = 'perfection'
        persona1 = 'persona'
        ramac1 = 'ramac'
        rivkaz1 = 'rivkaz'
        rosel1 = 'rosel'
        rots21 = 'rots2'
        sela1 = 'sela'
        shinemac1 = 'shine-mac'
        talkoren1 = 'talkoren'
        tanyac1 = 'tanyac'
        tautest1 = 'tautest'
        theta1 = 'theta'
        tilia1 = 'tilia'
        vaknint1 = 'vaknint'
        websmile1 = 'websmile'
        wesmile1 = 'wesmile'    
        for item in ROTS2_LIST:
            print(item)
        Customer2 = input("Select Customer ID:")
        if Customer2 in (All):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            KillButton = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/a[1]')
            Do = ActionChains(driver)
            Do.click(KillButton)
            Do.perform()
        
        if Customer2 in (abudi, aradu, avib, babezone, barmeir, biton, boazo, bodyr, celia, clevermed, demo, eichut, eidelman, hairclinic, hdi, heyman, iao, ispa, jbarr, korenm, lam, langer, marcusb, mauricio, medplus, mitt, moscona, mydoctor, ocd, oneman, orenk, perfection, persona, ramac, rivkaz, rosel, rots2, sela, shinemac, talkoren, tanyac, tautest, theta, tilia, vaknint, websmile, wesmile):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            search = driver.find_element_by_xpath('/html/body/div/main/div/div/div[1]/form/p/input[1]')
            if Customer2 in (abudi):
                search.send_keys(abudi1)
            elif Customer2 in (aradu):
                search.send_keys(aradu1)
            elif Customer2 in (avib):
                search.send_keys(avib1)
            elif Customer2 in (babezone):
                search.send_keys(babezone1)
            elif Customer2 in (barmeir):
                search.send_keys(barmeir1)
            elif Customer2 in (biton):
                search.send_keys(biton1)
            elif Customer2 in (boazo):
                search.send_keys(boazo1)
            elif Customer2 in (bodyr):
                search.send_keys(bodyr1)
            elif Customer2 in (celia):
                search.send_keys(celia1)
            elif Customer2 in (clevermed):
                search.send_keys(clevermed1)
            elif Customer2 in (demo):
                search.send_keys(demo1)
            elif Customer2 in (eichut):
                search.send_keys(eichut1)
            elif Customer2 in (eidelman):
                search.send_keys(eidelman1)
            elif Customer2 in (hairclinic):
                search.send_keys(hairclinic1)
            elif Customer2 in (hdi):
                search.send_keys(hdi1)
            elif Customer2 in (heyman):
                search.send_keys(heyman1)
            elif Customer2 in (iao):
                search.send_keys(iao1)
            elif Customer2 in (ispa):
                search.send_keys(ispa1)
            elif Customer2 in (jbarr):
                search.send_keys(jbarr1)
            elif Customer2 in (korenm):
                search.send_keys(korenm1)
            elif Customer2 in (lam):
                search.send_keys(lam1)
            elif Customer2 in (langer):
                search.send_keys(langer1)
            elif Customer2 in (marcusb):
                search.send_keys(marcusb1)
            elif Customer2 in (mauricio):
                search.send_keys(mauricio1)
            elif Customer2 in (medplus):
                search.send_keys(medplus1)
            elif Customer2 in (mitt):
                search.send_keys(mitt1)
            elif Customer2 in (moscona):
                search.send_keys(moscona1)
            elif Customer2 in (mydoctor):
                search.send_keys(mydoctor1)
            elif Customer2 in (ocd):
                search.send_keys(ocd1)
            elif Customer2 in (oneman):
                search.send_keys(oneman1)
            elif Customer2 in (orenk):
                search.send_keys(orenk1)
            elif Customer2 in (perfection):
                search.send_keys(perfection1)
            elif Customer2 in (persona):
                search.send_keys(persona1)
            elif Customer2 in (ramac):
                search.send_keys(ramac1)
            elif Customer2 in (rivkaz):
                search.send_keys(rivkaz1)
            elif Customer2 in (rosel):
                search.send_keys(rosel1)
            elif Customer2 in (rots2):
                search.send_keys(rots21)
            elif Customer2 in (sela):
                search.send_keys(sela1)
            elif Customer2 in (shinemac):
                search.send_keys(shinemac1)
            elif Customer2 in (talkoren):
                search.send_keys(talkoren1)
            elif Customer2 in (tanyac):
                search.send_keys(tanyac1)
            elif Customer2 in (tautest):
                search.send_keys(tautest1)
            elif Customer2 in (theta):
                search.send_keys(theta1)
            elif Customer2 in (tilia):
                search.send_keys(tilia1)
            elif Customer2 in (vaknint):
                search.send_keys(vaknint1)
            elif Customer2 in (websmile):
                search.send_keys(websmile1)
            elif Customer2 in (wesmile):
                search.send_keys(wesmile1)

            search.send_keys(Keys.RETURN)
            sleep(2)
            elem = driver.find_element_by_xpath('/html/body/div/main/div/table/thead/tr/th[1]/input')
            kill = driver.find_element_by_xpath('/html/body/div/main/div/div/div[4]/form/p/input[1]')
            actions = ActionChains(driver)
            actions.click(elem)
            actions.click(kill)
            actions.perform()


#ROTS3 Config
    if ChooseServer in ROTS3:
        ROTS3_LIST = ["CUSTOMER ID:", "All == 0, amie == 1, amiri == 2, arikz == 3, asafb == 4, ato == 5", "barlevy == 6 barr == 7 blachash == 8, bodyc == 9, feiner == 10", "doc = 11, doronb = 12, eitamw = 13, eyalt = 14, faceart = 15", "feiner = 16, gabot = 17, galor = 18, garac = 19, garae = 20", "hadas = 21, hadasat = 22, hadtest = 23, hclinic = 24, highdoc = 25", "honey = 26, hwc = 27, ibc = 28, kaplan = 29, kesher = 30", "lbm = 31, limorb = 32, lipo = 33, mamilla = 34, maoz = 35", "marcel = 36, marome = 37, matanis = 38, mayas = 39, mazor = 40", "medassist = 41, meyero = 42, neshai = 43, orenw = 44, orits = 45", "r1test = 46, rbn = 47, rdgw = 48, regev = 49, revitalc = 50", "roqa = 51, roqa2 = 52, rosales = 53, rots3 = 54, sarita = 55", "shahwan = 56, shine = 57, tenecare = 58, tessone = 59, theclinic = 60", "tiratz = 61, yaelh = 62, yoavy = 63, yosefm = 64"]
        All = '0'
        amie = '1'
        amiri= '2'
        arikz = '3'
        asafb = '4'
        ato = '5'
        barlevy = '6'
        barr = '7'
        blachash = '8'
        bodyc = '9'
        feiner = '10'
        doc = '11'
        doronb = '12'
        eitamw = '13'
        eyalt = '14'
        faceart = '15'
        feiner = '16'
        gabot = '17'
        galor = '18'
        garac = '19'
        garae = '20'
        hadas = '21'
        hadasat = '22'
        hadtest = '23'
        hclinic = '24'
        highdoc = '25'
        honey = '26'
        hwc = '27'
        ibc = '28'
        kaplan = '29'
        kesher = '30'
        lbm = '31'
        limorb = '32'
        lipo = '33'
        mamilla = '34'
        maoz = '35'
        marcel = '36'
        marome = '37'
        matanis = '38'
        mayas = '39'
        mazor = '40'
        medassist = '41'
        meyero = '42'
        neshai = '43'
        orenw = '44'
        orits = '45'
        r1test = '46'
        rbn = '47'
        rdgw = '48'
        regev = '49'
        revitalc = '50'
        roqa = '51'
        roqa2 = '52'
        rosales = '53'
        rots3 = '54'
        sarita = '55'
        shahwan = '56'
        shine = '57'
        tenecare = '58'
        tessone = '59'
        theclinic = '60'
        tiratz = '61'
        yaelh = '62'
        yoavy = '63'
        yosefm = '64'
        amie1 = 'amie'
        amiri1 = 'amiri'
        arikz1 = 'arikz'
        asafb1 = 'asafb'
        ato1 = 'ato'
        barlevy1 = 'barlevy'
        barr1 = 'barr'
        blachash1 = 'blachash'
        bodyc1 = 'bodyc'
        feiner1 = 'feiner'
        doc1 = 'doc'
        doronb1 = 'doronb'
        eitamw1 = 'eitamw'
        eyalt1 = 'eyalt'
        faceart1 = 'faceart'
        feiner1 = 'feiner'
        gabot1 = 'gabot'
        galor1 = 'galor'
        garac1 = 'garac'
        garae1 = 'garae'
        hadas1 = 'hadas'
        hadasat1 = 'hadasat'
        hadtest1 = 'hadtest'
        hclinic1 = 'hclinic'
        highdoc1 = 'highdoc'
        honey1 = 'honey'
        hwc1 = 'hwc'
        ibc1 = 'ibc'
        kaplan1 = 'kaplan'
        kesher1 = 'kesher'
        lbm1 = 'lbm'
        limorb1 = 'limorb'
        lipo1 = 'lipo'
        mamilla1 = 'mamilla'
        maoz1 = 'maoz'
        marcel1 = 'marcel'
        marome1 = 'marome'
        matanis1 = 'matanis'
        mayas1 = 'mayas'
        mazor1 = 'mazor'
        medassist1 = 'medassist'
        meyero1 = 'meyero'
        neshai1 = 'neshai'
        orenw1 = 'orenw'
        orits1 = 'orits'
        r1test1 = 'r1test'
        rbn1 = 'rbn'
        rdgw1 = 'rdgw'
        regev1 = 'regev'
        revitalc1 = 'revitalc'
        roqa1 = 'roqa'
        roqa21 = 'roqa2'
        rosales1 = 'rosales'
        rots31 = 'rots3'
        sarita1 = 'sarita'
        shahwan1 = 'shahwan'
        shine1 = 'shine'
        tenecare1 = 'tenecare'
        tessone1 = 'tessone'
        theclinic1 = 'theclinic'
        tiratz1 = 'tiratz'
        yaelh1 = 'yaelh'
        yoavy1 = 'yoavy'
        yosefm1 = 'yosefm'
        for item in ROTS3_LIST:
            print(item)
        Customer3 = input("Select Customer ID:")
        if Customer3 in (All):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            KillButton = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/a[1]')
            Do = ActionChains(driver)
            Do.click(KillButton)
            Do.perform()
        if Customer3 in (amie, amiri, arikz, asafb, ato, barlevy, barr, blachash, bodyc, feiner, doc, doronb, eitamw, eyalt, faceart, feiner, gabot, galor, garac, garae, hadas, hadasat, hadtest, hclinic, highdoc, honey, hwc, ibc, kaplan, kesher, lbm, limorb, lipo, mamilla, maoz, marcel, marome, matanis, mayas, mazor, medassist, meyero, neshai, orenw, orits, r1test, rbn, rdgw, regev, revitalc, roqa, roqa2, rosales, rots3, sarita, shahwan, shine, tenecare, tessone, theclinic, tiratz, yaelh, yoavy, yosefm):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            search = driver.find_element_by_xpath('/html/body/div/main/div/div/div[1]/form/p/input[1]')
            if Customer3 in (amie):
                search.send_keys(amie1)
            elif Customer3 in (amiri):
                search.send_keys(amiri1)
            elif Customer3 in (arikz):
                search.send_keys(arikz1)
            elif Customer3 in (asafb):
                search.send_keys(asafb1)
            elif Customer3 in (ato):
                search.send_keys(ato1)
            elif Customer3 in (barlevy):
                search.send_keys(barlevy1)
            elif Customer3 in (barr):
                search.send_keys(barr1)
            elif Customer3 in (blachash):
                search.send_keys(blachash1)
            elif Customer3 in (bodyc):
                search.send_keys(bodyc1)
            elif Customer3 in (feiner):
                search.send_keys(feiner1)
            elif Customer3 in (gabot):
                search.send_keys(gabot1)
            elif Customer3 in (galor):
                search.send_keys(galor1)
            elif Customer3 in (garac):
                search.send_keys(garac1)
            elif Customer3 in (garae):
                search.send_keys(garae1)
            elif Customer3 in (hadas):
                search.send_keys(hadas1)
            elif Customer3 in (hadasat):
                search.send_keys(hadasat1)
            elif Customer3 in (hadtest):
                search.send_keys(hadtest1)
            elif Customer3 in (hclinic):
                search.send_keys(hclinic1)
            elif Customer3 in (highdoc):
                search.send_keys(highdoc1)
            elif Customer3 in (honey):
                search.send_keys(honey1)
            elif Customer3 in (hwc):
                search.send_keys(hwc1)
            elif Customer3 in (ibc):
                search.send_keys(ibc1)
            elif Customer3 in (kaplan):
                search.send_keys(kaplan1)
            elif Customer3 in (kesher):
                search.send_keys(kesher1)
            elif Customer3 in (lbm):
                search.send_keys(lbm1)
            elif Customer3 in (limorb):
                search.send_keys(limorb1)
            elif Customer3 in (lipo):
                search.send_keys(lipo1)
            elif Customer3 in (mamilla):
                search.send_keys(mamilla1)
            elif Customer3 in (maoz):
                search.send_keys(maoz1)
            elif Customer3 in (marcel):
                search.send_keys(marcel1)
            elif Customer3 in (marome):
                search.send_keys(marome1)
            elif Customer3 in (matanis):
                search.send_keys(matanis1)
            elif Customer3 in (mayas):
                search.send_keys(mayas1)
            elif Customer3 in (mazor):
                search.send_keys(mazor1)
            elif Customer3 in (medassist):
                search.send_keys(medassist1)
            elif Customer3 in (meyero):
                search.send_keys(meyero1)
            elif Customer3 in (neshai):
                search.send_keys(neshai1)
            elif Customer3 in (orenw):
                search.send_keys(orenw1)
            elif Customer3 in (orits):
                search.send_keys(orits1)
            elif Customer3 in (r1test):
                search.send_keys(r1test1)
            elif Customer3 in (rbn):
                search.send_keys(rbn1)
            elif Customer3 in (rdgw):
                search.send_keys(rdgw1)
            elif Customer3 in (regev):
                search.send_keys(regev1)
            elif Customer3 in (revitalc):
                search.send_keys(revitalc1)
            elif Customer3 in (roqa):
                search.send_keys(roqa1)
            elif Customer3 in (roqa2):
                search.send_keys(roqa21)
            elif Customer3 in (rosales):
                search.send_keys(rosales1)
            elif Customer3 in (rots3):
                search.send_keys(rots31)
            elif Customer3 in (sarita):
                search.send_keys(sarita1)
            elif Customer3 in (shahwan):
                search.send_keys(shahwan1)
            elif Customer3 in (shine):
                search.send_keys(shine1)
            elif Customer3 in (tenecare):
                search.send_keys(tenecare1)
            elif Customer3 in (tessone):
                search.send_keys(tessone1)
            elif Customer3 in (theclinic):
                search.send_keys(theclinic1)
            elif Customer3 in (tiratz):
                search.send_keys(tiratz1)
            elif Customer3 in (yaelh):
                search.send_keys(yaelh1)
            elif Customer3 in (yoavy):
                search.send_keys(yoavy1)
            elif Customer3 in (yosefm):
                search.send_keys(yosefm1)

            search.send_keys(Keys.RETURN)
            sleep(2)
            elem = driver.find_element_by_xpath('/html/body/div/main/div/table/thead/tr/th[1]/input')
            kill = driver.find_element_by_xpath('/html/body/div/main/div/div/div[4]/form/p/input[1]')
            actions = ActionChains(driver)
            actions.click(elem)
            actions.click(kill)
            actions.perform()

    
#M4U Config
    if ChooseServer in M4U:
        M4U_LIST = ["CUSTOMER ID:", "All ==  0, amirw == 1, amor == 2, angio == 3, anuchka == 4, arbel == 5, athletic == 6, aviramb == 7, barakl == 8, barziv == 9, beautyc == 10", "beautyclass == 11, bellac == 12, bestmedical == 13, betterlife == 14, bina == 15 , borochov == 16, briuta == 17, brodsky == 18, btl == 19, cantek == 20", "danab == 21, deadsea == 22, deborac == 23, ecopolitan == 24, emsplus == 25, epilogic == 26, epos == 27, espada == 28, exper == 29, femi == 30", "guyg == 31, hadari == 32, haddada == 33, healthyaging == 34, herzala == 35, hescular == 36, icekson == 37, juc == 38, juvenus == 39, kalus == 40", "kesem == 41, krupnik == 42, kubiyot == 43, kuperman == 44, labriut == 45, lemaanam == 46, levid == 47, lightc == 48, mbcosmetic == 49, moon == 50", "morbeauty == 51, morlaser == 52, mtc == 53, naturaclinic == 54, naturclinic == 55, newmedic == 56, nitza == 57, novotalk == 58, ofery == 59, orasis == 60", "orc == 61, pearlynn == 62, physio == 63, proacademy == 64, protea == 65, psagot == 66, qmedical == 67, r-c == 68, raz == 69, rebeccav == 70", "rustam == 71, sharap == 72, shechter == 73, shiloah == 74, sil == 75, simono == 76, slovak == 77, smadarp == 78, social == 79, solomon == 80", "styledent == 81, tamarh == 82, terem == 83, tivot == 84, top == 85, tzaad == 86, virtuoz == 87, vtc == 88, winkler == 89, yaelj == 90", "yardenc == 91, yoava = 92, borochov == 93, faceboutique == 94, anneruth == 95 advmedworld == 96"]
        All = '0'
        amirw = '1'
        amor = '2'
        angio = '3'
        anuchka = '4'
        arbel = '5'
        athletic = '6'
        aviramb = '7'
        barakl = '8'
        barziv = '9'
        beautyc = '10'
        beautyclass = '11'
        bellac = '12'
        bestmedical = '13'
        betterlife = '14'
        bina = '15'
        borochov = '16'
        briuta = '17'
        brodsky = '18'
        btl = '19'
        cantek = '20'
        danab = '21'
        deadsea = '22'
        deborac = '23'
        ecopolitan = '24'
        emsplus = '25'
        epilogic = '26'
        epos = '27'
        espada = '28'
        exper = '29'
        femi = '30'
        guyg = '31'
        hadari = '32'
        haddada = '33'
        healthyaging = '34'
        herzala = '35'
        hescular = '36'
        icekson = '37'
        juc = '38'
        juvenus = '39'
        kalus = '40'
        kesem = '41'
        krupnik = '42'
        kubiyot = '43'
        kuperman = '44'
        labriut = '45'
        lemaanam = '46'
        levid = '47'
        lightc = '48'
        mbcosmetic = '49'
        moon = '50'
        morbeauty = '51'
        morlaser = '52'
        mtc = '53'
        naturaclinic = '54'
        naturclinic = '55'
        newmedic = '56'
        nitza = '57'
        novotalk = '58'
        ofery = '59'
        orasis = '60'
        orc = '61'
        pearlynn = '62'
        physio = '63'
        proacademy = '64'
        protea = '65'
        psagot = '66'
        qmedical = '67'
        rc = '68'
        raz = '69'
        rebeccav = '70'
        rustam = '71'
        sharap = '72'
        shechter = '73'
        shiloah = '74'
        sil = '75'
        simono = '76'
        slovak = '77'
        smadarp = '78'
        social = '79'
        solomon = '80'
        styledent = '81'
        tamarh = '82'
        terem = '83'
        tivot = '84'
        top = '85'
        tzaad = '86'
        virtuoz = '87'
        vtc = '88'
        winkler = '89'
        yaelj = '90'
        yardenc = '91'
        yoava = '92'
        borochov = '93'
        faceboutique = '94'
        anneruth = '95'
        advmedworld = '96'
        amirw1 = 'amirw'
        amor1 = 'amor'
        angio1 = 'angio'
        anneruth1 = 'anneruth'
        anuchka1 = 'anuchka'
        arbel1 = 'arbel'
        athletic1 = 'athletic'
        aviramb1 = 'aviramb'
        barakl1 = 'barakl'
        barziv1 = 'barziv'
        beautyc1 = 'beautyc'
        beautyclass1 = 'beautyclass'
        bellac1 = 'bellac'
        bestmedical1 = 'bestmedical'
        betterlife1 = 'betterlife'
        bina1 = 'bina'
        borochov1 = 'borochov'
        briuta1 = 'briuta'
        brodsky1 = 'brodsky'
        btl1 = 'btl'
        cantek1 = 'cantek'
        danab1 = 'danab'
        deadsea1 = 'deadsea'
        deborac1 = 'deborac'
        ecopolitan1 = 'ecopolitan'
        emsplus1 = 'emsplus'
        epilogic1 = 'epilogic'
        epos1 = 'epos'
        espada1 = 'espada'
        exper1 = 'exper'
        femi1 = 'femi'
        guyg1 = 'guyg'
        hadari1 = 'hadari'
        haddada1 = 'haddada'
        healthyaging1 = 'healthyaging'
        herzala1 = 'herzala'
        hescular1 = 'hescular'
        icekson1 = 'icekson'
        juc1 = 'juc'
        juvenus1 = 'juvenus'
        kalus1 = 'kalus'
        kesem1 = 'kesem'
        krupnik1 = 'krupnik'
        kubiyot1 = 'kubiyot'
        kuperman1 = 'kuperman'
        labriut1 = 'labriut'
        lemaanam1 = 'lemaanam'
        levid1 = 'levid'
        lightc1 = 'lightc'
        mbcosmetic1 = 'mbcosmetic'
        moon1 = 'moon'
        morbeauty1 = 'morbeauty'
        morlaser1 = 'morlaser'
        mtc1 = 'mtc'
        naturaclinic1 = 'naturaclinic'
        naturclinic1 = 'naturclinic'
        newmedic1 = 'newmedic'
        nitza1 = 'nitza'
        novotalk1 = 'novotalk'
        ofery1 = 'ofery'
        orasis1 = 'orasis'
        orcE = 'orc'
        pearlynn1 = 'pearlynn'
        physio1 = 'physio'
        proacademy1 = 'proacademy'
        protea1 = 'protea'
        psagot1 = 'psagot'
        qmedical1 = 'qmedical'
        rc1 = 'r-c'
        raz1 = 'raz'
        rebeccav1 = 'rebeccav'
        rustam1 = 'rustam'
        sharap1 = 'sharap'
        shechter1 = 'shechter'
        shiloah1 = 'shiloah'
        sil1 = 'sil'
        simono1 = 'simono'
        slovak1 = 'slovak'
        smadarp1 = 'smadarp'
        social1 = 'social'
        solomon1 = 'solomon'
        styledent1 = 'styledent'
        tamarh1 = 'tamarh'
        terem1 = 'terem'
        tivot1 = 'tivot'
        top1 = 'top'
        tzaad1 = 'tzaad'
        virtuoz1 = 'virtuoz'
        vtc1 = 'vtc'
        winkler1 = 'winkler'
        yaelj1 = 'yaelj'
        yardenc1 = 'yardenc'
        yoava1 = 'yoava'
        borochov1 = 'borochov'
        faceboutique1 = 'faceboutique'
        advmedworld1 = 'advmedworld'
        for item in M4U_LIST:
            print(item)
        Customer4 = input("Select Customer ID:")
        if Customer4 in (All):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            KillButton = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/a[1]')
            Do = ActionChains(driver)
            Do.click(KillButton)
            Do.perform()
            break
        elif Customer4 in (amirw, amor, angio, anneruth, anuchka, arbel, athletic, aviramb, barakl, barziv, beautyc, beautyclass, bellac, bestmedical, betterlife, bina, borochov, briuta, brodsky, btl, cantek, danab, deadsea, deborac, ecopolitan, emsplus, epilogic, epos, espada, exper, femi, guyg, hadari, haddada, healthyaging, herzala, hescular, icekson, juc, juvenus, kalus, kesem, krupnik, kubiyot, kuperman, labriut, lemaanam, levid, lightc, mbcosmetic, moon, morbeauty, morlaser, mtc, naturaclinic ,naturclinic, newmedic, nitza, novotalk, ofery, orasis, orc, pearlynn, physio, proacademy, protea, psagot, qmedical, rc, raz, rebeccav, rustam, sharap, shechter, shiloah, sil, simono, slovak, smadarp, social, solomon, styledent, tamarh, terem, tivot, top, tzaad, virtuoz, vtc, winkler, yaelj, yardenc, yoava, borochov, faceboutique):
            print('Working..')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get("http://localhost:5001/")
            sleep(2)
            search = driver.find_element_by_xpath('/html/body/div/main/div/div/div[1]/form/p/input[1]')
            if Customer4 in (amirw):
                search.send_keys(amirw1)
            elif Customer4 in (amor):
                search.send_keys(amor1)
            elif Customer4 in (angio):
                search.send_keys(angio1)
            elif Customer4 in (anneruth):
                search.send_keys(anneruth1)
            elif Customer4 in (anuchka):
                search.send_keys(anuchka1)
            elif Customer4 in (arbel):
                search.send_keys(arbel1)
            elif Customer4 in (athletic):
                search.send_keys(athletic1)
            elif Customer4 in (aviramb):
                search.send_keys(aviramb1)
            elif Customer4 in (barakl):
                search.send_keys(barakl1)
            elif Customer4 in (barziv):
                search.send_keys(barziv1)
            elif Customer4 in (beautyc):
                search.send_keys(beautyc1)
            elif Customer4 in (beautyclass):
                search.send_keys(beautyclass1)
            elif Customer4 in (bellac):
                search.send_keys(bellac1)
            elif Customer4 in (bestmedical):
                search.send_keys(bestmedical1)
            elif Customer4 in (betterlife):
                search.send_keys(betterlife1)
            elif Customer4 in (bina):
                search.send_keys(bina1)
            elif Customer4 in (borochov):
                search.send_keys(borochov1)
            elif Customer4 in (briuta):
                search.send_keys(briuta1)
            elif Customer4 in (brodsky):
                search.send_keys(brodsky1)
            elif Customer4 in (btl):
                search.send_keys(btl1)
            elif Customer4 in (cantek):
                search.send_keys(cantek1)
            elif Customer4 in (danab):
                search.send_keys(danab1)
            elif Customer4 in (deadsea):
                search.send_keys(deadsea1)
            elif Customer4 in (deborac):
                search.send_keys(deborac1)
            elif Customer4 in (ecopolitan):
                search.send_keys(ecopolitan1)
            elif Customer4 in (emsplus):
                search.send_keys(emsplus1)
            elif Customer4 in (epilogic):
                search.send_keys(epilogic1)
            elif Customer4 in (epos):
                search.send_keys(epos1)
            elif Customer4 in (espada):
                search.send_keys(espada1)
            elif Customer4 in (exper):
                search.send_keys(exper1)
            elif Customer4 in (femi):
                search.send_keys(femi1)
            elif Customer4 in (guyg):
                search.send_keys(guyg1)
            elif Customer4 in (hadari):
                search.send_keys(hadari1)
            elif Customer4 in (haddada):
                search.send_keys(haddada1)
            elif Customer4 in (healthyaging):
                search.send_keys(healthyaging1)
            elif Customer4 in (herzala):
                search.send_keys(herzala1)
            elif Customer4 in (hescular):
                search.send_keys(hescular1)
            elif Customer4 in (icekson):
                search.send_keys(icekson1)
            elif Customer4 in (juc):
                search.send_keys(juc1)
            elif Customer4 in (juvenus):
                search.send_keys(juvenus1)
            elif Customer4 in (kalus):
                search.send_keys(kalus1)
            elif Customer4 in (kesem):
                search.send_keys(kesem1)
            elif Customer4 in (krupnik):
                search.send_keys(krupnik1)
            elif Customer4 in (kubiyot):
                search.send_keys(kubiyot1)
            elif Customer4 in (kuperman):
                search.send_keys(kuperman1)
            elif Customer4 in (labriut):
                search.send_keys(labriut1)
            elif Customer4 in (lemaanam):
                search.send_keys(lemaanam1)
            elif Customer4 in (levid):
                search.send_keys(levid1)
            elif Customer4 in (lightc):
                search.send_keys(lightc1)
            elif Customer4 in (mbcosmetic):
                search.send_keys(mbcosmetic1)
            elif Customer4 in (moon):
                search.send_keys(moon1)
            elif Customer4 in (morbeauty):
                search.send_keys(morbeauty1)
            elif Customer4 in (morlaser):
                search.send_keys(morlaser1)
            elif Customer4 in (mtc):
                search.send_keys(mtc1)
            elif Customer4 in (naturaclinic):
                search.send_keys(naturaclinic1)
            elif Customer4 in (naturclinic):
                search.send_keys(naturclinic1)
            elif Customer4 in (newmedic):
                search.send_keys(newmedic1)
            elif Customer4 in (nitza):
                search.send_keys(nitza1)
            if Customer4 in (novotalk):
                search.send_keys(novotalk1)
            elif Customer4 in (ofery):
                search.send_keys(ofery1)
            elif Customer4 in (orasis):
                search.send_keys(orasis1)
            elif Customer4 in (orc):
                search.send_keys(orcE)
            elif Customer4 in (pearlynn):
                search.send_keys(pearlynn1)
            elif Customer4 in (physio):
                search.send_keys(physio1)
            elif Customer4 in (proacademy):
                search.send_keys(proacademy1)
            elif Customer4 in (protea):
                search.send_keys(protea1)
            elif Customer4 in (psagot):
                search.send_keys(psagot1)
            elif Customer4 in (qmedical):
                search.send_keys(qmedical1)
            elif Customer4 in (rc):
                search.send_keys(rc1)
            elif Customer4 in (raz):
                search.send_keys(raz1)
            elif Customer4 in (rebeccav):
                search.send_keys(rebeccav1)
            elif Customer4 in (rustam):
                search.send_keys(rustam1)
            elif Customer4 in (sharap):
                search.send_keys(sharap1)
            elif Customer4 in (shechter):
                search.send_keys(shechter1)
            elif Customer4 in (shiloah):
                search.send_keys(shiloah1)
            elif Customer4 in (sil):
                search.send_keys(sil1)
            elif Customer4 in (simono):
                search.send_keys(simono1)
            elif Customer4 in (slovak):
                search.send_keys(slovak1)
            elif Customer4 in (smadarp):
                search.send_keys(smadarp1)
            elif Customer4 in (social):
                search.send_keys(social1)
            elif Customer4 in (solomon):
                search.send_keys(solomon1)
            elif Customer4 in (styledent):
                search.send_keys(styledent1)
            elif Customer4 in (tamarh):
                search.send_keys(tamarh1)
            elif Customer4 in (terem):
                search.send_keys(terem1)
            elif Customer4 in (tivot):
                search.send_keys(tivot1)
            elif Customer4 in (top):
                search.send_keys(top1)
            elif Customer4 in (tzaad):
                search.send_keys(tzaad1)
            elif Customer4 in (virtuoz):
                search.send_keys(virtuoz1)
            elif Customer4 in (vtc):
                search.send_keys(vtc1)
            elif Customer4 in (winkler):
                search.send_keys(winkler1)
            elif Customer4 in (yaelj):
                search.send_keys(yaelj1)
            elif Customer4 in (yardenc):
                search.send_keys(yardenc1)
            elif Customer4 in (yoava):
                search.send_keys(yoava1)
            elif Customer4 in (borochov):
                search.send_keys(borochov1)
            elif Customer4 in (faceboutique):
                search.send_keys(faceboutique1)
            elif Customer4 in (advmedworld):
                search.send_keys(advmedworld1)


            search.send_keys(Keys.RETURN)
            sleep(2)
            elem = driver.find_element_by_xpath('/html/body/div/main/div/table/thead/tr/th[1]/input')
            kill = driver.find_element_by_xpath('/html/body/div/main/div/div/div[4]/form/p/input[1]')
            actions = ActionChains(driver)
            actions.click(elem)
            actions.click(kill)
            actions.perform()


#Powershell update websites
    while True:
        Live = ['Live', 'LIVE', 'live']
        Live2 = ['350']
        Develop = ['DEV', 'Dev', 'dev']
        WannaUp = input('Would you like to update?(Y/N):')
        print('Update RapidOne to 3.4.2 / 3.5.0 / DEVELOP with default settings.')

        if WannaUp in noChoice:
            print('Ok.. Skipping.')
            exit(0)

        if WannaUp in yesChoice:
            Version = input('3.4.2 / 3.5.0 / DEVELOP? (LIVE or DEV or 350):')
#ROTS1 Config
            if Version in Live: 
                if ChooseServer in ROTS1:
                    for item in ROTS1_LIST:
                        print(item)
            SelectCx = input("Select Customer ID:")
            if SelectCx in (alevy, amattra, amirg, assutat, baston, berkoyar, goder, hairm, hanic, heart4u, idith, idithtest, infinity, koren, kraussclinic, lifet, liliam, maxia, michaele, miller, mirih, morom, naderb, olgao, oxypro, refaelc, refuahvezrah, ro1, ronia, roniatest, roron, rots1, saritd, schein, sharona, time4s, uvneh, yaffac, yosefn):
                print('Updaing..')
            if SelectCx in (alevy):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments alevy")
            elif SelectCx in (All):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments")
            elif SelectCx in (amattra):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments amattra")
            elif SelectCx in (amirg):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments amirg")
            elif SelectCx in (assutat):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments assutat")
            elif SelectCx in (baston):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments baston")
            elif SelectCx in (berkoyar):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments berkoyar")
            elif SelectCx in (goder):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments goder")
            elif SelectCx in (hairm):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hairm")
            elif SelectCx in (hanic):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hanic")
            elif SelectCx in (heart4u):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments heart4u")
            elif SelectCx in (idith):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments idith")
            elif SelectCx in (idithtest):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments idithtest")
            elif SelectCx in (infinity):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments infinity")
            elif SelectCx in (koren):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments koren")
            elif SelectCx in (kraussclinic):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments kraussclinic")
            elif SelectCx in (lifet):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments lifet")
            elif SelectCx in (liliam):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments liliam")
            elif SelectCx in (maxia):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments maxia")
            elif SelectCx in (michaele):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments michaele")
            elif SelectCx in (miller):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments miller")
            elif SelectCx in (mirih):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mirih")
            elif SelectCx in (morom):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments morom")
            elif SelectCx in (naderb):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments naderb")
            elif SelectCx in (olgao):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments olgao")
            elif SelectCx in (oxypro):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments oxypro")
            elif SelectCx in (refaelc):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments refaelc")
            elif SelectCx in (refuahvezrah):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments refuahvezrah")
            elif SelectCx in (ro1):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ro1")
            elif SelectCx in (ronia):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ronia")
            elif SelectCx in (roniatest):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments roniatest")
            elif SelectCx in (roron):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments roron")
            elif SelectCx in (rots1):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rots1")
            elif SelectCx in (saritd):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments saritd")
            elif SelectCx in (schein):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments schein")
            elif SelectCx in (sharona):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments sharona")
            elif SelectCx in (time4s):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments time4s")
            elif SelectCx in (uvneh):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments uvneh")
            elif SelectCx in (yaffac):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments yaffac")
            elif SelectCx in (yosefn):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments yosefn")
            exit(0)
#ROTS2 Update
        if Version in Live:
            if ChooseServer in ROTS2:
                for item in ROTS2_LIST:
                    print(item)
            SelectCx2 = input("Select Customer ID:")
            if SelectCx2 in (All, abudi, aradu, avib, babezone, barmeir, biton, boazo, bodyr, celia, clevermed, demo, eichut, eidelman, hairclinic, hdi, heyman, iao, ispa, jbarr, korenm, lam, langer, marcusb, mauricio, medplus, mitt, moscona, mydoctor, ocd, oneman, orenk, perfection, persona, ramac, rivkaz, rosel, rots2, sela, shinemac, talkoren, tanyac, tautest, theta, tilia, vaknint, websmile, wesmile):
                print('Updaing..')
            if SelectCx2 in (abudi):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments abudi")
            elif SelectCx2 in (aradu):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments aradu")
            elif SelectCx2 in (All):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments")
            elif SelectCx2 in (avib):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments avib")
            elif SelectCx2 in (babezone):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments babezone")
            elif SelectCx2 in (barmeir):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments barmeir")
            elif SelectCx2 in (biton):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments biton")
            elif SelectCx2 in (boazo):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments boazo")
            elif SelectCx2 in (bodyr):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments bodyr")
            elif SelectCx2 in (celia):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments celia")
            elif SelectCx2 in (clevermed):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments clevermed")
            elif SelectCx2 in (demo):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments demo")
            elif SelectCx2 in (eichut):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments eichut")
            elif SelectCx2 in (eidelman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments eidelman")
            elif SelectCx2 in (hairclinic):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hairclinic")
            elif SelectCx2 in (hdi):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hdi")
            elif SelectCx2 in (heyman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments heyman")
            elif SelectCx2 in (iao):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments iao")
            elif SelectCx2 in (ispa):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ispa")
            elif SelectCx2 in (jbarr):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments jbarr")
            elif SelectCx2 in (korenm):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments korenm")
            elif SelectCx2 in (lam):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments lam")
            elif SelectCx2 in (langer):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments langer")
            elif SelectCx2 in (marcusb):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments marcusb")
            elif SelectCx2 in (mauricio):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mauricio")
            elif SelectCx2 in (medplus):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments medplus")
            elif SelectCx2 in (mitt):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mitt")
            elif SelectCx2 in (moscona):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments moscona")
            elif SelectCx2 in (mydoctor):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mydoctor")
            elif SelectCx2 in (ocd):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ocd")
            elif SelectCx2 in (oneman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments oneman")
            elif SelectCx2 in (orenk):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments orenk")
            elif SelectCx2 in (perfection):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments perfection")
            elif SelectCx2 in (persona):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments persona")
            elif SelectCx2 in (ramac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ramac")
            elif SelectCx2 in (rivkaz):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rivkaz")
            elif SelectCx2 in (rosel):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rosel")
            elif SelectCx2 in (rots2):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rots2")
            elif SelectCx2 in (sela):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments sela")
            elif SelectCx2 in (shinemac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments shine-mac")
            elif SelectCx2 in (talkoren):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments talkoren")
            elif SelectCx2 in (tanyac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments tanyac")
            elif SelectCx2 in (tautest):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments tautest")
            elif SelectCx2 in (theta):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments theta")
            elif SelectCx2 in (tilia):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments tilia")
            elif SelectCx2 in (vaknint):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments vaknint")
            elif SelectCx2 in (websmile):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments websmile")
            elif SelectCx2 in (wesmile):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments wesmile")
            exit(0)

#ROTS3 Update
        if Version in Live:
            if ChooseServer in ROTS3:
                    for item in ROTS3_LIST:
                        print(item)
                    SelectCx3 = input("Select Customer ID:")
                    if SelectCx3 in (All, amie, amiri, arikz, asafb, ato, barlevy, barr, blachash, bodyc, feiner, doc, doronb, eitamw, eyalt, faceart, feiner, gabot, galor, garac, garae, hadas, hadasat, hadtest, hclinic, highdoc, honey, hwc, ibc, kaplan, kesher, lbm, limorb, lipo, mamilla, maoz, marcel, marome, matanis, mayas, mazor, medassist, meyero, neshai, orenw, orits, r1test, rbn, rdgw, regev, revitalc, roqa, roqa2, rosales, rots3, sarita, shahwan, shine, tenecare, tessone, theclinic, tiratz, yaelh, yoavy, yosefm):
                        print('Updaing..')
                    if SelectCx3 in (amie):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments amie")
                    elif SelectCx3 in (amiri):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments amiri")
                    elif SelectCx3 in (All):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments")
                    elif SelectCx3 in (arikz):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments arikz")
                    elif SelectCx3 in (asafb):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments asafb")
                    elif SelectCx3 in (ato):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ato")
                    elif SelectCx3 in (barlevy):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments barlevy")
                    elif SelectCx3 in (barr):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments barr")
                    elif SelectCx3 in (blachash):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments blachash")
                    elif SelectCx3 in (bodyc):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments bodyc")
                    elif SelectCx3 in (feiner):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments feiner")
                    elif SelectCx3 in (doc):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments doc")
                    elif SelectCx3 in (doronb):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments doronb")
                    elif SelectCx3 in (eitamw):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments eitamw")
                    elif SelectCx3 in (eyalt):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments eyalt")
                    elif SelectCx3 in (faceart):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments faceart")
                    elif SelectCx3 in (feiner):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments feiner")
                    elif SelectCx3 in (gabot):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments gabot")
                    elif SelectCx3 in (galor):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments galor")
                    elif SelectCx3 in (garac):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments garac")
                    elif SelectCx3 in (garae):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments garae")
                    elif SelectCx3 in (hadas):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hadas")
                    elif SelectCx3 in (hadasat):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hadasat")
                    elif SelectCx3 in (hadtest):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hadtest")
                    elif SelectCx3 in (hclinic):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hclinic")
                    elif SelectCx3 in (highdoc):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments highdoc")
                    elif SelectCx3 in (honey):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments honey")
                    elif SelectCx3 in (hwc):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments hwc")
                    elif SelectCx3 in (ibc):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments ibc")
                    elif SelectCx3 in (kaplan):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments kaplan")
                    elif SelectCx3 in (kesher):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments kesher")
                    elif SelectCx3 in (lbm):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments lbm")
                    elif SelectCx3 in (limorb):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments limorb")
                    elif SelectCx3 in (lipo):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments lipo")
                    elif SelectCx3 in (mamilla):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mamilla")
                    elif SelectCx3 in (maoz):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments maoz")
                    elif SelectCx3 in (marcel):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments marcel")
                    elif SelectCx3 in (marome):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments marome")
                    elif SelectCx3 in (matanis):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments matanis")
                    elif SelectCx3 in (mayas):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mayas")
                    elif SelectCx3 in (mazor):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments mazor")
                    elif SelectCx3 in (medassist):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments medassist")
                    elif SelectCx3 in (meyero):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments meyero")
                    elif SelectCx3 in (neshai):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments neshai")
                    elif SelectCx3 in (orenw):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments orenw")
                    elif SelectCx3 in (orits):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments orits")
                    elif SelectCx3 in (r1test):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments r1test")
                    elif SelectCx3 in (rbn):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rbn")
                    elif SelectCx3 in (rdgw):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rdgw")
                    elif SelectCx3 in (regev):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments regev")
                    elif SelectCx3 in (revitalc):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments revitalc")
                    elif SelectCx3 in (roqa):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments roqa")
                    elif SelectCx3 in (roqa2):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments roqa2")
                    elif SelectCx3 in (rosales):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rosales")
                    elif SelectCx3 in (rots3):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments rots3")
                    elif SelectCx3 in (sarita):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments sarita")
                    elif SelectCx3 in (shahwan):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments shahwan")
                    elif SelectCx3 in (shine):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments shine")
                    elif SelectCx3 in (tenecare):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments tenecare")
                    elif SelectCx3 in (tessone):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments tessone")
                    elif SelectCx3 in (theclinic):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments theclinic")
                    elif SelectCx3 in (tiratz):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments tiratz")
                    elif SelectCx3 in (yaelh):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments yaelh")
                    elif SelectCx3 in (yoavy):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments yoavy")
                    elif SelectCx3 in (yosefm):
                            os.system(R"powershell.exe cd C:\users\vlad\desktop")
                            os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments yosefm")
                    exit(0)

#M4U Update
        if Version in Live:
            if ChooseServer in M4U:
                    for item in M4U_LIST:
                        print(item)
                    SelectCx4 = input("Select Customer ID:")
                    if SelectCx4 in (All, amirw, amor, angio, anneruth, anuchka, arbel, athletic, aviramb, barakl, barziv, beautyc, beautyclass, bellac, bestmedical, betterlife, bina, borochov, briuta, brodsky, btl, cantek, danab, deadsea, deborac, ecopolitan, emsplus, epilogic, epos, espada, exper, femi, guyg, hadari, haddada, healthyaging, herzala, hescular, icekson, juc, juvenus, kalus, kesem, krupnik, kubiyot, kuperman, labriut, lemaanam, levid, lightc, mbcosmetic, moon, morbeauty, morlaser, mtc, naturaclinic ,naturclinic, newmedic, nitza, novotalk, ofery, orasis, orc, pearlynn, physio, proacademy, protea, psagot, qmedical, rc, raz, rebeccav, rustam, sharap, shechter, shiloah, sil, simono, slovak, smadarp, social, solomon, styledent, tamarh, terem, tivot, top, tzaad, virtuoz, vtc, winkler, yaelj, yardenc, yoava, borochov, faceboutique, advmedworld):
                        print('Updaing..')
                    if SelectCx4 in (amirw):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R73_amirw")
                    elif SelectCx4 in (amor):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R09_Amor")
                    elif SelectCx4 in (All):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments")
                    elif SelectCx4 in (angio):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R70_Angio")
                    elif SelectCx4 in (anuchka):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R14_Anuchka")
                    elif SelectCx4 in (arbel):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R31_Arbel")
                    elif SelectCx4 in (athletic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R27_Athletic")
                    elif SelectCx4 in (aviramb):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R74_AviramB")
                    elif SelectCx4 in (barakl):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R06_BarakL")
                    elif SelectCx4 in (barziv):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R89_Barziv")
                    elif SelectCx4 in (beautyc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R34_BeautyC")
                    elif SelectCx4 in (beautyclass):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R66_BeautyClass")
                    elif SelectCx4 in (bestmedical):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R48_Bestmedical")
                    elif SelectCx4 in (betterlife):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R44_BetterLife")
                    elif SelectCx4 in (bina):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R36_Bina")
                    elif SelectCx4 in (borochov):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R90_Borochov")
                    elif SelectCx4 in (briuta):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R76_Briuta")
                    elif SelectCx4 in (brodsky):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R47_Brodsky")
                    elif SelectCx4 in (btl):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R21_BTL")
                    elif SelectCx4 in (cantek):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R08_Cantek")
                    elif SelectCx4 in (danab):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R42_Danab")
                    elif SelectCx4 in (deadsea):
                            print('No Database to update')
                    elif SelectCx4 in (deborac):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R38_DeboraC")
                    elif SelectCx4 in (ecopolitan):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R72_Ecopolitan")
                    elif SelectCx4 in (emsplus):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R12_EMSPlus")
                    elif SelectCx4 in (epilogic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments epilogic")
                    elif SelectCx4 in (epos):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R80_Epos")
                    elif SelectCx4 in (espada):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R62_Espada")
                    elif SelectCx4 in (exper):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R82_Exper")
                    elif SelectCx4 in (femi):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R15_Femi")
                    elif SelectCx4 in (guyg):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R81_GuyG")
                    elif SelectCx4 in (hadari):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R50_Hadari")
                    elif SelectCx4 in (haddada):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R63_HaddadA")
                    elif SelectCx4 in (healthyaging):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R24_HealthyAging")
                    elif SelectCx4 in (herzala):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R58_Herzala")
                    elif SelectCx4 in (hescular):
                            print('No Database to update')
                    elif SelectCx4 in (icekson):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R22_Icekson")
                    elif SelectCx4 in (juc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R56_JUC")
                    elif SelectCx4 in (juvenus):
                            print('No Database to update..')
                    elif SelectCx4 in (kalus):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R26_Kalus")
                    elif SelectCx4 in (kesem):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R60_Kesem")
                    elif SelectCx4 in (krupnik):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R30_Krupnik")
                    elif SelectCx4 in (kubiyot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R87_Kubiyot")
                    elif SelectCx4 in (kuperman):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R59_Kuperman")
                    elif SelectCx4 in (labriut):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R20_Labriut")
                    elif SelectCx4 in (lemaanam):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R04_Lemaanam")
                    elif SelectCx4 in (levid):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R64_LeviD")
                    elif SelectCx4 in (lightc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R11_LightC")
                    elif SelectCx4 in (mbcosmetic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R49_MBCosmetic")
                    elif SelectCx4 in (moon):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R83_Moon")
                    elif SelectCx4 in (morbeauty):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R10_MorBeauty")
                    elif SelectCx4 in (morlaser):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R23_Morlaser")
                    elif SelectCx4 in (mtc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R78_MTC")
                    elif SelectCx4 in (naturaclinic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R41_Naturaclinic")
                    elif SelectCx4 in (naturclinic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R41_Naturaclinic")
                    elif SelectCx4 in (newmedic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R57_Newmedic")
                    elif SelectCx4 in (nitza):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R37_Nitza")
                    elif SelectCx4 in (novotalk):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R92_Novotalk")
                    elif SelectCx4 in (ofery):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R32_OferY")
                    elif SelectCx4 in (orasis):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R28_Orasis")
                    elif SelectCx4 in (orc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R85_OrC")
                    elif SelectCx4 in (pearlynn):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R91_Pearlynn")
                    elif SelectCx4 in (physio):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R51_Physio")
                    elif SelectCx4 in (proacademy):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R33_ProAcademy")
                    elif SelectCx4 in (protea):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R77_Protea")
                    elif SelectCx4 in (psagot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R54_Psagot")
                    elif SelectCx4 in (qmedical):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R86_QMedical")
                    elif SelectCx4 in (rc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R88_RC")
                    elif SelectCx4 in (raz):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R07_Raz")
                    elif SelectCx4 in (rebeccav):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R35_RebeccaV")
                    elif SelectCx4 in (rustam):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R52_Rustam")
                    elif SelectCx4 in (sharap):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R53_Sharap")
                    elif SelectCx4 in (shechter):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R46_Shechter")
                    elif SelectCx4 in (shiloah):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R84_Shiloah")
                    elif SelectCx4 in (sil):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R25_Sil")
                    elif SelectCx4 in (simono):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R18_SimonO")
                    elif SelectCx4 in (slovak):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R79_Slovak")
                    elif SelectCx4 in (smadarp):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments Smadarp")
                    elif SelectCx4 in (social):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R75_Social")
                    elif SelectCx4 in (solomon):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R68_Solomon")
                    elif SelectCx4 in (styledent):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R40_StyleDent")
                    elif SelectCx4 in (tamarh):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R43_TamarH")
                    elif SelectCx4 in (terem):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R55_Terem")
                    elif SelectCx4 in (tivot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R19_tivot")
                    elif SelectCx4 in (top):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R67_Top")
                    elif SelectCx4 in (tzaad):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R16_Tzaad")
                    elif SelectCx4 in (virtuoz):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R17_Virtuoz")
                    elif SelectCx4 in (vtc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R45_VTC")
                    elif SelectCx4 in (winkler):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R39_Winkler")
                    elif SelectCx4 in (yaelj):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R29_YaelJ")
                    elif SelectCx4 in (yardenc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R65_YardenC")
                    elif SelectCx4 in (yoava):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R05_YoavA")
                    elif SelectCx4 in (borochov):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R90_borochov")
                    elif SelectCx4 in (faceboutique):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R97_Faceboutique")
                    elif SelectCx4 in (anneruth):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R13_AnneRuth")
                    elif SelectCx4 in (advmedworld):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version342 -forceConfig -deployEnvironments R106_advmedworld")
                    exit(0)
#ROTS1 DEVELOP
            if Version in Develop: 
                if ChooseServer in ROTS1:
                    for item in ROTS1_LIST:
                        print(item)
            SelectCx = input("Select Customer ID:")
            if SelectCx in (alevy, amattra, amirg, assutat, baston, berkoyar, goder, hairm, hanic, heart4u, idith, idithtest, infinity, koren, kraussclinic, lifet, liliam, maxia, michaele, miller, mirih, morom, naderb, olgao, oxypro, refaelc, refuahvezrah, ro1, ronia, roniatest, roron, rots1, saritd, schein, sharona, time4s, uvneh, yaffac, yosefn):
                print('Updaing..')
            if SelectCx in (alevy):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments alevy")
            elif SelectCx in (All):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments")
            elif SelectCx in (amattra):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments amattra")
            elif SelectCx in (amirg):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments amirg")
            elif SelectCx in (assutat):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments assutat")
            elif SelectCx in (baston):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments baston")
            elif SelectCx in (berkoyar):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments berkoyar")
            elif SelectCx in (goder):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments goder")
            elif SelectCx in (hairm):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hairm")
            elif SelectCx in (hanic):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hanic")
            elif SelectCx in (heart4u):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments heart4u")
            elif SelectCx in (idith):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments idith")
            elif SelectCx in (idithtest):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments idithtest")
            elif SelectCx in (infinity):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments infinity")
            elif SelectCx in (koren):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments koren")
            elif SelectCx in (kraussclinic):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments kraussclinic")
            elif SelectCx in (lifet):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments lifet")
            elif SelectCx in (liliam):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments liliam")
            elif SelectCx in (maxia):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments maxia")
            elif SelectCx in (michaele):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments michaele")
            elif SelectCx in (miller):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments miller")
            elif SelectCx in (mirih):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mirih")
            elif SelectCx in (morom):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments morom")
            elif SelectCx in (naderb):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments naderb")
            elif SelectCx in (olgao):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments olgao")
            elif SelectCx in (oxypro):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments oxypro")
            elif SelectCx in (refaelc):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments refaelc")
            elif SelectCx in (refuahvezrah):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments refuahvezrah")
            elif SelectCx in (ro1):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ro1")
            elif SelectCx in (ronia):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ronia")
            elif SelectCx in (roniatest):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments roniatest")
            elif SelectCx in (roron):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments roron")
            elif SelectCx in (rots1):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rots1")
            elif SelectCx in (saritd):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments saritd")
            elif SelectCx in (schein):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments schein")
            elif SelectCx in (sharona):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments sharona")
            elif SelectCx in (time4s):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments time4s")
            elif SelectCx in (uvneh):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments uvneh")
            elif SelectCx in (yaffac):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments yaffac")
            elif SelectCx in (yosefn):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments yosefn")
            exit(0)
#ROTS2 Develop
        if Version in Develop:
            if ChooseServer in ROTS2:
                for item in ROTS2_LIST:
                    print(item)
            SelectCx2 = input("Select Customer ID:")
            if SelectCx2 in (All, abudi, aradu, avib, babezone, barmeir, biton, boazo, bodyr, celia, clevermed, demo, eichut, eidelman, hairclinic, hdi, heyman, iao, ispa, jbarr, korenm, lam, langer, marcusb, mauricio, medplus, mitt, moscona, mydoctor, ocd, oneman, orenk, perfection, persona, ramac, rivkaz, rosel, rots2, sela, shinemac, talkoren, tanyac, tautest, theta, tilia, vaknint, websmile, wesmile):
                print('Updaing..')
            if SelectCx2 in (abudi):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments abudi")
            elif SelectCx2 in (aradu):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments aradu")
            elif SelectCx2 in (All):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments")
            elif SelectCx2 in (avib):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments avib")
            elif SelectCx2 in (babezone):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments babezone")
            elif SelectCx2 in (barmeir):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments barmeir")
            elif SelectCx2 in (biton):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments biton")
            elif SelectCx2 in (boazo):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments boazo")
            elif SelectCx2 in (bodyr):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments bodyr")
            elif SelectCx2 in (celia):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments celia")
            elif SelectCx2 in (clevermed):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments clevermed")
            elif SelectCx2 in (demo):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments demo")
            elif SelectCx2 in (eichut):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments eichut")
            elif SelectCx2 in (eidelman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments eidelman")
            elif SelectCx2 in (hairclinic):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hairclinic")
            elif SelectCx2 in (hdi):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hdi")
            elif SelectCx2 in (heyman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments heyman")
            elif SelectCx2 in (iao):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments iao")
            elif SelectCx2 in (ispa):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ispa")
            elif SelectCx2 in (jbarr):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments jbarr")
            elif SelectCx2 in (korenm):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments korenm")
            elif SelectCx2 in (lam):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments lam")
            elif SelectCx2 in (langer):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments langer")
            elif SelectCx2 in (marcusb):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments marcusb")
            elif SelectCx2 in (mauricio):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mauricio")
            elif SelectCx2 in (medplus):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments medplus")
            elif SelectCx2 in (mitt):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mitt")
            elif SelectCx2 in (moscona):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments moscona")
            elif SelectCx2 in (mydoctor):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mydoctor")
            elif SelectCx2 in (ocd):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ocd")
            elif SelectCx2 in (oneman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments oneman")
            elif SelectCx2 in (orenk):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments orenk")
            elif SelectCx2 in (perfection):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments perfection")
            elif SelectCx2 in (persona):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments persona")
            elif SelectCx2 in (ramac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ramac")
            elif SelectCx2 in (rivkaz):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rivkaz")
            elif SelectCx2 in (rosel):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rosel")
            elif SelectCx2 in (rots2):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rots2")
            elif SelectCx2 in (sela):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments sela")
            elif SelectCx2 in (shinemac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments shine-mac")
            elif SelectCx2 in (talkoren):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments talkoren")
            elif SelectCx2 in (tanyac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments tanyac")
            elif SelectCx2 in (tautest):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments tautest")
            elif SelectCx2 in (theta):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments theta")
            elif SelectCx2 in (tilia):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments tilia")
            elif SelectCx2 in (vaknint):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments vaknint")
            elif SelectCx2 in (websmile):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments websmile")
            elif SelectCx2 in (wesmile):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments wesmile")
            exit(0)

#ROTS3 Develop
        if Version in Develop: 
            if ChooseServer in ROTS3:
                for item in ROTS3_LIST:
                    print(item)
                SelectCx3 = input("Select Customer ID:")
                if SelectCx3 in (All, amie, amiri, arikz, asafb, ato, barlevy, barr, blachash, bodyc, feiner, doc, doronb, eitamw, eyalt, faceart, feiner, gabot, galor, garac, garae, hadas, hadasat, hadtest, hclinic, highdoc, honey, hwc, ibc, kaplan, kesher, lbm, limorb, lipo, mamilla, maoz, marcel, marome, matanis, mayas, mazor, medassist, meyero, neshai, orenw, orits, r1test, rbn, rdgw, regev, revitalc, roqa, roqa2, rosales, rots3, sarita, shahwan, shine, tenecare, tessone, theclinic, tiratz, yaelh, yoavy, yosefm):
                    print('Updaing..')
                if SelectCx3 in (amie):
                    os.system(R"powershell.exe cd C:\users\vlad\desktop")
                    os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments amie")
                elif SelectCx3 in (amiri):
                    os.system(R"powershell.exe cd C:\users\vlad\desktop")
                    os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments amiri")
                elif SelectCx3 in (All):
                    os.system(R"powershell.exe cd C:\users\vlad\desktop")
                    os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments")
                elif SelectCx3 in (arikz):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments arikz")
                elif SelectCx3 in (asafb):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments asafb")
                elif SelectCx3 in (ato):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ato")
                elif SelectCx3 in (barlevy):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments barlevy")
                elif SelectCx3 in (barr):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments barr")
                elif SelectCx3 in (blachash):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments blachash")
                elif SelectCx3 in (bodyc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments bodyc")
                elif SelectCx3 in (feiner):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments feiner")
                elif SelectCx3 in (doc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments doc")
                elif SelectCx3 in (doronb):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments doronb")
                elif SelectCx3 in (eitamw):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments eitamw")
                elif SelectCx3 in (eyalt):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments eyalt")
                elif SelectCx3 in (faceart):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments faceart")
                elif SelectCx3 in (feiner):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments feiner")
                elif SelectCx3 in (gabot):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments gabot")
                elif SelectCx3 in (galor):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments galor")
                elif SelectCx3 in (garac):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments garac")
                elif SelectCx3 in (garae):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments garae")
                elif SelectCx3 in (hadas):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hadas")
                elif SelectCx3 in (hadasat):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hadasat")
                elif SelectCx3 in (hadtest):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hadtest")
                elif SelectCx3 in (hclinic):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hclinic")
                elif SelectCx3 in (highdoc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments highdoc")
                elif SelectCx3 in (honey):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments honey")
                elif SelectCx3 in (hwc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments hwc")
                elif SelectCx3 in (ibc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments ibc")
                elif SelectCx3 in (kaplan):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments kaplan")
                elif SelectCx3 in (kesher):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments kesher")
                elif SelectCx3 in (lbm):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments lbm")
                elif SelectCx3 in (limorb):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments limorb")
                elif SelectCx3 in (lipo):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments lipo")
                elif SelectCx3 in (mamilla):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mamilla")
                elif SelectCx3 in (maoz):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments maoz")
                elif SelectCx3 in (marcel):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments marcel")
                elif SelectCx3 in (marome):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments marome")
                elif SelectCx3 in (matanis):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments matanis")
                elif SelectCx3 in (mayas):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mayas")
                elif SelectCx3 in (mazor):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments mazor")
                elif SelectCx3 in (medassist):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments medassist")
                elif SelectCx3 in (meyero):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments meyero")
                elif SelectCx3 in (neshai):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments neshai")
                elif SelectCx3 in (orenw):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments orenw")
                elif SelectCx3 in (orits):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments orits")
                elif SelectCx3 in (r1test):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments r1test")
                elif SelectCx3 in (rbn):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rbn")
                elif SelectCx3 in (rdgw):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rdgw")
                elif SelectCx3 in (regev):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments regev")
                elif SelectCx3 in (revitalc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments revitalc")
                elif SelectCx3 in (roqa):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments roqa")
                elif SelectCx3 in (roqa2):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments roqa2")
                elif SelectCx3 in (rosales):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rosales")
                elif SelectCx3 in (rots3):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments rots3")
                elif SelectCx3 in (sarita):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments sarita")
                elif SelectCx3 in (shahwan):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments shahwan")
                elif SelectCx3 in (shine):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments shine")
                elif SelectCx3 in (tenecare):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments tenecare")
                elif SelectCx3 in (tessone):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments tessone")
                elif SelectCx3 in (theclinic):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments theclinic")
                elif SelectCx3 in (tiratz):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments tiratz")
                elif SelectCx3 in (yaelh):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments yaelh")
                elif SelectCx3 in (yoavy):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments yoavy")
                elif SelectCx3 in (yosefm):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments yosefm")
                exit(0)

#M4U DEVELOP
        if Version in Develop:
            if ChooseServer in M4U:
                    for item in M4U_LIST:
                        print(item)
                    SelectCx4 = input("Select Customer ID:")
                    if SelectCx4 in (All, amirw, amor, angio, anneruth, anuchka, arbel, athletic, aviramb, barakl, barziv, beautyc, beautyclass, bellac, bestmedical, betterlife, bina, borochov, briuta, brodsky, btl, cantek, danab, deadsea, deborac, ecopolitan, emsplus, epilogic, epos, espada, exper, femi, guyg, hadari, haddada, healthyaging, herzala, hescular, icekson, juc, juvenus, kalus, kesem, krupnik, kubiyot, kuperman, labriut, lemaanam, levid, lightc, mbcosmetic, moon, morbeauty, morlaser, mtc, naturaclinic ,naturclinic, newmedic, nitza, novotalk, ofery, orasis, orc, pearlynn, physio, proacademy, protea, psagot, qmedical, rc, raz, rebeccav, rustam, sharap, shechter, shiloah, sil, simono, slovak, smadarp, social, solomon, styledent, tamarh, terem, tivot, top, tzaad, virtuoz, vtc, winkler, yaelj, yardenc, yoava, borochov, faceboutique, advmedworld):
                        print('Updaing..')
                    if SelectCx4 in (amirw):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R73_amirw")
                    elif SelectCx4 in (amor):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R09_Amor")
                    elif SelectCx4 in (All):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments")
                    elif SelectCx4 in (angio):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R70_Angio")
                    elif SelectCx4 in (anuchka):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R14_Anuchka")
                    elif SelectCx4 in (arbel):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R31_Arbel")
                    elif SelectCx4 in (athletic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R27_Athletic")
                    elif SelectCx4 in (aviramb):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R74_AviramB")
                    elif SelectCx4 in (barakl):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R06_BarakL")
                    elif SelectCx4 in (barziv):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R89_Barziv")
                    elif SelectCx4 in (beautyc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R34_BeautyC")
                    elif SelectCx4 in (beautyclass):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R66_BeautyClass")
                    elif SelectCx4 in (bestmedical):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R48_Bestmedical")
                    elif SelectCx4 in (betterlife):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R44_BetterLife")
                    elif SelectCx4 in (bina):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R36_Bina")
                    elif SelectCx4 in (borochov):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R90_Borochov")
                    elif SelectCx4 in (briuta):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R76_Briuta")
                    elif SelectCx4 in (brodsky):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R47_Brodsky")
                    elif SelectCx4 in (btl):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R21_BTL")
                    elif SelectCx4 in (cantek):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R08_Cantek")
                    elif SelectCx4 in (danab):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R42_Danab")
                    elif SelectCx4 in (deadsea):
                            print('No Database to update')
                    elif SelectCx4 in (deborac):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R38_DeboraC")
                    elif SelectCx4 in (ecopolitan):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R72_Ecopolitan")
                    elif SelectCx4 in (emsplus):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R12_EMSPlus")
                    elif SelectCx4 in (epilogic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments epilogic")
                    elif SelectCx4 in (epos):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R80_Epos")
                    elif SelectCx4 in (espada):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R62_Espada")
                    elif SelectCx4 in (exper):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R82_Exper")
                    elif SelectCx4 in (femi):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R15_Femi")
                    elif SelectCx4 in (guyg):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R81_GuyG")
                    elif SelectCx4 in (hadari):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R50_Hadari")
                    elif SelectCx4 in (haddada):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R63_HaddadA")
                    elif SelectCx4 in (healthyaging):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R24_HealthyAging")
                    elif SelectCx4 in (herzala):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R58_Herzala")
                    elif SelectCx4 in (hescular):
                            print('No Database to update')
                    elif SelectCx4 in (icekson):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R22_Icekson")
                    elif SelectCx4 in (juc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R56_JUC")
                    elif SelectCx4 in (juvenus):
                            print('No Database to update..')
                    elif SelectCx4 in (kalus):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R26_Kalus")
                    elif SelectCx4 in (kesem):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R60_Kesem")
                    elif SelectCx4 in (krupnik):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R30_Krupnik")
                    elif SelectCx4 in (kubiyot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R87_Kubiyot")
                    elif SelectCx4 in (kuperman):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R59_Kuperman")
                    elif SelectCx4 in (labriut):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R20_Labriut")
                    elif SelectCx4 in (lemaanam):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R04_Lemaanam")
                    elif SelectCx4 in (levid):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R64_LeviD")
                    elif SelectCx4 in (lightc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R11_LightC")
                    elif SelectCx4 in (mbcosmetic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R49_MBCosmetic")
                    elif SelectCx4 in (moon):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R83_Moon")
                    elif SelectCx4 in (morbeauty):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R10_MorBeauty")
                    elif SelectCx4 in (morlaser):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R23_Morlaser")
                    elif SelectCx4 in (mtc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R78_MTC")
                    elif SelectCx4 in (naturaclinic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R41_Naturaclinic")
                    elif SelectCx4 in (naturclinic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R41_Naturaclinic")
                    elif SelectCx4 in (newmedic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R57_Newmedic")
                    elif SelectCx4 in (nitza):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R37_Nitza")
                    elif SelectCx4 in (novotalk):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R92_Novotalk")
                    elif SelectCx4 in (ofery):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R32_OferY")
                    elif SelectCx4 in (orasis):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R28_Orasis")
                    elif SelectCx4 in (orc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R85_OrC")
                    elif SelectCx4 in (pearlynn):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R91_Pearlynn")
                    elif SelectCx4 in (physio):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R51_Physio")
                    elif SelectCx4 in (proacademy):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R33_ProAcademy")
                    elif SelectCx4 in (protea):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R77_Protea")
                    elif SelectCx4 in (psagot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R54_Psagot")
                    elif SelectCx4 in (qmedical):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R86_QMedical")
                    elif SelectCx4 in (rc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R88_RC")
                    elif SelectCx4 in (raz):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R07_Raz")
                    elif SelectCx4 in (rebeccav):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R35_RebeccaV")
                    elif SelectCx4 in (rustam):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R52_Rustam")
                    elif SelectCx4 in (sharap):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R53_Sharap")
                    elif SelectCx4 in (shechter):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R46_Shechter")
                    elif SelectCx4 in (shiloah):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R84_Shiloah")
                    elif SelectCx4 in (sil):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R25_Sil")
                    elif SelectCx4 in (simono):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R18_SimonO")
                    elif SelectCx4 in (slovak):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R79_Slovak")
                    elif SelectCx4 in (smadarp):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments Smadarp")
                    elif SelectCx4 in (social):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R75_Social")
                    elif SelectCx4 in (solomon):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R68_Solomon")
                    elif SelectCx4 in (styledent):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R40_StyleDent")
                    elif SelectCx4 in (tamarh):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R43_TamarH")
                    elif SelectCx4 in (terem):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R55_Terem")
                    elif SelectCx4 in (tivot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R19_tivot")
                    elif SelectCx4 in (top):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R67_Top")
                    elif SelectCx4 in (tzaad):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R16_Tzaad")
                    elif SelectCx4 in (virtuoz):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R17_Virtuoz")
                    elif SelectCx4 in (vtc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R45_VTC")
                    elif SelectCx4 in (winkler):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R39_Winkler")
                    elif SelectCx4 in (yaelj):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R29_YaelJ")
                    elif SelectCx4 in (yardenc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R65_YardenC")
                    elif SelectCx4 in (yoava):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R05_YoavA")
                    elif SelectCx4 in (borochov):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R90_borochov")
                    elif SelectCx4 in (faceboutique):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R97_Faceboutique")
                    elif SelectCx4 in (anneruth):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R13_AnneRuth")
                    elif SelectCx4 in (advmedworld):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition DEVELOP -forceConfig -deployEnvironments R106_advmedworld")
                    exit(0)
#ROTS1 Live2
            if Version in Live2: 
                if ChooseServer in ROTS1:
                    for item in ROTS1_LIST:
                        print(item)
            SelectCx = input("Select Customer ID:")
            if SelectCx in (alevy, amattra, amirg, assutat, baston, berkoyar, goder, hairm, hanic, heart4u, idith, idithtest, infinity, koren, kraussclinic, lifet, liliam, maxia, michaele, miller, mirih, morom, naderb, olgao, oxypro, refaelc, refuahvezrah, ro1, ronia, roniatest, roron, rots1, saritd, schein, sharona, time4s, uvneh, yaffac, yosefn):
                print('Updaing..')
            if SelectCx in (alevy):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments alevy")
            elif SelectCx in (All):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments")
            elif SelectCx in (amattra):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments amattra")
            elif SelectCx in (amirg):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments amirg")
            elif SelectCx in (assutat):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments assutat")
            elif SelectCx in (baston):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments baston")
            elif SelectCx in (berkoyar):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments berkoyar")
            elif SelectCx in (goder):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments goder")
            elif SelectCx in (hairm):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hairm")
            elif SelectCx in (hanic):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hanic")
            elif SelectCx in (heart4u):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments heart4u")
            elif SelectCx in (idith):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments idith")
            elif SelectCx in (idithtest):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments idithtest")
            elif SelectCx in (infinity):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments infinity")
            elif SelectCx in (koren):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments koren")
            elif SelectCx in (kraussclinic):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments kraussclinic")
            elif SelectCx in (lifet):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments lifet")
            elif SelectCx in (liliam):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments liliam")
            elif SelectCx in (maxia):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments maxia")
            elif SelectCx in (michaele):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments michaele")
            elif SelectCx in (miller):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments miller")
            elif SelectCx in (mirih):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mirih")
            elif SelectCx in (morom):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments morom")
            elif SelectCx in (naderb):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments naderb")
            elif SelectCx in (olgao):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments olgao")
            elif SelectCx in (oxypro):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments oxypro")
            elif SelectCx in (refaelc):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments refaelc")
            elif SelectCx in (refuahvezrah):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments refuahvezrah")
            elif SelectCx in (ro1):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ro1")
            elif SelectCx in (ronia):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ronia")
            elif SelectCx in (roniatest):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments roniatest")
            elif SelectCx in (roron):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments roron")
            elif SelectCx in (rots1):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rots1")
            elif SelectCx in (saritd):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments saritd")
            elif SelectCx in (schein):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments schein")
            elif SelectCx in (sharona):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments sharona")
            elif SelectCx in (time4s):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments time4s")
            elif SelectCx in (uvneh):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments uvneh")
            elif SelectCx in (yaffac):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments yaffac")
            elif SelectCx in (yosefn):
                    os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                    os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                    os.system(R"powershell.exe C:\users\sap1.RAPIDCLOUD\desktop\PublishLocal.ps1 -configPath C:\users\sap1.RAPIDCLOUD\desktop\RoTs1Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments yosefn")
            exit(0)
#ROTS2 Live2
        if Version in Live2:
            if ChooseServer in ROTS2:
                for item in ROTS2_LIST:
                    print(item)
            SelectCx2 = input("Select Customer ID:")
            if SelectCx2 in (All, abudi, aradu, avib, babezone, barmeir, biton, boazo, bodyr, celia, clevermed, demo, eichut, eidelman, hairclinic, hdi, heyman, iao, ispa, jbarr, korenm, lam, langer, marcusb, mauricio, medplus, mitt, moscona, mydoctor, ocd, oneman, orenk, perfection, persona, ramac, rivkaz, rosel, rots2, sela, shinemac, talkoren, tanyac, tautest, theta, tilia, vaknint, websmile, wesmile):
                print('Updaing..')
            if SelectCx2 in (abudi):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments abudi")
            elif SelectCx2 in (aradu):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments aradu")
            elif SelectCx2 in (All):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments")
            elif SelectCx2 in (avib):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments avib")
            elif SelectCx2 in (babezone):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments babezone")
            elif SelectCx2 in (barmeir):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments barmeir")
            elif SelectCx2 in (biton):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments biton")
            elif SelectCx2 in (boazo):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments boazo")
            elif SelectCx2 in (bodyr):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments bodyr")
            elif SelectCx2 in (celia):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments celia")
            elif SelectCx2 in (clevermed):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments clevermed")
            elif SelectCx2 in (demo):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments demo")
            elif SelectCx2 in (eichut):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments eichut")
            elif SelectCx2 in (eidelman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments eidelman")
            elif SelectCx2 in (hairclinic):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hairclinic")
            elif SelectCx2 in (hdi):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hdi")
            elif SelectCx2 in (heyman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments heyman")
            elif SelectCx2 in (iao):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments iao")
            elif SelectCx2 in (ispa):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ispa")
            elif SelectCx2 in (jbarr):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments jbarr")
            elif SelectCx2 in (korenm):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments korenm")
            elif SelectCx2 in (lam):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments lam")
            elif SelectCx2 in (langer):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments langer")
            elif SelectCx2 in (marcusb):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments marcusb")
            elif SelectCx2 in (mauricio):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mauricio")
            elif SelectCx2 in (medplus):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments medplus")
            elif SelectCx2 in (mitt):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mitt")
            elif SelectCx2 in (moscona):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments moscona")
            elif SelectCx2 in (mydoctor):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mydoctor")
            elif SelectCx2 in (ocd):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ocd")
            elif SelectCx2 in (oneman):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments oneman")
            elif SelectCx2 in (orenk):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments orenk")
            elif SelectCx2 in (perfection):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments perfection")
            elif SelectCx2 in (persona):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments persona")
            elif SelectCx2 in (ramac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ramac")
            elif SelectCx2 in (rivkaz):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rivkaz")
            elif SelectCx2 in (rosel):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rosel")
            elif SelectCx2 in (rots2):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rots2")
            elif SelectCx2 in (sela):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments sela")
            elif SelectCx2 in (shinemac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments shine-mac")
            elif SelectCx2 in (talkoren):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments talkoren")
            elif SelectCx2 in (tanyac):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments tanyac")
            elif SelectCx2 in (tautest):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments tautest")
            elif SelectCx2 in (theta):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments theta")
            elif SelectCx2 in (tilia):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments tilia")
            elif SelectCx2 in (vaknint):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments vaknint")
            elif SelectCx2 in (websmile):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments websmile")
            elif SelectCx2 in (wesmile):
                    os.system(R"powershell.exe cd c:\users\sap1\desktop")
                    os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments wesmile")
            exit(0)

#ROTS3 Live2
        if Version in Live2: 
            if ChooseServer in ROTS3:
                for item in ROTS3_LIST:
                    print(item)
                SelectCx3 = input("Select Customer ID:")
                if SelectCx3 in (All, amie, amiri, arikz, asafb, ato, barlevy, barr, blachash, bodyc, feiner, doc, doronb, eitamw, eyalt, faceart, feiner, gabot, galor, garac, garae, hadas, hadasat, hadtest, hclinic, highdoc, honey, hwc, ibc, kaplan, kesher, lbm, limorb, lipo, mamilla, maoz, marcel, marome, matanis, mayas, mazor, medassist, meyero, neshai, orenw, orits, r1test, rbn, rdgw, regev, revitalc, roqa, roqa2, rosales, rots3, sarita, shahwan, shine, tenecare, tessone, theclinic, tiratz, yaelh, yoavy, yosefm):
                    print('Updaing..')
                if SelectCx3 in (amie):
                    os.system(R"powershell.exe cd C:\users\vlad\desktop")
                    os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments amie")
                elif SelectCx3 in (amiri):
                    os.system(R"powershell.exe cd C:\users\vlad\desktop")
                    os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments amiri")
                elif SelectCx3 in (All):
                    os.system(R"powershell.exe cd C:\users\vlad\desktop")
                    os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments")
                elif SelectCx3 in (arikz):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments arikz")
                elif SelectCx3 in (asafb):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments asafb")
                elif SelectCx3 in (ato):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ato")
                elif SelectCx3 in (barlevy):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments barlevy")
                elif SelectCx3 in (barr):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments barr")
                elif SelectCx3 in (blachash):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments blachash")
                elif SelectCx3 in (bodyc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments bodyc")
                elif SelectCx3 in (feiner):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments feiner")
                elif SelectCx3 in (doc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments doc")
                elif SelectCx3 in (doronb):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments doronb")
                elif SelectCx3 in (eitamw):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments eitamw")
                elif SelectCx3 in (eyalt):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments eyalt")
                elif SelectCx3 in (faceart):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments faceart")
                elif SelectCx3 in (feiner):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments feiner")
                elif SelectCx3 in (gabot):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments gabot")
                elif SelectCx3 in (galor):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments galor")
                elif SelectCx3 in (garac):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments garac")
                elif SelectCx3 in (garae):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments garae")
                elif SelectCx3 in (hadas):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hadas")
                elif SelectCx3 in (hadasat):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hadasat")
                elif SelectCx3 in (hadtest):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hadtest")
                elif SelectCx3 in (hclinic):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hclinic")
                elif SelectCx3 in (highdoc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments highdoc")
                elif SelectCx3 in (honey):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments honey")
                elif SelectCx3 in (hwc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments hwc")
                elif SelectCx3 in (ibc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments ibc")
                elif SelectCx3 in (kaplan):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments kaplan")
                elif SelectCx3 in (kesher):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments kesher")
                elif SelectCx3 in (lbm):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments lbm")
                elif SelectCx3 in (limorb):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments limorb")
                elif SelectCx3 in (lipo):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments lipo")
                elif SelectCx3 in (mamilla):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mamilla")
                elif SelectCx3 in (maoz):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments maoz")
                elif SelectCx3 in (marcel):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments marcel")
                elif SelectCx3 in (marome):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments marome")
                elif SelectCx3 in (matanis):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments matanis")
                elif SelectCx3 in (mayas):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mayas")
                elif SelectCx3 in (mazor):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments mazor")
                elif SelectCx3 in (medassist):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments medassist")
                elif SelectCx3 in (meyero):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments meyero")
                elif SelectCx3 in (neshai):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments neshai")
                elif SelectCx3 in (orenw):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments orenw")
                elif SelectCx3 in (orits):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments orits")
                elif SelectCx3 in (r1test):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments r1test")
                elif SelectCx3 in (rbn):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rbn")
                elif SelectCx3 in (rdgw):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rdgw")
                elif SelectCx3 in (regev):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments regev")
                elif SelectCx3 in (revitalc):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments revitalc")
                elif SelectCx3 in (roqa):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments roqa")
                elif SelectCx3 in (roqa2):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments roqa2")
                elif SelectCx3 in (rosales):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rosales")
                elif SelectCx3 in (rots3):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments rots3")
                elif SelectCx3 in (sarita):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments sarita")
                elif SelectCx3 in (shahwan):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments shahwan")
                elif SelectCx3 in (shine):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments shine")
                elif SelectCx3 in (tenecare):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments tenecare")
                elif SelectCx3 in (tessone):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments tessone")
                elif SelectCx3 in (theclinic):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments theclinic")
                elif SelectCx3 in (tiratz):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments tiratz")
                elif SelectCx3 in (yaelh):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments yaelh")
                elif SelectCx3 in (yoavy):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments yoavy")
                elif SelectCx3 in (yosefm):
                        os.system(R"powershell.exe cd C:\users\vlad\desktop")
                        os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments yosefm")
                exit(0)

#M4U Live2
        if Version in Live2:
            if ChooseServer in M4U:
                    for item in M4U_LIST:
                        print(item)
                    SelectCx4 = input("Select Customer ID:")
                    if SelectCx4 in (All, amirw, amor, angio, anneruth, anuchka, arbel, athletic, aviramb, barakl, barziv, beautyc, beautyclass, bellac, bestmedical, betterlife, bina, borochov, briuta, brodsky, btl, cantek, danab, deadsea, deborac, ecopolitan, emsplus, epilogic, epos, espada, exper, femi, guyg, hadari, haddada, healthyaging, herzala, hescular, icekson, juc, juvenus, kalus, kesem, krupnik, kubiyot, kuperman, labriut, lemaanam, levid, lightc, mbcosmetic, moon, morbeauty, morlaser, mtc, naturaclinic ,naturclinic, newmedic, nitza, novotalk, ofery, orasis, orc, pearlynn, physio, proacademy, protea, psagot, qmedical, rc, raz, rebeccav, rustam, sharap, shechter, shiloah, sil, simono, slovak, smadarp, social, solomon, styledent, tamarh, terem, tivot, top, tzaad, virtuoz, vtc, winkler, yaelj, yardenc, yoava, borochov, faceboutique, advmedworld):
                        print('Updaing..')
                    if SelectCx4 in (amirw):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R73_amirw")
                    elif SelectCx4 in (amor):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R09_Amor")
                    elif SelectCx4 in (All):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments")
                    elif SelectCx4 in (angio):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R70_Angio")
                    elif SelectCx4 in (anuchka):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R14_Anuchka")
                    elif SelectCx4 in (arbel):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R31_Arbel")
                    elif SelectCx4 in (athletic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R27_Athletic")
                    elif SelectCx4 in (aviramb):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R74_AviramB")
                    elif SelectCx4 in (barakl):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R06_BarakL")
                    elif SelectCx4 in (barziv):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R89_Barziv")
                    elif SelectCx4 in (beautyc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R34_BeautyC")
                    elif SelectCx4 in (beautyclass):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R66_BeautyClass")
                    elif SelectCx4 in (bestmedical):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R48_Bestmedical")
                    elif SelectCx4 in (betterlife):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R44_BetterLife")
                    elif SelectCx4 in (bina):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R36_Bina")
                    elif SelectCx4 in (borochov):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R90_Borochov")
                    elif SelectCx4 in (briuta):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R76_Briuta")
                    elif SelectCx4 in (brodsky):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R47_Brodsky")
                    elif SelectCx4 in (btl):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R21_BTL")
                    elif SelectCx4 in (cantek):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R08_Cantek")
                    elif SelectCx4 in (danab):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R42_Danab")
                    elif SelectCx4 in (deadsea):
                            print('No Database to update')
                    elif SelectCx4 in (deborac):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R38_DeboraC")
                    elif SelectCx4 in (ecopolitan):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R72_Ecopolitan")
                    elif SelectCx4 in (emsplus):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R12_EMSPlus")
                    elif SelectCx4 in (epilogic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments epilogic")
                    elif SelectCx4 in (epos):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R80_Epos")
                    elif SelectCx4 in (espada):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R62_Espada")
                    elif SelectCx4 in (exper):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R82_Exper")
                    elif SelectCx4 in (femi):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R15_Femi")
                    elif SelectCx4 in (guyg):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R81_GuyG")
                    elif SelectCx4 in (hadari):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R50_Hadari")
                    elif SelectCx4 in (haddada):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R63_HaddadA")
                    elif SelectCx4 in (healthyaging):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R24_HealthyAging")
                    elif SelectCx4 in (herzala):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R58_Herzala")
                    elif SelectCx4 in (hescular):
                            print('No Database to update')
                    elif SelectCx4 in (icekson):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R22_Icekson")
                    elif SelectCx4 in (juc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R56_JUC")
                    elif SelectCx4 in (juvenus):
                            print('No Database to update..')
                    elif SelectCx4 in (kalus):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R26_Kalus")
                    elif SelectCx4 in (kesem):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R60_Kesem")
                    elif SelectCx4 in (krupnik):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R30_Krupnik")
                    elif SelectCx4 in (kubiyot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R87_Kubiyot")
                    elif SelectCx4 in (kuperman):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R59_Kuperman")
                    elif SelectCx4 in (labriut):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R20_Labriut")
                    elif SelectCx4 in (lemaanam):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R04_Lemaanam")
                    elif SelectCx4 in (levid):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R64_LeviD")
                    elif SelectCx4 in (lightc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R11_LightC")
                    elif SelectCx4 in (mbcosmetic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R49_MBCosmetic")
                    elif SelectCx4 in (moon):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R83_Moon")
                    elif SelectCx4 in (morbeauty):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R10_MorBeauty")
                    elif SelectCx4 in (morlaser):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R23_Morlaser")
                    elif SelectCx4 in (mtc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R78_MTC")
                    elif SelectCx4 in (naturaclinic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R41_Naturaclinic")
                    elif SelectCx4 in (naturclinic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R41_Naturaclinic")
                    elif SelectCx4 in (newmedic):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R57_Newmedic")
                    elif SelectCx4 in (nitza):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R37_Nitza")
                    elif SelectCx4 in (novotalk):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R92_Novotalk")
                    elif SelectCx4 in (ofery):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R32_OferY")
                    elif SelectCx4 in (orasis):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R28_Orasis")
                    elif SelectCx4 in (orc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R85_OrC")
                    elif SelectCx4 in (pearlynn):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R91_Pearlynn")
                    elif SelectCx4 in (physio):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R51_Physio")
                    elif SelectCx4 in (proacademy):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R33_ProAcademy")
                    elif SelectCx4 in (protea):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R77_Protea")
                    elif SelectCx4 in (psagot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R54_Psagot")
                    elif SelectCx4 in (qmedical):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R86_QMedical")
                    elif SelectCx4 in (rc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R88_RC")
                    elif SelectCx4 in (raz):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R07_Raz")
                    elif SelectCx4 in (rebeccav):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R35_RebeccaV")
                    elif SelectCx4 in (rustam):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R52_Rustam")
                    elif SelectCx4 in (sharap):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R53_Sharap")
                    elif SelectCx4 in (shechter):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R46_Shechter")
                    elif SelectCx4 in (shiloah):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R84_Shiloah")
                    elif SelectCx4 in (sil):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R25_Sil")
                    elif SelectCx4 in (simono):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R18_SimonO")
                    elif SelectCx4 in (slovak):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R79_Slovak")
                    elif SelectCx4 in (smadarp):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments Smadarp")
                    elif SelectCx4 in (social):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R75_Social")
                    elif SelectCx4 in (solomon):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R68_Solomon")
                    elif SelectCx4 in (styledent):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R40_StyleDent")
                    elif SelectCx4 in (tamarh):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R43_TamarH")
                    elif SelectCx4 in (terem):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R55_Terem")
                    elif SelectCx4 in (tivot):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R19_tivot")
                    elif SelectCx4 in (top):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R67_Top")
                    elif SelectCx4 in (tzaad):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R16_Tzaad")
                    elif SelectCx4 in (virtuoz):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R17_Virtuoz")
                    elif SelectCx4 in (vtc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R45_VTC")
                    elif SelectCx4 in (winkler):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R39_Winkler")
                    elif SelectCx4 in (yaelj):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R29_YaelJ")
                    elif SelectCx4 in (yardenc):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R65_YardenC")
                    elif SelectCx4 in (yoava):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R05_YoavA")
                    elif SelectCx4 in (borochov):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R90_borochov")
                    elif SelectCx4 in (faceboutique):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R97_Faceboutique")
                    elif SelectCx4 in (anneruth):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R13_AnneRuth")
                    elif SelectCx4 in (advmedworld):
                            os.system(R"powershell.exe cd c:\scripts")
                            os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition RapidOne_Version350 -forceConfig -deployEnvironments R106_advmedworld")
                    exit(0)