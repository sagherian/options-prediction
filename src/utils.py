def load_config(config_path):
    import json
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def calculate_accuracy(predictions, labels):
    correct = (predictions == labels).sum().item()
    accuracy = correct / len(labels)
    return accuracy

def plot_metrics(metrics):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(metrics['train_loss'], label='Train Loss')
    plt.plot(metrics['val_loss'], label='Validation Loss')
    plt.title('Loss Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()