package main

import (
	"context"
	pb "ggjang/grpc/demo/api/greeting"
)

type GreetingServiceServer struct {
	pb.GreetingServiceServer
}

func newGreetingServiceServer() *GreetingServiceServer {
	return &GreetingServiceServer{}
}

func (g *GreetingServiceServer) HelloWorld(ctx context.Context, req *pb.Request) (*pb.Response, error) {
	return &pb.Response{Messgae: "Hi"}, nil
}
