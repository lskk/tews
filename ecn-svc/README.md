# ECN API Service

## Pytorch

Windows, Python 3.7, CPU only no CUDA: (56 MB)

    pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp37-cp37m-win_amd64.whl


## Deployment Configuration

Environment variables (for production, use PPTIK MongoDB server and `ecn` database)

    MONGODB_URI=mongodb://localhost/ecn

Set these configuration in `.env` file.

## Run Locally

    Set configuration in `.env` file as above.

    set FLASK_APP=ecnsvc.py
    python -m flask run
