from subprocess import call
import os
import json
import pandas as pd


DEFAULT_LITTLER_PATH = '/usr/local/bin/lr'
TEMP_CSV_LOCATION = '../data/temp_rds_to_csv.csv'
TEMP_COLTYPES_LOCATION = '../data/temp_rds_to_json_coltypes.json'
CAPTURE_R_OUTPUT = '../data/R_output.txt'

class ReadRDS(object):
    """Load a saved .rds R dataframe into Pandas.

    Parameters
    ----------
    filename: string, name of .rds file
    littler_path: full path to littler
    """

    def __init__(self, filename, littler_path):
        self.filename = filename
        self.littler_path = littler_path

    def make_r_call(self):
        """Make system call to rds_to_pandas.R to convert .rds file to json."""

        call_args = [
            self.littler_path,
            self.full_path_to_R_script,
            self.full_path_filename,
            self.full_path_temp_csv_location,
            self.full_path_temp_coltypes_location
        ]

        with open(CAPTURE_R_OUTPUT, 'w') as f:
            # run R via system call using littler and capture R output
            call(call_args, stdout=f, stderr=f)

    def rds_to_pandas(self):
        """Output saved R dataframe as pandas DataFrame."""

        # full path to load_rds.py
        dir_of_file = os.path.dirname(os.path.abspath(__file__))

        self.full_path_filename = os.path.abspath(self.filename)
        self.full_path_temp_csv_location = os.path.abspath(TEMP_CSV_LOCATION)
        self.full_path_temp_coltypes_location = os.path.abspath(TEMP_COLTYPES_LOCATION)
        self.full_path_to_R_script = dir_of_file + '/rds_to_pandas.R'
        self.make_r_call()

        # if we get an error in R, mostly likely we couldn't find the .rds file
        try:
            with open(self.full_path_temp_coltypes_location, 'r') as f:
                R_types = json.loads(f.readlines()[0])
        except IOError:
            raise IOError("Problem with {0}, likely file doesn't exist or is not .rds format".format(self.filename))

        # convert R classes to pandas dtypes
        R_to_pandas = {
            'character': object,
            'factor': object,
            'integer': int,
            'numeric': float,
            'complex': complex,
            'logical': bool
        }
        col_types = { str(k) : R_to_pandas[v[0]] for k, v in R_types.iteritems() }

        df = pd.read_csv(self.full_path_temp_csv_location, dtype=col_types)

        # remove temporary files
        os.remove(self.full_path_temp_csv_location)
        os.remove(self.full_path_temp_coltypes_location)

        return df

def read_rds(filename, littler_path=DEFAULT_LITTLER_PATH):

    rds = ReadRDS(filename, littler_path)
    return rds.rds_to_pandas()
