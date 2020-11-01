# Exercise:
# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), 
# and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:
# Ask the user to specify the name of the output file that will be saved.


from bs4 import BeautifulSoup
import requests


def obtain_data():
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "html.parser")
    all_span = soup.find_all("p")
    data = ""

    for span in all_span:
        title = span.text.strip()
        data = data + "\n" + title

    return data


def write_file(file_name, data):
    with open(file_name + '.txt', 'w') as open_file:
        open_file.write(data)

def run():
    
    file_name = input("Please inset the file name to use: ")

    data = obtain_data()    
    write_file(file_name, data)

if __name__ == "__main__":
    run()


