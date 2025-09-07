import requests
query=input("enter your topic for news!:")
api="6c43658c2d90411fb3ca6e34a2d0afa0"
url=f"https://newsapi.org/v2/everything?q={query}=2025-08-07&sortBy=publishedAt&apiKey={api}"

r=requests.get(url)
data=r.json()
articles=data["articles"]
for index, article in enumerate(articles):
    print(index+1 ,article["author"],article["description"])
    print("\n***************************")

 