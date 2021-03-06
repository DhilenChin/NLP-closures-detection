# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import MAP.internal.graphmatch_pb2 as graphmatch__pb2


class GraphMatchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Version = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/Version',
                request_serializer=graphmatch__pb2.VersionRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.VersionResponse.FromString,
                )
        self.SingleTrailMatch = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/SingleTrailMatch',
                request_serializer=graphmatch__pb2.SingleTrailMatchRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.SingleTrailMatchResponse.FromString,
                )
        self.FlowMatch = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/FlowMatch',
                request_serializer=graphmatch__pb2.FlowMatchRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.FlowMatchResponse.FromString,
                )
        self.OpenlrMatch = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/OpenlrMatch',
                request_serializer=graphmatch__pb2.OpenlrMatchRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.OpenlrMatchResponse.FromString,
                )
        self.VertexBulkMatch = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/VertexBulkMatch',
                request_serializer=graphmatch__pb2.VertexBulkMatchRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.VertexBulkMatchResponse.FromString,
                )
        self.EdgeBulkMatch = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/EdgeBulkMatch',
                request_serializer=graphmatch__pb2.EdgeBulkMatchRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.EdgeBulkMatchResponse.FromString,
                )
        self.RouteMatch = channel.stream_stream(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/RouteMatch',
                request_serializer=graphmatch__pb2.RouteMatchRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.RouteMatchResponse.FromString,
                )
        self.OffRouteCheck = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatch/OffRouteCheck',
                request_serializer=graphmatch__pb2.OffRouteCheckRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.OffRouteCheckResponse.FromString,
                )


class GraphMatchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Version(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SingleTrailMatch(self, request, context):
        """SingleTrailMatch partially processes a trail - the match may not be complete if the endpoints
        are within range of multiple vertices. It is meant to be used repeatedly to piece together
        a complete trail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FlowMatch(self, request, context):
        """FlowMatch is similar to SingleTrailMatch, but is meant to match completely in one call.
        The end points are snapped to junctions so that the whole trail is matched if at all possible
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenlrMatch(self, request, context):
        """OpenlrMatch, like FlowMatch, matches a complete series of points. The points are taken
        from the openlr bytes input.
        The end points are snapped to junctions so that the whole trail is matched if at all possible
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VertexBulkMatch(self, request, context):
        """Will match the given coordinates to the closes vertices and connect them
        This is used to match EdgeIds from our legacy system to nugraph. This must snap to the closest vertex with the correct heading and connect betweend vertices.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EdgeBulkMatch(self, request, context):
        """Will match the given coordinates to the closes edge.
        This is used to match in/out-edge ids of the legacy system to nugraph. This must return the edge id of the turn that is described by the coordinates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteMatch(self, request_iterator, context):
        """Will match the given coordinates to the closest vertices and connect them.
        Geometries will be returned.
        This is used to match routes to nugraph vertices.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OffRouteCheck(self, request, context):
        """Given the trail of probes from a user, and a list of vertex ids representing a route,
        comments on whether the user has gone off route
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GraphMatchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Version': grpc.unary_unary_rpc_method_handler(
                    servicer.Version,
                    request_deserializer=graphmatch__pb2.VersionRequest.FromString,
                    response_serializer=graphmatch__pb2.VersionResponse.SerializeToString,
            ),
            'SingleTrailMatch': grpc.unary_unary_rpc_method_handler(
                    servicer.SingleTrailMatch,
                    request_deserializer=graphmatch__pb2.SingleTrailMatchRequest.FromString,
                    response_serializer=graphmatch__pb2.SingleTrailMatchResponse.SerializeToString,
            ),
            'FlowMatch': grpc.unary_unary_rpc_method_handler(
                    servicer.FlowMatch,
                    request_deserializer=graphmatch__pb2.FlowMatchRequest.FromString,
                    response_serializer=graphmatch__pb2.FlowMatchResponse.SerializeToString,
            ),
            'OpenlrMatch': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenlrMatch,
                    request_deserializer=graphmatch__pb2.OpenlrMatchRequest.FromString,
                    response_serializer=graphmatch__pb2.OpenlrMatchResponse.SerializeToString,
            ),
            'VertexBulkMatch': grpc.unary_unary_rpc_method_handler(
                    servicer.VertexBulkMatch,
                    request_deserializer=graphmatch__pb2.VertexBulkMatchRequest.FromString,
                    response_serializer=graphmatch__pb2.VertexBulkMatchResponse.SerializeToString,
            ),
            'EdgeBulkMatch': grpc.unary_unary_rpc_method_handler(
                    servicer.EdgeBulkMatch,
                    request_deserializer=graphmatch__pb2.EdgeBulkMatchRequest.FromString,
                    response_serializer=graphmatch__pb2.EdgeBulkMatchResponse.SerializeToString,
            ),
            'RouteMatch': grpc.stream_stream_rpc_method_handler(
                    servicer.RouteMatch,
                    request_deserializer=graphmatch__pb2.RouteMatchRequest.FromString,
                    response_serializer=graphmatch__pb2.RouteMatchResponse.SerializeToString,
            ),
            'OffRouteCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.OffRouteCheck,
                    request_deserializer=graphmatch__pb2.OffRouteCheckRequest.FromString,
                    response_serializer=graphmatch__pb2.OffRouteCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'graphmasters.nugraph.graphmatch.v1.GraphMatch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GraphMatch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Version(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/Version',
            graphmatch__pb2.VersionRequest.SerializeToString,
            graphmatch__pb2.VersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SingleTrailMatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/SingleTrailMatch',
            graphmatch__pb2.SingleTrailMatchRequest.SerializeToString,
            graphmatch__pb2.SingleTrailMatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FlowMatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/FlowMatch',
            graphmatch__pb2.FlowMatchRequest.SerializeToString,
            graphmatch__pb2.FlowMatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenlrMatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/OpenlrMatch',
            graphmatch__pb2.OpenlrMatchRequest.SerializeToString,
            graphmatch__pb2.OpenlrMatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VertexBulkMatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/VertexBulkMatch',
            graphmatch__pb2.VertexBulkMatchRequest.SerializeToString,
            graphmatch__pb2.VertexBulkMatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EdgeBulkMatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/EdgeBulkMatch',
            graphmatch__pb2.EdgeBulkMatchRequest.SerializeToString,
            graphmatch__pb2.EdgeBulkMatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteMatch(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/RouteMatch',
            graphmatch__pb2.RouteMatchRequest.SerializeToString,
            graphmatch__pb2.RouteMatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OffRouteCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatch/OffRouteCheck',
            graphmatch__pb2.OffRouteCheckRequest.SerializeToString,
            graphmatch__pb2.OffRouteCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class GraphMatchSsspStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransitions = channel.unary_unary(
                '/graphmasters.nugraph.graphmatch.v1.GraphMatchSssp/GetTransitions',
                request_serializer=graphmatch__pb2.GetTransitionsRequest.SerializeToString,
                response_deserializer=graphmatch__pb2.GetTransitionsResponse.FromString,
                )


class GraphMatchSsspServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTransitions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GraphMatchSsspServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTransitions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransitions,
                    request_deserializer=graphmatch__pb2.GetTransitionsRequest.FromString,
                    response_serializer=graphmatch__pb2.GetTransitionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'graphmasters.nugraph.graphmatch.v1.GraphMatchSssp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GraphMatchSssp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTransitions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/graphmasters.nugraph.graphmatch.v1.GraphMatchSssp/GetTransitions',
            graphmatch__pb2.GetTransitionsRequest.SerializeToString,
            graphmatch__pb2.GetTransitionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
