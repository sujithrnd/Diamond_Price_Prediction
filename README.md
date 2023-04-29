## End To End ML Project

### created a environment
```
conda create -p envdp python==3.8

conda activate envdp/
```
### Install all necessary libraries
```
pip install -r requirements.txt
### remove all your env
conda remove --name ENVIRONMENT --all

python src/pipeline/training_pipeline.py
python src/pipeline/prediction_pipeline.py