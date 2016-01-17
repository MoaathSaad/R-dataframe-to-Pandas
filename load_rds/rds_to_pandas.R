#!/usr/bin/env r

# for running in Rstudio, since argv doesn't exist
try_catch = try( length(argv), silent = TRUE )
if( class(try_catch) == "try-error" ){
    rm(list = ls())
    setwd("~/Dropbox/Davis/Winter_2016/Data_Science/hw_1/")
    argv = list()
}

require(jsonlite)

convert_rds_to_json = 
    # INPUT: as .rds file containing a data frame
    # OUTPUT: NULL
    # DOC: saves two files: one containing the data frame data as csv,
    #   the other contains the column type information as json
function( filename, output_file_df, output_file_coltypes )
{
    # write data frame data out as csv
    df = readRDS( filename )
    write.csv( df, file = output_file_df, row.names = FALSE )
    
    # write data frame column classes out as json
    col_classes = toJSON( lapply( df, class ) )
    write( col_classes, output_file_coltypes )
}

####################
# Running the Code #
####################

if( length(argv) == 0 ) {
    filename = '/Users/kdelrosso/Dropbox/Davis/Winter_2016/Data_Science/hw_1/test_save.rds'
    output_file_df = "~/Desktop/temp_rds_to_csv.csv"
    output_file_coltypes = "~/Desktop/rds_to_json_coltypes.csv"
} else {
    print( "Using command line inputs..." )
    print( argv )
    filename = argv[1]
    output_file_df = argv[2]
    output_file_coltypes = argv[3]
}

convert_rds_to_json( filename, output_file_df, output_file_coltypes )
