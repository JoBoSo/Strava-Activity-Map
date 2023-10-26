import pandas as pd
import xml.etree.ElementTree as ET
import os

open('gpx_to_json_error_log.txt', 'w').close()

data = {
    'file': [],
    'activity': [],
    'time': [],
    'lat': [],
    'lon': [],
    'elevation': []
}

path = 'gpx_files'
namespace = {"gpx": "http://www.topografix.com/GPX/1/1"}
file_counter = 1

for file in os.listdir(path):
    filename = os.path.join(path, file)
    try:
        tree = ET.parse(filename)
        for track in tree.findall('gpx:trk', namespace):
            try:
                act_type = track.find('gpx:type', namespace).text
            except AttributeError:
                act_type = 'N/A'
            for track_segment in track.findall('gpx:trkseg', namespace):
                for track_point in track_segment.findall('gpx:trkpt', namespace):
                    data['file'] += [file]
                    data['activity'] += [act_type]
                    try:
                        data['time'] += [track_point.find('gpx:time', namespace).text]
                    except AttributeError:
                        data['time'] += ['N/A']
                    data['lat'] += [track_point.attrib['lat']]
                    data['lon'] += [track_point.attrib['lon']]
                    try:
                        data['elevation'] += [track_point.find('gpx:ele', namespace).text]
                    except AttributeError:
                        data['elevation'] += ['N/A']
        
        print(file_counter, file)
        file_counter += 1
        # if file_counter > 2:
        #     break

    except Exception as e:
        error_message = repr(e) + ' occured for file: ' + file
        print(error_message)
        with open("gpx_to_json_error_log.txt", "a") as text_file:
            text_file.write(error_message + '\n')
        continue

for key in data:
    data[key] = data[key][::100]

df = pd.DataFrame(data)
df.to_json('data.json', orient="columns")