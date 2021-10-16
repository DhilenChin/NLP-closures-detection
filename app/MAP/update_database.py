from time import timezone
from MAP.internal.graphmatch_pb2 import Point, Trail, RouteMatchRequest
from MAP.internal.graphmatch_pb2_grpc import GraphMatchStub
from MAP.internal.incidents_v2_pb2 import CreateOrReplaceTrafficIncidentRequest, GeoLocation, MatchItem, MatchedGeometry, ClosureInfo, TrafficIncident, CreateTrafficIncidentRequest, Type, ReplaceTrafficIncidentRequest
from MAP.internal.incidents_v2_pb2_grpc import TrafficIncidentsStub
from google.protobuf.timestamp_pb2 import Timestamp
import grpc
import dateparser
import pytz
channel = grpc.insecure_channel("35.195.19.93:32248")
graph_stub = GraphMatchStub(channel)

creds = grpc.ssl_channel_credentials()
incident_channel = grpc.secure_channel('traffic-incidents.graphmasters.net:443', creds)
incident_stub = TrafficIncidentsStub(incident_channel)

class accident_info:
    #Structure to store the accident information, storing the tweet_info object of the accident and the incident id in the closure database
    def __init__(self, output, id):
        self.output = output
        self.id = id

def update_database(timezone_loc,output):
    #Main function to update the closure database
    list_of_response, index_map = get_trail(output)
    list_of_closures = []
    accident = None
    for response in list_of_response:
        coor_ind = index_map[response.index]
        list_of_matchitems = get_match_items_list(response)
        
        match_geo = MatchedGeometry(items = list_of_matchitems)

        timestampnow, timestampbegin, timestampend = organise_time(timezone_loc, output, coor_ind)
        
        if timestampnow == None:
            continue
        
        closureinfo = ClosureInfo(type = ClosureInfo.Road , target = ClosureInfo.All, state = ClosureInfo.Valid)

        is_accident = len(output.time.end) == len(output.time.begin) == 0 and len(output.cause) != 0

        if is_accident:
            incident_id =  get_accident_id(output, coor_ind)
            accident = accident_info(output= output, id = incident_id)
            
        else:
            incident_id = get_closure_id(output, coor_ind, timestampbegin, timestampend)
        
        incident = TrafficIncident(id = incident_id, 
                                    type = Type.CLOSURE,
                                    creation_time = timestampnow, 
                                    start_time = timestampbegin, 
                                    end_time = timestampend, 
                                    matched_geometry = match_geo,
                                    closure_info = closureinfo, 
                                    source = "Twitter",
                                    description = output.content)            
        
        req = CreateTrafficIncidentRequest(incident = incident)
        try:
            traffic_incident = incident_stub.CreateTrafficIncident(req)
            list_of_closures.append(traffic_incident)
        except grpc.RpcError as err:
            print(err)
            pass
    
    return list_of_closures, accident

def replace_accident(output, accident):
    #Main function to update an accident closure as solved
    list_of_response, index_map = get_trail(accident.output)
    list_of_closures = []
    for response in list_of_response:
        list_of_matchitems = get_match_items_list(response)
        
        match_geo = MatchedGeometry(items = list_of_matchitems)

        begin_time = timezone_alloc('UTC', accident.output.datetime)
        end_time = timezone_alloc('UTC', output.datetime)
        timestampnow, timestampbegin, timestampend = set_timestamp(begin_time, end_time)

        closureinfo = ClosureInfo(type = ClosureInfo.Road , target = ClosureInfo.All, state = ClosureInfo.Valid)
        incident = TrafficIncident(id = accident.id, 
                                    type = Type.CLOSURE,
                                    creation_time = timestampnow, 
                                    start_time = timestampbegin, 
                                    end_time = timestampend, 
                                    matched_geometry = match_geo,
                                    closure_info = closureinfo, 
                                    source = 'Twitter',
                                    description = output.content)            
        
        req = ReplaceTrafficIncidentRequest(incident = incident)
        
        traffic_incident = incident_stub.ReplaceTrafficIncident(req)
        list_of_closures.append(traffic_incident)
    
    return list_of_closures

def get_trail(output):
    #Calling graphmatch grpc
    index_map = {}
    list_of_req = []
    req_index = 1   #trailmatch doesn't take 0 as index
    for n in range(len(output.coordinates.begin)):
        begin_coor = output.coordinates.begin[n]
        end_coor = output.coordinates.end[n]
        if begin_coor.lat == 0.0 or end_coor.lat == 0.0:
            continue
        point1 = Point(lat_double = begin_coor.lat, lng_double = begin_coor.lon)
        point2 = Point(lat_double = end_coor.lat,  lng_double = end_coor.lon)
        trail1 = Trail(points = [point1, point2])
        ind = n
        index_map[req_index] = ind   #to keep track of the request made and the response
        req = RouteMatchRequest(trail = trail1, index = req_index)
        req_index += 1
        list_of_req.append(req)

    list_of_response = []
    for response in graph_stub.RouteMatch(iter(list_of_req)):
        list_of_response.append(response)

    return list_of_response, index_map

def get_geometry_list(match):
    list_of_geo = []
    for coor in match.geometry.coords:
        list_of_geo.append(GeoLocation(lat = coor.latitude, lng = coor.longitude))
    return list_of_geo

def get_match_items_list(response):
    list_of_matchitems = []
    for match in response.vertex_matches:
        list_of_geo = get_geometry_list(match)
        list_of_matchitems.append(MatchItem(nugraph_vertex_ids = [match.vertex_id], length = match.length, geometry= list_of_geo, vertex_id= match.vertex_id))
    return list_of_matchitems
       
def organise_time(timezone_loc, output, coor_ind):
    #logic to determine what does the time information in the tweet indicates about the closure
    date = output.datetime.date()
    date_str = date.__str__()
    if len(output.time.begin) == len(output.time.end) == 0 and len(output.cause) != 0:
        begin_time = timezone_alloc('UTC', output.datetime)
        end_time = timezone_alloc('UTC', output.datetime.replace(day = output.datetime.day + 1))
    elif len(output.time.begin) == len(output.time.end) == 0 and len(output.cause) == 0:
        return None, None, None
    elif len(output.time.begin) != 0 and len(output.time.end) == 0:
        return None, None, None
    elif len(output.time.begin) == 0 and len(output.time.end) != 0:
        begin_time = timezone_alloc('UTC', output.datetime)
        end_time = time_format(timezone_loc, date_str, output.time.end[coor_ind])
    else:
        begin_time = time_format(timezone_loc, date_str, output.time.begin[coor_ind])
        end_time = time_format(timezone_loc, date_str, output.time.end[coor_ind])
        
    if begin_time == None or end_time == None:
        return None, None, None

    return set_timestamp(begin_time, end_time)

def set_timestamp(begin_time, end_time):
    if end_time < begin_time:
        end_time = end_time.replace(day= end_time.day + 1)
    timestampnow = Timestamp()
    timestampnow.GetCurrentTime()
    timestampbegin = Timestamp()
    timestampbegin.FromDatetime(begin_time)
    timestampend = Timestamp()
    timestampend.FromDatetime(end_time)

    return timestampnow, timestampbegin, timestampend

def time_format(timezone_loc, date_str, time_str):
    #date_str is the date of the tweet
    #time_str is the time information detected by the NLP model
    timezone_dict = {'TIMEZONE': timezone_loc, 'RETURN_AS_TIMEZONE_AWARE': True}
    HHMM_format = len(time_str) == 4 and time_str.isnumeric()
    HH_MM_format = len(time_str) == 5 and ':' in time_str
    if HHMM_format or HH_MM_format:
        return dateparser.parse(date_string = date_str + ' ' + time_str, settings= timezone_dict, date_formats=["%Y-%m-%d %H%M", "%Y-%m-%d %H:%M"])
    elif '/' in time_str:
        return dateparser.parse(date_string = time_str, settings= timezone_dict, date_formats=["%H%M %d/%m/%Y", "%H:%M %d/%m/%Y", "%d/%m/%Y", "%d/%m"])
    else:
        return None

def get_closure_id(output, coor_ind, timestampbegin, timestampend):
    #generate a closure id with road name, closures location and time information
    road_name_str = output.road_name[coor_ind] 
    closure_begin_str = output.closure.begin[coor_ind]
    closure_end_str = output.closure.end[coor_ind]
    time_begin_str = timestampbegin.ToDatetime().__str__()
    time_end_str = timestampend.ToDatetime().__str__()
    closure_id = "Motorway Closure {}, between {} and {}, during {} to {}".format(road_name_str, closure_begin_str, closure_end_str, time_begin_str, time_end_str)
    return closure_id
    
def get_accident_id(output, coor_ind):
    #generate an accident id with road namem closure location and cause of accident
    road_name_str = output.road_name[coor_ind] 
    closure_begin_str = output.closure.begin[coor_ind]
    closure_end_str = output.closure.end[coor_ind]
    accident_str= output.cause[coor_ind]
    closure_id = "Motorway Closure {}, between {} and {} due to {}".format(road_name_str, closure_begin_str, closure_end_str, accident_str)
    return closure_id

def timezone_alloc(loc, dt):
    #allocating time zone to a datetime object
    timezone = pytz.timezone(loc)
    return timezone.localize(dt)