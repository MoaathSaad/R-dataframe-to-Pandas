# R-dataframe-to-Pandas

A package to load a saved .rds R data frame into Pandas. The package simply loads the data into R, saves it as a temporary .csv file and a temporary .json file containing the column types, and then loads the .csv data into Pandas. R is called via <a href = http://dirk.eddelbuettel.com/code/littler.html>littler</a>.

To install run

<pre><code>python setup.py install</code></pre>

from the terminal. Then simply use

<pre><code>from load_rds import read_rds

df = read_rds( 'my_saved_data.rds', littler_path = 'your_path_here' )</code></pre>

from Python.

####Note on littler installation

The default <code>littler_path</code> location for <code>read_rds()</code> is <code>/usr/local/bin/lr</code>. We can configure this path during the littlr installation by running the following from the terminal. On my system (OS X) the <code>installed_littlr_path</code> is <code>/Users/username/Library/R/3.2/library/littler/bin/r</code>. 

<pre><code>echo "install.packages( 'littler', repos='http://cran.us.r-project.org' )" | R --vanilla

# create symbolic link
ln -s your_installed_littlr_path /usr/local/bin/lr
</code></pre>