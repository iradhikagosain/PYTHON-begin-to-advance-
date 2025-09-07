import requests

r = requests.get('https://api.github.com/users/iradhikagosain')
print(r.name)

with open("radhika.txt","w") as f:
    f.write(r.text)
