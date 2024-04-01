from copy import deepcopy
from utils import *
from matplotlib import pyplot as plt


# Get Model and data
use_random_labels = False
model_name = 'vgg11_bn'  # 'resnet20', 'vgg13_bn',...
epochs = 30
learning_rate = 0.01



train_loader = get_dataloader(use_random_labels, train=True)
images = torch.cat([batch[0] for batch in train_loader])
# compute pca from 10K images, no need for all 50K.
images = images[torch.randperm(images.shape[0])][:10000]
num_images = images.shape[0]

patches = images.unfold(1, 3, 1).unfold(2, 3, 1).unfold(3, 3, 1).to(torch.float64)

pca = torch.pca_lowrank(patches.flatten(-3).flatten(0, -2), q=27)

torch.save(pca,"DTD_vgg_pca.pt")


