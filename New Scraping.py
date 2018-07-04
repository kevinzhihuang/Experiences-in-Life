from bs4 import BeautifulSoup
import urllib.request


def find_answers(soup):
    text = soup.find_all("p", class_="ui_qtext_para")

    for t in text:
        print(t.text.strip())


url = "https://www.quora.com/What-is-the-biggest-mistake-you-can-avoid-taking-care-of-a-newborn"
content = urllib.request.urlopen(url)
soup = BeautifulSoup(content, "html.parser")
count = 0

#find_answers(soup) this function finds all the text and prints it

spans = soup.find_all("span", class_ = "ui_qtext_rendered_qtext") #finds all the span tags
for s in spans:
    answers = s.find_all("p") #within the span tags finds all the paragraph tags so answers can be kept together
    count += 1
    with open("Test" + str(count) + ".txt", "w+") as f: #need to add in an if statement since some spans empty
        for a in answers:
            print(a.text)
            f.write(a.text) #writes each answer in a separate text file, though some are empty cause no text

