from utils.data import load_data, train_model, save_model

def run_process():
    
    X_train, _, Y_train, _ = load_data()
    model = train_model(X_train, Y_train)
    save_model(model)