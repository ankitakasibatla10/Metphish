from flask import Flask, render_template, redirect, url_for, request
import flask
from flask import Flask, render_template, redirect, url_for, flash, abort

from flask import Flask, render_template, redirect, url_for, request
import flask
from flask import Flask, render_template, redirect, url_for, flash, abort

from werkzeug.utils import secure_filename
import uuid as uuid
import os

a = " some_string"

app = Flask(__name__, template_folder="template")
app.app_context().push()
UPLOAD_FOLDER='static/csvfiles'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER


@app.route("/choosefile", methods=["GET", "POST"])
def choosefile():

    if request.method == "POST":
        File = request.files.get("filename")
        File_filename = secure_filename(File.filename)
        File_name = str(uuid.uuid1()) + "_" + File_filename
        File.save(os.path.join(app.config['UPLOAD_FOLDER'], File_name))
        File = File_name
        print(File)


    return render_template("choosefile.html")

def hello(a):
    print(a)
    file1 = open("file.csv", "w")  # write mode
    file1.write(a)
    file1.close()

    file1 = open("file.csv", "r")

    print(file1.read())

    file1.close()

link=""

@app.route("/" ,methods=["GET", "POST"])
def welcome():
    global link
    if request.method=="POST":
        link=request.form.get("url")



    return render_template("index.html")

@app.route("/team" )
def team():
    return render_template("Team.html")


if __name__ == "__main__":
    app.run(debug=True)
app.app_context()

# if (expiration_date is None):
#     return 1
# elif (type(expiration_date) is list):

#     return 1

# else:

#     today = datetime.now()
#     end = abs((expiration_date - today).days)
#     if ((end/30) < 6):
#       end = 0
#     else:
#       end = 1
#   return end

import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from urllib import *

from bs4 import BeautifulSoup

import requests

import re

import csv

# import warnings
# warnings.filterwarnings('ignore')
# import socket
# socket.getaddrinfo('localhost', 8080)


# print("Accuracy is :",accuracy_score(y_test,y_pred))
# a = "milpitaslions.com"

"""## 3.3. HTML and JavaScript based Features

Many features can be extracted that come under this category. Out of them, below mentioned were considered for this project.

*   IFrame Redirection
*   Status Bar Customization
*   Disabling Right Click
*   Website Forwarding

Each of these features are explained and the coded below:
"""

# importing required packages for this section
import requests

"""### 3.3.1. IFrame Redirection

IFrame is an HTML tag used to display an additional webpage into one that is currently shown. Phishers can make use of the “iframe” tag and make it invisible i.e. without frame borders. In this regard, phishers make use of the “frameBorder” attribute which causes the browser to render a visual delineation. 

If the iframe is empty or repsonse is not found then, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""


# 15. IFrame Redirection (iFrame)
def iframe(response):
    if response == "":
        return 1
    else:
        if re.findall(r"[<iframe>|<frameBorder>]", response.text):
            return 0
        else:
            return 1


# 16.Checks the effect of mouse over on status bar (Mouse_Over)
def mouseOver(response):
    if response == "":
        return 1
    else:
        if re.findall("<script>.+onmouseover.+</script>", response.text):
            return 1
        else:
            return 0


"""### 3.3.3. Disabling Right Click

Phishers use JavaScript to disable the right-click function, so that users cannot view and save the webpage source code. This feature is treated exactly as “Using onMouseOver to hide the Link”. Nonetheless, for this feature, we will search for event “event.button==2” in the webpage source code and check if the right click is disabled.

If the response is empty or onmouseover is not found then, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""


# 17.Checks the status of the right click attribute (Right_Click)
def rightClick(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 0
        else:
            return 1


# 18.Checks the number of forwardings (Web_Forwards)
def forwarding(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1


"""## 4. Computing URL Features

Create a list and a function that calls the other functions and stores all the features of the URL in the list. We will extract the features of each URL and append to this list.
"""


# 1.Domain of the URL (Domain)


def getDomain(url):
    domain = urllib.parse.urlparse(url).netloc
    if re.match(r"^www.", domain):
        domain = domain.replace("www.", "")
    return domain


# 2.Checks for IP address in URL (Have_IP)
def havingIP(url):
    try:
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip


# 3.Checks the presence of @ in URL (Have_At)
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at


# 4.Finding the length of URL and categorizing (URL_Length)
def getLength(url):
    if len(url) < 54:
        length = 0
    else:
        length = 1
    return length


"""#### 3.1.5. Depth of URL

Computes the depth of the URL. This feature calculates the number of sub pages in the given url based on the '/'.

The value of feature is a numerical based on the URL.
"""


# 5.Gives number of '/' in URL (URL_Depth)
def getDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
        if len(s[j]) != 0:
            depth = depth + 1
    return depth


# 6.Checking for redirection '//' in the url (Redirection)
def redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0


# 7.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)
def httpDomain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0


"""#### 3.1.8. Using URL Shortening Services “TinyURL”

URL shortening is a method on the “World Wide Web” in which a URL may be made considerably smaller in length and still lead to the required webpage. This is accomplished by means of an “HTTP Redirect” on a domain name that is short, which links to the webpage that has a long URL. 

If the URL is using Shortening Services, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""

# listing shortening services
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"


# 8. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0


# 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1  # phishing
    else:
        return 0  # legitimate


"""### 3.2. Domain Based Features:

Many features can be extracted that come under this category. Out of them, below mentioned were considered for this project.

*   DNS Record
*   Website Traffic 
*   Age of Domain
*   End Period of Domain

Each of these features are explained and the coded below:
"""

# !pip install python-whois

# importing required packages for this section
import re
from bs4 import BeautifulSoup
# import whois
import urllib
import urllib.request

from urllib.parse import urlparse
from datetime import datetime


# 12.Web traffic (Web_Traffic)
def web_traffic(url):
    try:
        # Filling the whitespaces in the URL if any
        url = urlparse(url)
        rank = \
        BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
            "REACH")['RANK']
        rank = int(rank)
    except TypeError:
        return 1
    if rank < 100000:
        return 1
    else:
        return 0


# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
def domainAge(domain_name):
    creation_date = domain_name.creation_date
    expiration_date = domain_name.expiration_date
    if (isinstance(creation_date, str) or isinstance(expiration_date, str)):
        try:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1
    if ((expiration_date is None) or (creation_date is None)):
        return 1
    elif ((type(expiration_date) is list) or (type(creation_date) is list)):
        return 1
    else:
        ageofdomain = abs((expiration_date - creation_date).days)
        if ((ageofdomain / 30) < 6):
            age = 1
        else:
            age = 0
    return age


"""#### 3.2.4. End Period of Domain

This feature can be extracted from WHOIS database. For this feature, the remaining domain time is calculated by finding the different between expiration time & current time. The end period considered for the legitimate domain is 6 months or less  for this project. 

If end period of domain > 6 months, the vlaue of this feature is 1 (phishing) else 0 (legitimate).
"""


# 14.End time of domain: The difference between termination time and current time (Domain_End)
def domainEnd(domain_name):
    expiration_date = domain_name.expiration_date
    if isinstance(expiration_date, str):
        try:
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1


# 12.Web traffic (Web_Traffic)
def web_traffic(url):
    try:
        # Filling the whitespaces in the URL if any
        url = urllib.parse.quote(url)
        rank = \
        BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
            "REACH")['RANK']
        rank = int(rank)
    except TypeError:
        return 1
    if rank < 100000:
        return 1
    else:
        return 0


# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
def domainAge(domain_name):
    creation_date = domain_name.creation_date
    expiration_date = domain_name.expiration_date
    if (isinstance(creation_date, str) or isinstance(expiration_date, str)):

        try:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1
    if ((expiration_date is None) or (creation_date is None)):
        return 1
    elif ((type(expiration_date) is list) or (type(creation_date) is list)):
        return 1
    else:
        ageofdomain = abs((expiration_date - creation_date).days)
        if ((ageofdomain / 30) < 6):
            age = 1
        else:
            age = 0

        return age


# Function to extract features
def featureExtraction(url):
    features = []
    # Address bar based features (10)
    #   features.append(getDomain(url))
    features.append(havingIP(url))
    features.append(haveAtSign(url))
    features.append(getLength(url))
    features.append(getDepth(url))
    features.append(redirection(url))
    features.append(httpDomain(url))
    features.append(tinyURL(url))
    features.append(prefixSuffix(url))

    # Domain based features (4)
    #   dns = 0
    #   try:
    #     domain_name = whois.whois(urlparse(url).netloc)
    #   except:
    #     dns = 1

    #   features.append(dns)
    #   features.append(web_traffic(url))
    #   features.append(1 if dns == 1 else domainAge(domain_name))
    #   features.append(1 if dns == 1 else domainEnd(domain_name))

    # HTML & Javascript based features
    try:
        response = requests.get(url)
    except:
        response = ""

    features.append(iframe(response))
    features.append(mouseOver(response))
    features.append(rightClick(response))
    features.append(forwarding(response))

    return features


data = pd.read_csv("Hack.csv")

data1 = data.drop(['Domain'], axis=1).copy()
y = data1['Label']
X = data1.drop('Label', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=([100, 100, 100]))
mlp.fit(X_train, y_train)

data2 = pd.read_csv("insta.csv")

df = pd.DataFrame(data2)

x = data2.drop(['Domain'], axis=1)

y_pred = mlp.predict(x)

# print()
print(y_pred)

url =link

# //random forest

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(random_state=10, max_depth=7)

forest.fit(X_train, y_train)

phished_value = 1

if phished_value in y_pred:

    np_array = np.array(y_pred)

    arr = np.array(y_pred)

    x = np.where(arr == phished_value)

    link = df.iloc[x]['Domain'].astype(str).tolist()

    # print(link)

    with open("RandomForest.csv", "w") as Rfile:

        cols = ["Domain", "Have_IP", "Have_At", "URL_Length", "URL_Depth", "Redirection", "https_Domain", "TinyURL",
                "Prefix/Suffix", "iFrame", "Mouse_Over", "Right_Click", "Web_Forwards"]

        writer = csv.writer(Rfile)

        writer.writerow(cols)

        for j in link:

            if "https://" in j:

                pass

            elif "http://" in j:

                pass

            else:
                # url.strip("http://")

                j = "https://" + j

            j = "https://www.comnetwork.org/newsletter-archive/"


            def htmlContent(j):

                response = requests.get(j)

                return response.text


            html_document = htmlContent(j)

            soup = BeautifulSoup(html_document, 'html.parser')

            image_data = []

            images = soup.select('img')

            for image in images:
                src = image.get('src')
                alt = image.get('alt')
                image_data.append({"src": src, "alt": alt})

            print(image_data)

            all_links = []

            links = soup.select('a')

            for reference_tags in links:
                text = reference_tags.text
                text = text.strip()

                tags = reference_tags.get('href')

                tags = tags.strip()

            all_links.append({"text": text, "tags": tags})

            print(all_links)

    #         for i in  soup.find_all('a', href=True):

    #             #print(i["href"])

    #             # np.array(featureExtraction(j))

    #             # print(np.asarray([featureExtraction(j)]))
    #             scrapped_links = []

    #             domain_names = []

    #             domain_names.append(f'{i["href"]}')

    #             for l in domain_names:

    #                 if "https://" not in l:

    #                     domain_names.remove(l)

    #             print(domain_names)

    #             for k in np.array(featureExtraction(j)):

    #                 a = int(k)

    #                 scrapped_links.append(a)

    #             over = domain_names + scrapped_links

    #             csv.writer(Rfile).writerow(over)

    # time.sleep(10)

    # randomForestData  = pd.read_csv("RandomForest.csv")

    # df1 = pd.DataFrame(randomForestData)

    # y = randomForestData.drop(['Domain'], axis=1)

    # y_test_forest = forest.predict(y)

    # deep = mlp.predict(y)

    # print(y_test_forest)

    # print(deep)

    # domain_names.append(j)

    # print(list2)

    # np.savetxt("RandomForest.csv" , (np.ceil(np.asarray([featureExtraction(j)])).astype(int)), delimiter=",")

    # np.savetxt("RandomForest.csv" , [list2], delimiter=",")

    # np.savetxt("RandomForest.csv" , int()  ,  end = '')

    # [     ]
    # Rfile.write(f'{i} , np.savetxt("RandomForest.csv" ,  featureExtraction(i), delimiter=","))')

    # def htmlContent(link):

    #     response = requests.get(link)

    #     return response.text

    # index_phish = y_pred.where(np_array == phished_value)[11]

    # link = data2['Domain'][index_phish]

    # print(link)

    # def getHtml(link):

    # response = requests.get(url)

    # return response.txt

# url1 = "instagram.com"

# l = featureExtraction(url1)

# print(l)


# url2 = "twitter.com"

# l2 = featureExtraction(url2)

# print(l2)


# print(X_test)
# url1 = "instagram.com"


# with open("user.csv" , "w") as file:

#     file.write(url1)

# l = featureExtraction(url1)

# print(accuracy_score(y_test, y_pred))


# arr = np.array(l , dtype=float)


# print(l)

# y_userpred = mlp.predict([l])

# print(y_pred)

# print(y_userpred)


# with open("phish.csv" , "w") as file:

#     file.write(url)


# converting the list to dataframe

feature_names = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection', 'https_Domain', 'TinyURL',
                 'Prefix/Suffix', 'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards', 'Label']


