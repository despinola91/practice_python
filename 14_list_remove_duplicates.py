# Exercise:
# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def clean_duplicates_loop(original_list):
    new_list = list()
    for elem in original_list:
        if elem not in new_list:
            new_list.append(elem)

    return new_list

def clean_duplicates_set(original_list):
    return list(set(original_list))


def run():
    original_list = [1,1,1,2,3,5,4,5,4,5,6,8,7,7,8,9,5,6,4,4,5,6,3,2,1,2]
    
    #Option 1 by using loop and constructing new list
    #new_list = clean_duplicates_loop(original_list)

    #Option 2 by using sets
    #new_list = clean_duplicates_set(original_list)
    print(new_list)

if __name__ == "__main__":
    run()