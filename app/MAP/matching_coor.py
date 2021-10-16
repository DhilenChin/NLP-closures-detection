import numpy as np
import requests
from haversine import haversine_vector, Unit

class coordinates:
    #Structure for coordinates 
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class matching_coor:
    #Class to obtain coordinates from junction-coordinates:8080
    def __init__(self, output = None, address=''):
        self.output = output
        self.address = address #address of juncation-coordinates:8080

    def matching_coor(self):
        #Main function in this class
        #Save the result in self.output, which is a tweet_info object
        equal_length = len(self.output.road_name) == len(self.output.closure.begin) == len(self.output.closure.end) #To ensure sufficient information is available to get the coordinates
        if not equal_length:
            self.output.coordinates.begin.append(coordinates(lat= 0.0, lon = 0.0))
            self.output.coordinates.end.append(coordinates(lat= 0.0, lon = 0.0))
            return
        for n in range (len(self.output.road_name)):
            road_name = self.output.road_name[n]
            if road_name[0] == 'A' and road_name[-1] == 'M':
                road_name = road_name.replace('M', '(M)')
            begin_coor_list = self.making_right_query(road_name, self.output.closure.begin[n], self.output.extra_closure.begin)
            end_coor_list = self.making_right_query(road_name, self.output.closure.end[n], self.output.extra_closure.end) 

            begin_coor_list = self.making_right_query(road_name, self.output.closure.begin[n], self.output.extra_closure.begin)
            end_coor_list = self.making_right_query(road_name, self.output.closure.end[n], self.output.extra_closure.end) 

            begin_coor, end_coor = self.shortest_pair(begin_coor_list, end_coor_list)
            self.output.coordinates.begin.append(coordinates(lat =begin_coor[0], lon = begin_coor[1]))
            self.output.coordinates.end.append(coordinates(lat =end_coor[0], lon = end_coor[1]))


    def making_right_query(self, road_name, closure, extra_closure_list):
        #querying based on appropriate information, whether from the BEGIN_CLOSURE or EXTRA_BEGIN_CLOSURE information
        junc = closure.replace('J', '')
        try:
            coor_list = self.query_http(road_name, junc)
        except:
            try:
                coor_list = [{'Lat':0.0, 'Lon': 0.0}]
                for extra in extra_closure_list:
                    if extra[0] == 'A':
                        extra = extra.replace('M', '(M)')
                    coor_list = self.query_http(extra, junc)
                    break
            except:
                coor_list = [{'Lat':0.0, 'Lon': 0.0}]
        return coor_list

    def query_http(self, road, junc):
        #making http req to get coordinates for junctions
        r = requests.get("http://{}/?road={}&junc={}".format(self.address,road,junc))
        return r.json()['Coordinates']


    def shortest_pair(self, begin_coor_list, end_coor_list):
        #getting a pair of begin and end coordinates with the shortest haversine distance
        begin_list = [(n['Lat'], n['Lon']) for n in begin_coor_list]
        end_list = [(n['Lat'], n['Lon']) for n in end_coor_list]
        distance = haversine_vector(begin_list, end_list, Unit.KILOMETERS, comb= True)
        index = np.where(distance == np.amin(distance))
        begin_coor = begin_list[index[1][0]]
        end_coor = end_list[index[0][0]]
        return begin_coor, end_coor
