package main

import (
	"context"
	pb "ggjang/grpc/demo/api/greeting"
)

type GreetingServiceServer struct {
	pb.UnsafeExampleServiceServer
}

func newGreetingServiceServer() *GreetingServiceServer {
	return &GreetingServiceServer{}
}

func (g *GreetingServiceServer) SayHello(ctx context.Context, req *pb.HelloRequest) (*pb.HelloResponse, error) {
	return &pb.HelloResponse{
		Message: "Hi",
	}, nil
}
