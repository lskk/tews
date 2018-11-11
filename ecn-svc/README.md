# ECN API Service

## Pytorch

Windows, no CUDA: (56 MB)

    pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-win_amd64.whl


## Deployment Configuration

Environment variables (for production, use PPTIK MongoDB server and `ecn` database)

    MONGODB_URI=mongodb://localhost/ecn

## Run Locally

    set FLASK_APP=ecnsvc.py
    python -m flask run
