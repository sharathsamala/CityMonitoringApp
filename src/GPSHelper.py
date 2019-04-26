from GPSPhoto import gpsphoto

data = gpsphoto.getGPSData('/Users/sharathsamala/Downloads/UNADJUSTEDNONRAW_thumb_287b.jpg')
print(data)
for tag in data.keys():
    print("%s: %s" % (tag, data[tag]))