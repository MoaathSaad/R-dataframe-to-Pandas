# R-dataframe-to-Pandas
Python package to load a saved R dataframe into Pandas.

<hr>

A package to load a saved .rds R data frame into Pandas. We simply load the data into R, saved as a temporary .csv file and a temporary .json file containing the column types, and then load the .csv into Pandas. Finally we delete the temporary files.

To install run

<pre><code> 
python setup.py install
</code></pre>

from the terminal. Then simply use

<pre><code> 
from load_rds import read_rds

df = read_rds( 'my_saved_data.rds' )
</code></pre>

from Python.