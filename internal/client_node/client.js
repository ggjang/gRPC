// Import necessary modules
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');

// Define the path to the .proto file
const PROTO_PATH = path.resolve(__dirname, '../../api/greeting/helloworld.proto');

// Load the .proto file
var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});
const exampleProto = grpc.loadPackageDefinition(packageDefinition).example.ExampleService;

// Create a client instance
const client = new exampleProto('localhost:50051', grpc.credentials.createInsecure());

// Function to call the SayHello RPC
function greet(name) {
  return new Promise((resolve, reject) => {
    client.sayHello({ name }, (error, response) => {
      if (error) {
        return reject(error);
      }
      resolve(response.message);
    });
  });
}

// Main function
async function main() {
  try {
    const name = 'World';
    const message = await greet(name);
    console.log('Greeting:', message);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Execute the main function
main();
