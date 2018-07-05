from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def find_answers(soup, counter):
    """
    Goes through the soup object to find all divs that contain the answer class (Answer AnswerBase) then searches within
    those tags for the <p> tags which contain the actual text for the answer and then creates a new txt file which
    contains that text
    :param soup: the soup object from BeautifulSoup and allows for the parsing of the website
    :return: returns the count of how many text files have been made so more files can continue to be made
    """
    divs = soup.find_all("div", class_="Answer AnswerBase")  # finds all the div tags with the answer class
    for d in divs:
        answers = d.find_all("p")  # within the span tags finds all the paragraph tags so answers can be kept together
        counter += 1
        with open("Text" + str(counter) + ".txt", "w+") as f:
            for a in answers:
                f.write(a.text)  # writes each answer in a separate text file
                f.write("\n")
    return counter

def soup_given_url(given_url):
    """
    Takes in a url then using the BeautifulSoup library, creates a soup object which then can be parsed
    :param given_url: the url which you wish to go to and create the soup object from
    :return: returns the soup object back to main so it can be worked with and parsed
    """
    url = given_url
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")
    return soup


def scroll_page(no_of_pagedowns, elem):
    '''
    scrolls down the browser page to get more linkg
    :param no_of_pagedowns: the number of pages you want to scroll
    :param elem: the element that contains the scroll idk
    :return:
    '''
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no_of_pagedowns -= 1


def get_urls_list(browser):
    '''
    finds the wanted links in the browser
    :param browser: the browser object
    :return: the list of urls of the questions
    '''
    list = []
    post_elems = browser.find_elements_by_class_name("question_link")
    for post in post_elems:
        list.append(post.get_attribute('href'))
    return list


def main(topic):
    '''
    main function calls all the other functions and creates the text files with answers
    :param topic: the topic in quora
    '''
    driverLocation = '/home/kevin/Desktop/chromedriver_linux64/chromedriver'
    browser = webdriver.Chrome(driverLocation)

    browser.get("https://www.quora.com/topic/"+topic+ "/all_questions")
    time.sleep(1)

    scroll_page(2, browser.find_element_by_tag_name("body"))

    urls = get_urls_list(browser)
    #print(urls)

    count = 0
    for url in urls:
        soup = soup_given_url(url)
        count = find_answers(soup, count)



main(str('Experiences-in-Life'))