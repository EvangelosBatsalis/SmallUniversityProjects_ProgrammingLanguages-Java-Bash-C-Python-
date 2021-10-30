#!/usr/bin/env python3

"""

Άσκηση: Αναζήτηση αναρτήσεων στη «διαύγεια»

H γνωστή ιστοσελίδα ανάρτησης πράξεων της δημόσιας διοίκησης στο διαδίκτυο (http://diavgeia.gov.gr) παρέχει υπηρεσία rss feed (βλέπε: https://diavgeia.gov.gr/blog/?p=116). Να κατασκευάσετε εφαρμογή που να επιτρέπει στον χρήστη να αναζητήσει τις τελευταίες πράξεις κάποιου δημόσιου φορέα.
"""

import re
import urllib.request
import urllib.error
import csv

arxes = {}

def rss_feed(url): #3 μονάδες *
    '''
    Άνοιγμα του rss feed,
    :param url: η διεύθυνση του rss feed.
    Αυτή η συνάρτηση δημιουργεί ένα αρχείο
    με τα περιεχόμενα του rss_feed με όνομα
    την διεύθυνση του rss feed.
    Καλεί την συνάρτηση process_feed
    η οποία επιλέγει και τυπώνει περιεχόμενο
    Προσπαθήστε να κάνετε try/except τα exceptions
    HTTPError και URLError.
    '''
    #σύμφωνα με την ανακοίνωση της διαύγειας τα rss feeds είναι στο ίδιο url/rss
    url += r"/rss"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            char_set = response.headers.get_content_charset()
            rss = response.read().decode(char_set)
    except urllib.error.HTTPError as e:
        print('Σφάλμα HTTP: ', e.code)
    except urllib.error.URLError as e:
        print('Αποτυχία σύνδεσης στον server')
        print('Αιτία:', e.reason)
    else:
        with open("chosen_rss", "w", encoding = "utf-8") as f:
            f.write(rss)
        process_feed("chosen_rss")

def process_date(date): #2 μονάδες
    '''
    η συνάρτηση διαμορφώνει την ελληνική ημερομηνία του rss feed:
    Στο rss αρχείο η ημερομηνία είναι της μορφής: Wed, 14 Jun 2017 17:21:16 GMT
    Θα πρέπει να διαμορφώνεται σε ελληνική ημερομηνία, πχ: Τετ, 14 Ιουν 2017
    :param date:
    :return: η ελληνική ημερομηνία
    '''
    days = {
    "Mon," : "Δευ,",
    "Tue," : "Τρι,",
    "Wed," : "Τετ,",
    "Thu," : "Πεμ,",
    "Fri," : "Παρ,",
    "Sat," : "Σαβ,",
    "Sun," : "Κυρ,"
    }

    months = {
    "Jan" : "Ιαν",
    "Feb" : "Φεβ",
    "Mar" : "Μαρ",
    "Apr" : "Απρ",
    "May" : "Μαι",
    "Jun" : "Ιουν",
    "Jul" : "Ιουλ",
    "Aug" : "Αυγ",
    "Sep" : "Σεπ",
    "Oct" : "Οκτ",
    "Nov" : "Νοε",
    "Dec" : "Δεκ"
    }

    date = date[0].split()[:4]
    for i in date:
        if i in days.keys():
            date[date.index(i)] = days[i]
    for i in date:
        if i in months:
            date[date.index(i)] = months[i]
    print("ΗΜΕΡΟΜΗΝΙΑ:", " ".join(date).rstrip())

def process_feed(filename): #3 μονάδες *
    '''
    συνάρτηση που ανοίγει το αρχείο με το rss feed και 
    τυπώνει την ημερομηνία και τους τίτλους των αναρτήσεων που περιέχει.
    Xρησιμοποιήστε regular expressions 
    '''
    global date
    with open(filename, 'r', encoding = 'utf-8') as f:
        xml=f.read()
        xml=xml.replace("\n","")
        date_pattern = '<lastBuildDate>(.*)</lastBuildDate>'
        title_pattern = '<title>(.*?)</title>'
        date = re.findall(date_pattern, xml, re.MULTILINE | re.IGNORECASE)
        title = re.findall(title_pattern, xml, re.MULTILINE | re.IGNORECASE)
    process_date(date)
    print(3*"+" + "  " + title[0] + "  " + 3*"+")
    count = 1
    for praxi in title[1:]:
        print(count, "\t", praxi)
        count += 1
def search_arxes(arxh): #2 μονάδες
    '''
    Αναζήτηση ονόματος Αρχής που ταιριάζει στα κριτήρια του χρήστη
    '''
    matches=[]
    for k in arxes.keys():
        pattern=arxh
        if re.search(pattern, k, re.I):
            matches.append(k)
    return matches

def load_arxes(): #2 μονάδες
    '''
    φορτώνει τις αρχές στο λεξικό arxes{}
    '''
    with open("500_arxes.csv") as csvfile:
        stoixeia = csv.reader(csvfile, delimiter = ';')
        for row in stoixeia:
            arxes[row[0]]=row[1]
    return arxes

######### main ###############
'''
το κυρίως πρόγραμμα διαχειρίζεται την αλληλεπίδραση με τον χρήστη
'''
load_arxes()
while True :
    arxh = input(50*"^"+"\nΟΝΟΜΑ ΑΡΧΗΣ:(τουλάχιστον 3 χαρακτήρες), ? για λίστα:")
    if arxh == '':
        break
    elif arxh == "?": # παρουσιάζει τα ονόματα των αρχών
        for k,v in arxes.items():
            print (k,v)
    elif len(arxh) >= 3 :
        # αναζητάει όνομα αρχής που ταιριάζει στα κριτήρια του χρήστη
        result = search_arxes(arxh) 
        for r in result:
            print (result.index(r)+1, r, arxes[r])
        while result:
            epilogh = input("ΕΠΙΛΟΓΗ....")
            if epilogh == "": break
            elif epilogh.isdigit() and 0<int(epilogh)<len(result)+1:
                epilogh = int(epilogh)
                url = arxes[result[epilogh-1]]
                print(url)
                # καλεί τη συνάρτηση που φορτώνει το αρχείο rss:
                rss_feed(url)
            else: continue
    else :
        continue
