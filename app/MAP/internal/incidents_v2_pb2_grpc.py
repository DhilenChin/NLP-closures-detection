# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import MAP.internal.incidents_v2_pb2 as incidents__v2__pb2


class TrafficIncidentsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTrafficIncident = channel.unary_unary(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/GetTrafficIncident',
                request_serializer=incidents__v2__pb2.TrafficIncidentRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )
        self.GetTrafficIncidents = channel.unary_stream(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/GetTrafficIncidents',
                request_serializer=incidents__v2__pb2.TrafficIncidentsRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )
        self.GetTrafficIncidentsAggregation = channel.unary_stream(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/GetTrafficIncidentsAggregation',
                request_serializer=incidents__v2__pb2.TrafficIncidentsRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )
        self.CreateTrafficIncident = channel.unary_unary(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/CreateTrafficIncident',
                request_serializer=incidents__v2__pb2.CreateTrafficIncidentRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )
        self.ReplaceTrafficIncident = channel.unary_unary(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/ReplaceTrafficIncident',
                request_serializer=incidents__v2__pb2.ReplaceTrafficIncidentRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )
        self.CreateOrReplaceTrafficIncident = channel.unary_unary(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/CreateOrReplaceTrafficIncident',
                request_serializer=incidents__v2__pb2.CreateOrReplaceTrafficIncidentRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )
        self.DeleteTrafficIncident = channel.unary_unary(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/DeleteTrafficIncident',
                request_serializer=incidents__v2__pb2.DeleteTrafficIncidentRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.Response.FromString,
                )
        self.AddRating = channel.unary_unary(
                '/graphmasters.traffic.incidents.v2.TrafficIncidents/AddRating',
                request_serializer=incidents__v2__pb2.AddRatingRequest.SerializeToString,
                response_deserializer=incidents__v2__pb2.TrafficIncident.FromString,
                )


class TrafficIncidentsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTrafficIncident(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrafficIncidents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrafficIncidentsAggregation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTrafficIncident(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceTrafficIncident(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrReplaceTrafficIncident(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTrafficIncident(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrafficIncidentsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTrafficIncident': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrafficIncident,
                    request_deserializer=incidents__v2__pb2.TrafficIncidentRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
            'GetTrafficIncidents': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTrafficIncidents,
                    request_deserializer=incidents__v2__pb2.TrafficIncidentsRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
            'GetTrafficIncidentsAggregation': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTrafficIncidentsAggregation,
                    request_deserializer=incidents__v2__pb2.TrafficIncidentsRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
            'CreateTrafficIncident': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTrafficIncident,
                    request_deserializer=incidents__v2__pb2.CreateTrafficIncidentRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
            'ReplaceTrafficIncident': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceTrafficIncident,
                    request_deserializer=incidents__v2__pb2.ReplaceTrafficIncidentRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
            'CreateOrReplaceTrafficIncident': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrReplaceTrafficIncident,
                    request_deserializer=incidents__v2__pb2.CreateOrReplaceTrafficIncidentRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
            'DeleteTrafficIncident': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTrafficIncident,
                    request_deserializer=incidents__v2__pb2.DeleteTrafficIncidentRequest.FromString,
                    response_serializer=incidents__v2__pb2.Response.SerializeToString,
            ),
            'AddRating': grpc.unary_unary_rpc_method_handler(
                    servicer.AddRating,
                    request_deserializer=incidents__v2__pb2.AddRatingRequest.FromString,
                    response_serializer=incidents__v2__pb2.TrafficIncident.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'graphmasters.traffic.incidents.v2.TrafficIncidents', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrafficIncidents(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTrafficIncident(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/GetTrafficIncident',
            incidents__v2__pb2.TrafficIncidentRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrafficIncidents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/GetTrafficIncidents',
            incidents__v2__pb2.TrafficIncidentsRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrafficIncidentsAggregation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/GetTrafficIncidentsAggregation',
            incidents__v2__pb2.TrafficIncidentsRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTrafficIncident(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/CreateTrafficIncident',
            incidents__v2__pb2.CreateTrafficIncidentRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplaceTrafficIncident(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/ReplaceTrafficIncident',
            incidents__v2__pb2.ReplaceTrafficIncidentRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOrReplaceTrafficIncident(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/CreateOrReplaceTrafficIncident',
            incidents__v2__pb2.CreateOrReplaceTrafficIncidentRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTrafficIncident(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/DeleteTrafficIncident',
            incidents__v2__pb2.DeleteTrafficIncidentRequest.SerializeToString,
            incidents__v2__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.traffic.incidents.v2.TrafficIncidents/AddRating',
            incidents__v2__pb2.AddRatingRequest.SerializeToString,
            incidents__v2__pb2.TrafficIncident.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
