import torch.nn as nn
import torch

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = SimpleNN()

def predict(input_data):
    tensor_data = torch.tensor([input_data], dtype=torch.float32)
    with torch.no_grad():
        output = model(tensor_data).tolist()
    return output

# python -m uvicorn main:app --reload