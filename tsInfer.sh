ssh -Y ich@beluga.computecanada.ca
cd yourDirectory

module load python gcc
virtualenv --no-download tsinfer
source tsinfer/bin/activate
pip install scipy-stack
pip install pandas 


salloc --time=3:00:00 --mem=50G --account=def-haricots

python

>>> exec(open('ConvertData.py').read())
>>> createSampleData(geno, locations) # this function is defined in ConverData.py
>>> inferred_ts = ts.infer(sample_data) # us ts.infer to infer the tree sequence
