# ECN API Service

## UPDATE: TensorFlow model

For TensorFlow H5 model, see https://drive.google.com/open?id=1-JlAKGv2uSWTSGJCU7eZJ8tnCErY1SeX

## Prepare venv

    python -m venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Pytorch

Windows, Python 3.7, CPU only no CUDA: (56 MB)

    pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp37-cp37m-win_amd64.whl


Torch 1.3.1 using CPU:
    
        pip install torch==1.3.1+cpu torchvision==0.4.2+cpu -f https://download.pytorch.org/whl/torch_stable.html


## Deployment Configuration

Environment variables (for production, use PPTIK MongoDB server and `ecn` database)

    MONGODB_URI=mongodb://localhost/ecn

Set these configuration in `.env` file.

## Run Locally

    Set configuration in `.env` file as above.

    set FLASK_APP=ecnsvc.py
    python -m flask run
