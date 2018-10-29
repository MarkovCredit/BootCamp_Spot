
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import splinter
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


# In[126]:
def scrape():


    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    mars_dict = {}


    # In[3]:


    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[4]:


    


    browser.visit(url)


    # In[6]:


    html = browser.html


    # In[7]:


    soup_1 = BeautifulSoup(html,'html.parser')


    # In[8]:

    #For loop if i want to display all the results
    results = soup_1.find_all('li', class_='slide')
    title_list = []
    para_list = []

    for result in results[0]:
        
        news_title = result.find('h3').text
        news_p = result.find('div', class_='rollover_description').text
        title_list.append(news_title)
        para_list.append(news_p)
        
        
        # print(f'----Printing article {i}-----')
        # print(news_title)
        # print(news_p)
        # i += 1
        


    # In[9]:



    #articles_dict = dict(zip(title_list[0],para_list[0]))
    #Just need the latest results
    article_latest = news_title+":  "+news_p
    

    # In[145]:


    mars_dict['article'] = article_latest
    


    # In[10]:


    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    html2 = browser.html


    # In[11]:


    soup_2 = BeautifulSoup(html2,'html.parser')
    print(soup_2)


    # In[168]:


    
    results_2 = soup_2.find('div', {'class': 'carousel_items'}).find('article')

    # for img in results_2:
    #     print(img['src'])
    cover_photo = results_2['style']
    cover_photo_2 = cover_photo.split(':')[1]
    cover_photo_link = cover_photo_2.split('\'')[1]
    cover_url = 'https://www.jpl.nasa.gov'+cover_photo_link
    cover_url
    mars_dict['cover_photo'] = cover_url


    # #Mars Weather Tweets

    # In[13]:


    twitter_url = 'https://twitter.com/marswxreport?lang=en'


    # In[14]:


    browser.visit(twitter_url)
    html = browser.html
    soup_t = BeautifulSoup(html,'html.parser')


    # In[15]:



    tweets = [p.text for p in soup_t.findAll('p', class_='tweet-text')]
    latest_tweet = tweets[0]
    print(latest_tweet)


    # In[169]:


    mars_dict['Weather'] = latest_tweet


    # #Mars Facts -- pull down tabular data, convert to table and then convert to HTML table string

    # In[16]:


    mars_f_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_f_url)
    df = tables[0]
    df.rename(columns={0: 'Desc', 1: 'Value'})
        # In[17]:


    html_table = df.to_html()
    html_table.replace('\n','')


    # In[170]:


    mars_dict['mars_table'] = html_table


    # #Mars Hemispheres

    # In[18]:


    mars_enh_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    # In[20]:




    browser.visit(mars_enh_url)
    html3 = browser.html

    #print(soup_2)


    # In[22]:


    soup_3 = BeautifulSoup(html3,'html.parser')


    # In[118]:


    soup_3_pages = soup_3.find("div",{"id":"product-section"}).find_all("div",{"class":"item"})


    # In[44]:


    titles = [h3.text for h3 in soup_3.findAll('h3')]
    titles


    # In[125]:


    base_url = 'https://astrogeology.usgs.gov'


    url_list = []

    for x in soup_3_pages:
        image_url = x.find('a')['href']
        image_full_url = base_url + image_url
        title = x.find("div",{"class":"description"}).find("a").find("h3").text
        #visit each page    
        browser.visit(image_full_url)
        soup_img = BeautifulSoup(browser.html,"html.parser")
        img_items = soup_img.find("div",{"class":"downloads"})
        image_link = img_items.find("li").find("a")["href"]
        #store in dictionary and then append into list
        url_d = {'Title': title, 'Url': image_link}
        url_list.append(url_d)
        
        


    
    # In[171]:


    mars_dict['mars_hemis'] = url_list


    # In[172]:

    browser.quit()
    return mars_dict

