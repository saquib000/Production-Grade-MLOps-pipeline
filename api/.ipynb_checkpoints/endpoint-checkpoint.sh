#http://136.111.190.138:8000/

curl -X POST http://136.111.190.138:8000/predict -H "Content-Type: application/json" -d '{
  "age": 63,
  "gender": 0,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}'