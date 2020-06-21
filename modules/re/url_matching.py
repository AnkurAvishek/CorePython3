#problem - https://www.hackerrank.com/challenges/detect-the-domain-name/problem
import re
fp = open('url1.txt', 'r')

regex_pattern = r'^[http|https]?[://]?(\w+.\w+.\w+)$'
regex = re.compile(regex_pattern)

url_set = set()

for line in fp:
    data = fp.readline()
    #print(data)
    #print(type(data))
    t = re.findall(r"[=\'\"](?:https{0,1}\:\/\/(?:ww[w0-9]\.){0,1})([0-9a-zA-Z][0-9a-zA-Z_\-\.]+\.[a-zA-Z]+)",data)
    for item in t:
        if item not in url_set:
            url_set.add(item)
#print(url_set)
print(';'.join(sorted(url_set)))
