#! /bin/bash

cd ..
git clone https://github.com/Graphmasters/apis.git

python -m grpc_tools.protoc -I ./apis/nugraph/graphmatch/v1 --python_out=./closures-detection/app/MAP/internal --grpc_python_out=./app/closures-detection/MAP/internal ./apis/nugraph/graphmatch/v1/graphmatch.proto
python -m grpc_tools.protoc -I ./apis/traffic/incidents/v2 --python_out=./closures-detection/app/MAP/internal --grpc_python_out=./app/closures-detection/MAP/internal ./apis/traffic/incidents/v2/incidents_v2.proto
