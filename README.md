# Fairness Evaluator

## Git clone

Clone repositroy:
```bash
git clone https://github.com/XXXX/XXXX.git
```

In the main project folder, use the following command:

```bash
python setup.py install --user
```

From files in the main directory, you should be able to use
```bash
from FairnessEvaluator import FairnessEvaluator
```
Note that this does not work for subfolders.


## Install as package

Install package: 
```bash
pip install git+https://github.com/XXX/XXX.git
```
For installation from any branch with name [branch name]:
```bash
pip install git+https://github.com/XXXX/XXXX.git@[branch name] 
```

Test code:
```python
import numpy as np 
import pandas as pd
from FairnessEvaluator import FairnessEvaluator

data_raw = pd.read_csv('X.csv', sep=',')
y = data_raw['G3'].to_numpy()
X = data_raw.drop(columns=['Unnamed: 0','G3'])
X['label_value'] = y
X['idx'] = X.index
X = X[X['Medu'] != 0]
X = X.reset_index(drop=True)

fo = FairnessEvaluator(X,
                      'label_value',
                      'sex',
                      metrics=['es','tpr','fpr','fnr'],
                      metrics_to_plot=['tpr','fpr','fnr','es'],
                      fairness_bounds=[0.9,1.1],
                      metric_fairness_bounds={'es':[0.5,1.5], 'tpr': [0.7,1.3]},
                      fully_constrained=False,
                      precision_ub = 0.7)        
fo.evaluate()

```
