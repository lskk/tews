# ECN API Service

## Prepare venv

    python -m venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Pytorch

Windows, Torch 1.3.1 using CPU no CUDA: (56+ MB)
    
        pip install torch==1.3.1+cpu torchvision==0.4.2+cpu -f https://download.pytorch.org/whl/torch_stable.html


## Deployment Configuration

Environment variables (for production, use PPTIK MongoDB server and `ecn` database)

    MONGODB_URI=mongodb://localhost/ecn

Set these configuration in `.env` file.

## Run Locally

Set configuration in `.env` file as above.

    set FLASK_APP=tpsvc.py
    python -m flask run

API URL: http://localhost:5000/tsunamiPotential/predict
