import torch
import torchvision
import torchvision.transforms as transforms

# print("yyx")
# # transform = transforms.Compose(
# #     [transforms.ToTensor(),
# #      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
#
# trainset = torchvision.datasets.CIFAR10(root='./cifar_data', train=True,
#                                         download=True, transform=None)
# trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
#                                           shuffle=True, num_workers=2)
#
# testset = torchvision.datasets.CIFAR10(root='./cifar_data', train=False,
#                                        download=True, transform=None)
# testloader = torch.utils.data.DataLoader(testset, batch_size=4,
#                                          shuffle=False, num_workers=2)
#
if __name__ == '__main__':
    trainset = torchvision.datasets.CIFAR100(root='./cifar_data', train=True,
                                             download=True, transform=None)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                              shuffle=True, num_workers=2)

    testset = torchvision.datasets.CIFAR100(root='./cifar_data', train=False,
                                            download=True, transform=None)
    testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                             shuffle=False, num_workers=2)
