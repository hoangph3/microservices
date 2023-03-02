FROM python:3.7-slim-buster

WORKDIR /service/recommendations

COPY . .
# COPY ca.pem /service/recommendations/

RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I protobufs --python_out=. \
           --grpc_python_out=. protobufs/recommendations.proto
# RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations \
#                 -keyout server.key -out server.csr
# RUN --mount=type=secret,id=ca.key \
#     openssl x509 -req -in server.csr -CA ca.pem -CAkey /run/secrets/ca.key \
#                  -set_serial 1 -out server.pem

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]
