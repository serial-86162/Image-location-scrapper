import os
import exif
import  folium
from PIL import Image 
def get_gps_info(image_path):
    with open(image_path,'rb') as image_file:
        my_image = exif.Image(image_file)
        lat_ref = my_image.gps_latitude_ref
        lon_ref = my_image.gps_longitude_ref
        lat = my_image.gps_latitude
        lon =my_image.gps_longitude

        if lat_ref and lon_ref and lat and lon:
            lat_value = lat[0] + lat[1]/60 + lat[2]/3600
            lon_value = lon[0] + lon[1]/60 + lon[2]/3600
            if lat_ref =='S':
                lat_value = -lat_value
            if lon_ref =='W':
                lon_value = -lon_value
            return lat_value,lon_value
        else:
            return None, None
def main():
    folder_path = r'c:\Users\OKI86162\Documents\Python scripts\Underthemassillusion\trial run'
    map_center = [0,0]

    m =folium.Map(location=map_center,zoom_start=10)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg','.jpeg','.png')):
            image_path = os.path.join(folder_path,filename)
            lat,lon = get_gps_info(image_path)
            if lat is not None and lon is not None:
                folium.Marker([lat,lon], popup=filename).add_to(m)
            else:
                print(filename,"skipped")
    
    m.save('image_map.html')
    print("Map saved as 'image_map'")
if __name__ == "__main__":
    main()  



    
    
    