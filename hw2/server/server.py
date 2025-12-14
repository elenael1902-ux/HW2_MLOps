import grpc
from concurrent import futures
import time

import model_pb2
import model_pb2_grpc

class ModelServiceServicer(model_pb2_grpc.ModelServiceServicer):
    def health(self, request, context):
        return model_pb2.HealthResponse(status='OK', version='1.0')

    def predict(self, request, context):
        input_data = request.input  
        # Вызов модели, пример для sklearn/pickle
        prediction = model.predict([input_data])
        confidence = max(model.predict_proba([input_data])[0])  # вероятность

        return model_pb2.PredictResponse(
        prediction=str(prediction[0]),
        confidence=confidence
    )
        
        

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
import os
import pickle  

# Получаем путь к модели из переменной окружения
model_path = os.getenv('MODEL_PATH', '/default/path/to/model.pkl')

# Загружаем модель
with open(model_path, 'rb') as f:
    model = pickle.load(f)
