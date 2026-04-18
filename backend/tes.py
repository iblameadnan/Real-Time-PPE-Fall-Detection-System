import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)
#cd backend
#uvicorn main:app --reload --host 127.0.0.1 --port 8000
#Frontend Setup
#In a second terminal:

#cd frontend
#npm install
#npm run dev