import azureml.core
from azureml.core import Workspace, Dataset, Experiment, Run
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def main():
    # Configuração do workspace
    ws = Workspace.from_config()

    # Carrega dataset
    dataset = Dataset.get_by_name(ws, name='bike_rental_dataset')
    data = dataset.to_pandas_dataframe()

    # Preparação dos dados
    X = data[['temperature', 'humidity', 'windspeed']]  
    y = data['rental_count'] 

    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelo de regressão
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Salvar o modelo treinado
    joblib.dump(model, 'model.pkl')

    print("Modelo treinado e salvo com sucesso!")

if __name__ == "__main__":
    main()
