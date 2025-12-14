import grpc
from concurrent import futures
import time

import model_pb2
import model_pb2_grpc

class ModelServiceServicer(model_pb2_grpc.ModelServiceServicer):
    def health(self, request, context):
        return model_pb2.HealthResponse(status='OK', version='1.0')

    def predict(self, request, context):
        # Здесь можно реализовать логику предсказания
        prediction = "example_prediction"
        confidence = 0.9
        return model_pb2.PredictResponse(prediction=prediction, confidence=confidence)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_ModelServiceServicer_to_server(ModelServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server Started at port 50051")
    try:
        while True:
            time.sleep(86400)  # 1 день
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()