import urllib.request, json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("saveloc", help="The location to save images to (eg. 'C:/users/images')")
parser.add_argument("--mkt", help="The market the images are meant for (eg. en-CA)")
args = parser.parse_args()

#Change the market to get these images from if it was specified
if args.mkt:
    url_str = """https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={}""".format(args.mkt)
else:
    url_str = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-CA"


#Download the images
with urllib.request.urlopen(url_str) as url:
    data = json.loads(url.read().decode())
    picture_url = data['images'][0]['url'];

    #The picture url looks like '/az/hprichbg/rb/Mellieha_EN-CA9931288836_1920x1080.jpg'
    #This line gets the part between ...rb/ and  _EN-CA...
    picture_name = picture_url.split("/")[4].split("_")[0]

    #Download and save the image
    urllib.request.urlretrieve('https://www.bing.com' + picture_url,
        "{}/{}.jpg".format(args.saveloc, picture_name))
