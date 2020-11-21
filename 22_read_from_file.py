# Exercise:
# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 
# I have a .txt file for you, if you want to use it!

# Extra:
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image 
# there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy 
# for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going 
# to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.


# with open('names.txt', 'r') as open_file:
#     all_text = open_file.read()

def run():
    # No-extra solution
    # names = {}

    # with open('names.txt', 'r') as open_file:
    #     line = open_file.readline()
    #     while line:
    #         line = line.strip()
    #         if line in names.keys():
    #             names[line] += 1
    #         else:
    #             names[line] = 1
    #         line = open_file.readline()

    # print(names)

    #Extra solution
    categories = {}

    with open("extra.txt", "r") as file:
        line = file.readline()
        while line:
            line = line.strip()
            category = line.split("/")[2]
            if category in categories.keys():
                categories[category] += 1
            else:
                categories[category] = 1
            line = file.readline()
    
    print(categories)
    	

if __name__ == "__main__":
    run()