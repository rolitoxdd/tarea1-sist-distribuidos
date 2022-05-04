import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";

const PROTO_PATH = process.env.PROTO_PATH || "item.proto";
const HOST = process.env.GRPC_SERVER_HOST || "localhost";

const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

const packageDefinition = protoLoader.loadSync(PROTO_PATH, options);
const ItemService = grpc.loadPackageDefinition(packageDefinition).ItemService;
const client = new ItemService(
  `${HOST}:50051`,
  grpc.credentials.createInsecure()
);

export default client;
