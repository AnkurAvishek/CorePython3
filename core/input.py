# input string
text = input()

# feedback 
text = input("Enter text: ")
#input int
text = int(input())
#input char
text = input()[0]
#input float
text = float(input())

#raw input #python2
raw_input() #' 0 5      '
raw_input().strip() # '0 5'
raw_input().strip().split() #['0', '5']

#multiline
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
text = '\n'.join(contents)