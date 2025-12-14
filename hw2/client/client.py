import grpc
import model_pb2
import model_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = model_pb2_grpc.ModelServiceStub(channel)
        
        # Проверка статуса
        response = stub.health(model_pb2.HealthRequest())
        print("Health status:", response.status)
        
        # Вызов предсказания
        predict_request = model_pb2.PredictRequest(input="some input data")
        predict_response = stub.predict(predict_request)
        print("Prediction:", predict_response.prediction)
        print("Confidence:", predict_response.confidence)

if __name__ == '__main__':
    run()