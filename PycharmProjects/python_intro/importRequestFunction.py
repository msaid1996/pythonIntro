import requests                                                 # can request anything from online

bbc_website = requests.get("https://www.bbc.co.uk/")
dailyMail_website = requests.get("https://www.dailymail.co.uk/home/index.html")

#view status code
print(bbc_website.status_code)                                  # 200 = perfect, 404 = ERROR

#view content
print(bbc_website.content)                                      # computer content of http

#view the headers
print(bbc_website.headers)

#view the cookies
print(bbc_website.cookies)

#view the cookies
print(bbc_website.history)
print(dailyMail_website.history)