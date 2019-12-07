from selenium import webdriver
import requests

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Chrome(executable_path=r"C:\Users\Admin\Downloads\chromedriver.exe")
    browser.get(url)
    links = []
    find_tag = browser.find_elements_by_tag_name('a')
    for x in find_tag:
        links.append(x.get_attribute('href'))
    browser.close()
    return links

urllist = get_links("https://cpske.github.io/ISP/")
def invalid_urls(urllist):
    invalid_list = []
    for ivl in urllist:
        get_head = requests.head(ivl)
        if get_head.status_code == 404:
            invalid_list.append(ivl)
    return invalid_list

if __name__ == "__main__":
    for x in urllist:
        print(x)
    invalidlist = invalid_urls(urllist)
    for x in invalidlist:
        print(x)
