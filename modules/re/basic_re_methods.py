import re


regex_pattern = "a"
regex = re.compile(regex_pattern)

def check_if_patten_begin_with(data):

    #re.match checks in beginning of the string for the match
    response = re.match(regex, data)
    #print(response)
    #response re.match returns None if no Match match is found.
    if response:
        return True
    else:
        return False

def check_if_patten_is(data): #starts with

    #re.fullmatch entire match
    response = re.fullmatch(regex, data)
    #print(response)
    #response re.match returns None if no Match match is found.
    if response:
        return True
    else:
        return False

def check_if_pattern_in(data):
    #search in multiline only return first match object
    response = re.search(regex, data)
    #print(response)
    if response:
        return True
    else:
        return False


def get_pattern_count(data):
    pass

def get_match_list(data):
    
    response = re.findall(regex, data)

    #print(response)
    if response:
        return response
    else:
        return []

def get_match_object(data):
    
    #response = re.findall(regex, data)
    response = re.finditer(regex, data)
    #print(response)
    if response:
        return response
    else:
        return iter(re.match(None))        

def replace_pattern_string(data, replace_with):
    response = re.sub(regex, replace_with, data)
    #print(response)
    if response:
        return response



if __name__ == "__main__":
    
    data = input("Enter Your Search String: ")

    print("\nDoes data {} begin with regex: {} ? ".format(data, regex_pattern))
    print(check_if_patten_begin_with(data))

    print("\nDoes data {} exactly match regex: {} ? ".format(data, regex.pattern))
    print(check_if_patten_is(data))

    print("\nDoes data {} is in regex: {} ? ".format(data, regex.pattern))
    print(check_if_pattern_in(data))
    
    #getting values
    print("\nList of all match : ")
    print(get_match_list(data))
    
    #playing with object
    print("\nGive me itterable object: ")
    response = get_match_object(data)

    print("\n check itterable object")
    print("\n first match object ")
    
    try:
        print(next(response))
        print("\n 2nd match object's value")
        print(next(response).__getitem__(0))
    except StopIteration:
        print("Less Match found")

    print("\n 3rd to n object and its values values, printed twice: ")
    for match in response:
        print(match)
        print(match.__getitem__(0))
        print(match[0])

    #replace regex value
    print("\n Sustititution test")
    print("\n substitutin {} in {} with {} ".format(regex_pattern, data, "_XoX"))
    print(replace_pattern_string(data, replace_with="_XoX_"))
    response = replace_pattern_string(data, "_XoX_")
   
    #group 
    print("\n Grouping Test")
    test = re.search("(a) (.)", data) #match, #findall- dose not have group support.
    if test:
        try:
            print(test.group())
            print(test.group(1))
            print(test.group(2))
        except IndexError:
            print("Less matching group")

    #split
    print("Split")
    response = re.split(regex, data)
    print(response)


    re.purge()