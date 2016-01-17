from subprocess import call
import os
import json
import pandas as pd


def _make_r_call( file_args ):
    '''
    Make system call to rds_to_pandas.R to convert .rds file to json
    '''

    # run R via system call, using littler
    call_args = [ '/usr/local/bin/lr', file_args['rds_to_pandas'], 
                  file_args['f'], file_args['out1'], file_args['out2'] ] 

    # capture R output to R_output.txt
    with open( "../data/R_output.txt", "w" ) as f:
        call( call_args, stdout = f, stderr = f )

              # rds_to_pandas = '/Users/kdelrosso/Github/R-dataframe-to-Pandas/rds_to_pandas.R',
def read_rds( filename, 
              out_file1 = '../data/temp_rds_to_csv.csv', 
              out_file2 = '../data/temp_rds_to_json_coltypes.csv',
              keep_temp = False ):
    '''
    INPUT: 
        - filename: of .rds file
        - out_file1 / out_file2: where to write temp .csv files
        - rds_to_pandas: full path (no ~/) to rds_to_pandas.R file
    OUTPUT: pandas data frame
    DOC: use keep_temp = True to retain temporary .csv files
    '''
    
    # full path to load_rds.py    
    dir_of_file = os.path.dirname(os.path.abspath(__file__))

    # arguments to _make_r_call()
    args = {'f': os.path.abspath( filename ), 
            'out1': os.path.abspath( out_file1 ),
            'out2': os.path.abspath( out_file2 ),
            'rds_to_pandas': dir_of_file + '/rds_to_pandas.R' }

    _make_r_call( args )

    # converting R to pandas dtypes
    R_to_pandas = { 'character': object,
                    'factor': object,
                    'integer': int,
                    'numeric': float,
                    'complex': complex,
                    'logical': bool }

    # if we get an error in R, mostly likely we couldn't find the .rds file
    try:
        with open( args['out2'], 'r' ) as f:
            R_types = json.loads( f.readlines()[0] )
    except IOError:
        raise IOError( "Problem with {0}, likely file doesn't exist or is not .rds format".format( filename ) )

    # convert R classes to pandas dtypes
    col_types = { str(k) : R_to_pandas[ v[0] ] for k, v in R_types.iteritems() }

    # read data into pandas
    df = pd.read_csv( args['out1'], dtype = col_types )

    if not keep_temp:
        # remove temporary files
        os.remove(out_file1)
        os.remove(out_file2)

    return df