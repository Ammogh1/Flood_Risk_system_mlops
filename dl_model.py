import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image

MODEL_PATH = "models/dl_cnn_model.pth"

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Input shape: (3, 64, 64)
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 2) # 2 classes: Flood (1), No Flood (0)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 32 * 16 * 16)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def train_dl_model(data_dir="data/images", epochs=5):
    """Trains a basic CNN on dummy image data."""
    if not os.path.exists(data_dir) or len(os.listdir(data_dir)) == 0:
        from utils import generate_dummy_images
        generate_dummy_images()
        
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
    ])
    
    dataset = datasets.ImageFolder(root=data_dir, transform=transform)
    # Expected classes from ImageFolder: 'flood', 'no_flood'
    # We will map them appropriately during inference if needed.
    
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
    
    model = SimpleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch {epoch+1}, Loss: {running_loss/len(dataloader)}")
        
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), MODEL_PATH)
    print(f"DL Model saved to {MODEL_PATH}")
    return model

def predict_dl(image_path):
    """Predicts flood risk using the trained CNN.
    Returns 1 for Flood, 0 for No Flood.
    """
    if not os.path.exists(MODEL_PATH):
        train_dl_model()
        
    model = SimpleCNN()
    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
    ])
    
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
        prediction = torch.argmax(output, dim=1).item()
        
    # We need to map the predicted class index back to semantic meaning
    # Assume class 0 is 'flood' and class 1 is 'no_flood' based on alphabetical order
    # Let's return 1 for flood and 0 for no flood
    if prediction == 0: # 'flood' directory
        return 1
    return 0

if __name__ == "__main__":
    train_dl_model()
