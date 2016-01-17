# R-dataframe-to-Pandas

A package to load a saved .rds R data frame into Pandas. The package simply loads the data into R, saves it as a temporary .csv file and a temporary .json file containing the column types, and then loads the .csv data into Pandas.

To install run

<pre><code> python setup.py install</code></pre>

from the terminal. Then simply use

<pre><code>from load_rds import read_rds

df = read_rds( 'my_saved_data.rds' )</code></pre>

from Python.