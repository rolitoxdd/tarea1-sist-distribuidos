from concurrent import futures
# import logging

import grpc
import item_pb2
import item_pb2_grpc
from data_base import Database


class Inventory(item_pb2_grpc.ItemService):
    def GetItem(self, request, context):
        print("request", request)
        # print("context", dir(context))
        name = request.name
        if name:
            list_of_elements = db.list_by_name(name)
        else:
            list_of_elements = db.list_of_elements()

        list_of_elements = [{
            "id": elem[0],
            "name":elem[1].strip(),
            "price": elem[2],
            "category": elem[3].strip(),
            "count": elem[4]
        }
            for elem in list_of_elements
        ]
        return item_pb2.Response(items=list_of_elements)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    item_pb2_grpc.add_ItemServiceServicer_to_server(Inventory(), server)
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
