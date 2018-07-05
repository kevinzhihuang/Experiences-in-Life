from bs4 import BeautifulSoup
import urllib.request


def find_answers(soup, counter):
    divs = soup.find_all("div", class_="Answer AnswerBase")  # finds all the div tags
    for d in divs:
        answers = d.find_all("p")  # within the span tags finds all the paragraph tags so answers can be kept together
        counter += 1
        with open("Text" + str(counter) + ".txt", "w+") as f:  # need to add in an if statement since some spans empty
            for a in answers:
                f.write(a.text)  # writes each answer in a separate text file, though some are empty cause no text
                f.write("\n")
    return counter

def soup_given_url(given_url):
    url = given_url
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")
    return soup


def main():
    url = ["https://www.quora.com/Have-you-ever-had-someone-react-negatively-or-strangely-to-your-name",
           "https://www.quora.com/People-who-enter-homes-for-a-living-Maintenance-cable-contractors-etc-what-s-the"
           "-strangest-thing-you-ve-encountered-when-entering-someone-s-home",
           "https://www.quora.com/What-is-the-most-difficult-thing-you-ever-faced-as-a-teen"]
    count = 0
    for u in url:
        soup = soup_given_url(u)
        count = find_answers(soup, count)

main()
