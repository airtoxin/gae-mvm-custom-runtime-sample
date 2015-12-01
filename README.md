# Google App Engine Managed VM and Custom Runtime sample

GAE Managed VM and Custom Runtime sample app.

Managed VM provides Virtual Machine on GAE. Custom Runtime provides Docker Container on GAE.


## deploy to GAE

`$ gcloud preview app deploy app.yaml --promote`

## test localy

If you have python3, simply run `$ python3 main.py`.

1. install `direnv` and `pyenv`
2. enter this repository
3. `$ direnv allow .` (don't pay attentions for any errors!)
4. `$ pyenv install 3.4.3` (then install python3.4.3 to .pyenv directory)
5. re-run `$ direnv allow .`
6. `$ python3 main.py`
