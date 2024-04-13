
from torchvision import models, transforms
import torch
from PIL import Image

#model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
alexnet = models.alexnet(pretrained=True)
# Load pre-trained ResNet model
#model = models.resnet152(pretrained=True)
alexnet.eval()  # Set model to evaluation mode

# Define image preprocessing steps (resize, normalize)
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Load and pre-process your PNG image
image = Image.open('C:/Users/Peter/OneDrive - University of Bath/Pictures/hopefulcloud.png').convert('RGB') # Load your PNG image using PIL
image = transform(image)

# Add a batch dimension for the model
image = torch.unsqueeze(image, 0)

output = alexnet(image)
# Get predictions
#with torch.no_grad():
#    output = model(image)

with open('imagenet_classes.txt') as f:
  classes = [line.strip() for line in f.readlines()]

_, index = torch.max(output, 1)
 
percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
 
print(classes[index[0]], percentage[index[0]].item())

# Analyze probability distribution for clues about image type
#probabilities = torch.nn.functional.softmax(output[0], dim=0)
# ... analyze probabilities here
#print()
#print(probabilities)