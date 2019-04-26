
import urllib.request
import os


pothole_img_urls = open("../data/pathhole_image_urls.txt", 'r').read()

counter=0
for img_url in pothole_img_urls.split("\n"):
    try:
        f, f_ext = os.path.splitext(img_url)
        if counter > 138:
            urllib.request.urlretrieve(img_url, "training_img_"+str(counter)+f_ext.lower().strip())
        counter=counter+1
        print("downloading image : " + str(counter))
    except Exception:
        pass

print("done")