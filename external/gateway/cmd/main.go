package main

import (
	"log"
	"net"
	"sync"

	pb "ggjang/grpc/demo/api/greeting"

	"google.golang.org/grpc"
)

func main() {
	//ctx := context.Background()
	grpcAddress := ":50051"
	//httpAddress := ":40041"
	var wg sync.WaitGroup

	wg.Add(1)
	go func() {
		defer wg.Done()
		grpcListen, err := net.Listen("tcp", grpcAddress)
		if err != nil {
			log.Fatal(err)
		}

		greetingSvc := newGreetingServiceServer()

		grpcServer := grpc.NewServer()
		pb.RegisterExampleServiceServer(grpcServer, greetingSvc)

		grpcServer.Serve(grpcListen)
	}()

	// go func() {
	// 	defer wg.Done()
	// 	mux := runtime.NewServeMux()
	// 	if err := pb.RegisterExampleServiceHandlerFromEndpoint(ctx, mux, grpcAddress, []grpc.DialOption{grpc.WithInsecure()}); err != nil {
	// 		log.Fatal(err)
	// 	}
	// 	gwServer := &http.Server{
	// 		Addr: httpAddress,
	// 		Handler: http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
	// 			mux.ServeHTTP(w, r)
	// 		}),
	// 	}
	// 	gwServer.ListenAndServe()
	// }()

	wg.Wait()
}
