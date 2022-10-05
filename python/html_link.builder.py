#hyperlink HTML builder

linkurl = input("Enter your URL:\n")
linkname = input ("Enter the link name:\n")

print("Here's your HTML string:\n")
print(f'<a href="{linkurl}">{linkname}</a>')
