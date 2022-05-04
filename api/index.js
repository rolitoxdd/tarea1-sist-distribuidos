// const express = require("express");
// const grpcClient = require("./grpc_client");
// const { createClient } = require("redis");
import express from "express";
import grpcClient from "./grpc_client.js";
import { createClient } from "redis";

const app = express();
const PORT = process.env.PORT || 3000;

const client = createClient({
  socket: { host: process.env.REDIS_HOST, port: 6379 },
});
console.log({ host: process.env.REDIS_HOST, port: 6379 });
client.on("error", (err) => console.error("Redis Client Error", err));
await client.connect();

app.get("/inventory/search", async (req, res) => {
  const { query } = req;
  const q = query.q;

  let redisRes = await client.get(q);
  if (redisRes) {
    console.log("data from redis");
    redisRes = JSON.parse(redisRes);
    res.status(200).json({ products_list: redisRes.items });
  } else {
    console.log("data from grpc server");
    grpcClient.GetItem({ name: q }, async (err, data) => {
      if (err) {
        res.status(500).json({ err });
      } else {
        await client.set(q, JSON.stringify(data));
        res.status(200).json({ products_list: data.items });
      }
    });
  }
});

app.listen(PORT, () => console.log(`listening on port ${PORT}`));
