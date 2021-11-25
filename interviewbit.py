from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://www.interviewbit.com/google-interview-questions/").text
#print(html_text)

soup = BeautifulSoup(html_text, 'html.parser')

section = soup.find('section', class_='fourth-section')

jobs = section.find('div', class_='container')
#print(jobs)
for link in jobs.find_all('a'):
    print("https://www.interviewbit.com" +link.get('href'))

#company_name = jobs.find_all('h3', class_ ='joblist-comp-name').text.replace(' ','')
#print(company_name)
#skills = jobs.find(class_ ='spr-skills')
#print(skills)
