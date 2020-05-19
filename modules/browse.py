import re
import webbrowser

test = 'open google webpage'
reg_ex = re.search('open google (.*)', test)
print(reg_ex)