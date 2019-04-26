
import folium
import os
from GPSPhoto import gpsphoto


def get_img_info(img_path):
    return gpsphoto.getGPSData(img_path)

def download_training_data():
    ## googleimagesdownload --keywords "stagnant water roads india" --limit 40 --format jpg
    pass

def rename_imgs(dir_path, key):
    i = 0
    for filename in os.listdir(dir_path):
        dst = key + str(i) + ".jpg"
        src = os.path.join(dir_path, filename)
        dst = os.path.join(dir_path, dst)
        os.rename(src, dst)
        i += 1

def catogery_mapper(category):

    catogery_dict = {
        "pothole": "green",
        "trash": "yellow",
        "stagnant_water": "red"
    }

    return catogery_dict[category]

def render_map(lat_long_list, zoom_level=13):

    counter = 0
    try:
        if len(lat_long_list) > 0:
            my_map = folium.Map([lat_long_list[0][0], lat_long_list[0][1]], zoom_start=zoom_level)

            for lat_long in lat_long_list:
                counter = counter+1
                my_map.add_child(folium.Marker([lat_long[0], lat_long[1]], popup=lat_long[2]+"_"+str(counter),
                            icon=folium.Icon(color=catogery_mapper(lat_long[2]), prefix='fa', icon='circle')))

            legend_html = """
                 <div style=”position: fixed; 
                 bottom: 50px; left: 50px; width: 100px; height: 90px; 
                 border:2px solid grey; z-index:9999; font-size:14px;
                 “>&nbsp; Cool Legend <br>
                 &nbsp; East &nbsp; <i class=”fa fa-map-marker fa-2x”
                              style=”color:green”></i><br>
                 &nbsp; West &nbsp; <i class=”fa fa-map-marker fa-2x”
                              style=”color:red”></i>
                  </div>
                 """

            return my_map.get_root().html.add_child(folium.Element(legend_html))

    except:
        raise Exception


print(get_img_info("/Users/sharathsamala/Downloads/UNADJUSTEDNONRAW_thumb_287b.jpg"))


