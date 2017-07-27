import urllib.request, json

url_str = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-CA'

with urllib.request.urlopen(url_str) as url:
    data = json.loads(url.read().decode())
    picture_url = data['images'][0]['url'];

    picture_name = picture_url.split("/")[4].split("_")[0]

    urllib.request.urlretrieve('https://www.bing.com' + picture_url,
        "C:\\Users\\murphyc\\Pictures\\Saved Pictures\\" + picture_name + ".jpg")

print("Done!");
