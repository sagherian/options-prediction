# Options Prediction Project

This project aims to predict call options in the options market using a classification approach. It leverages historical options data to train a machine learning model and make predictions on current market states.

## Project Structure

```
options-prediction
├── data
│   ├── raw                # Directory for raw historical options data files
│   ├── processed          # Directory for processed data files ready for model training
├── src
│   ├── data_loader.py     # Class for loading historical options data
│   ├── data_preparation.py # Class for preparing data for training
│   ├── model.py           # Class defining the options prediction model
│   ├── train.py           # Function for training the model
│   ├── predict.py         # Function for making predictions with the trained model
│   └── utils.py           # Utility functions for various tasks
├── notebooks
│   └── exploratory_analysis.ipynb # Jupyter notebook for exploratory data analysis
├── requirements.txt       # List of project dependencies
├── .gitignore             # Files and directories to ignore by Git
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd options-prediction
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Place your raw historical options data files in the `data/raw` directory.

## Usage

1. Load the data using the `DataLoader` class from `src/data_loader.py`.
2. Prepare the data for training using the `DataPreparation` class from `src/data_preparation.py`.
3. Train the model using the `train_model` function from `src/train.py`.
4. Make predictions on current options data using the `make_predictions` function from `src/predict.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.