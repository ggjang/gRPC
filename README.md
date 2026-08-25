# gRPC Demo

Go로 구현한 gRPC 서비스 데모. grpc-gateway를 통해 HTTP/JSON도 함께 지원하며, Go · Node.j포함한다.

```
Client (Go / Node.js / Python)
        │
        ├── gRPC (port 50051)
        │
        └── HTTP/JSON (port 8080) ── grpc-gateway ──▶ gRPC Server
```

## 서비스 정의

`api/greeting/helloworld.proto`

```protobuf
service ExampleService {
  rpc SayHello (HelloRequest) returns (HelloResponse);
}

message HelloRequest { string name = 1; }
message HelloResponse { string message = 1; }
```

```
.
├── api/
│   ├── buf.yaml            # Buf 설정
│   ├── buf.gen.yaml        # 코드 생성 설정
│   └── greeting/
│       ├── helloworld.proto
│       ├── helloworld.pb.go
│       ├── helloworld_grpc.pb.go
│       └── helloworld.pb.gw.go
├── external/
│   └── gateway/cmd/        # grpc-gateway 서버
├── internal/
│   ├── client_go/cmd/      # Go 클라이언트
│   ├── client_node/        # Node.js 클라이언트
│   └── client_python/      # Python 클라이언트
└── vendor/
```

## 요구사항

- Go 1.22.5+
- [Buf CLI](https://buf.build/docs/installation) (proto 재생성 시)
- Node.js (Node 클라이언트 실행 시)
- Python 3.x (Python 클라이언트 실행 시)

## 실행 방법

### gRPC 서버

```bash
go run external/gateway/cmd/main.go
```

### Go 클라이언트

```bash
go run internal/client_go/cmd/main.go
```

### Python 클라이언트

```bash
cd internal/client_python
python main.py
```

### Node.js 클라이언트

```bash
cd internal/client_node
node index.js
```

### HTTP 호출 (grpc-gateway)

```bash
curl -X POST http://localhost:8080/v1/hello \
  -H "Content-Type: application/json" \
  -d '{"name": "world"}'
```

## Proto 재생성

```bash
cd api
buf generate
```

## 기술 스택

| 항목 | 버전 |
|------|------|
| Go | 1.22.5 |
| grpc | v1.65.0 |
| grpc-gateway | v2.22.0 |
| protobuf | v1.34.2 |
| Buf | - |

---
