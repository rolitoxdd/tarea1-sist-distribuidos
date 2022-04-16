from concurrent import futures
# import logging

import grpc
import example_pb2
import example_pb2_grpc
from data_base import Database


class Inventory(example_pb2_grpc.ItemService):
    def GetItem(self, request, context):
        list_of_elements = db.list_of_elements()
        print(list_of_elements)
        list_of_elements = [{
            "id": elem[0],
            "name":elem[1],
            "value": elem[2]
        }
            for elem in list_of_elements
        ]
        return example_pb2.Response(items=list_of_elements)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ItemServiceServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    db = Database()
    # conn = db.connectionDB()
    # print(conn)

    # logging.basicConfig()
    print("listening...")
    serve()
