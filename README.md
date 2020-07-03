# CSVMapRange
# Language: Python
# Input: prefix (for two CSV files of abundances)
# Output: CSV (first CSV file, mapped into the range of the second)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin to map the range of values of one CSV file to the range of values of another.
This can be useful for example when mapping a weighted network to the range of an unweighted network
like the attached example, but can also be useful when using multiple types of data that
have been measured using different metrics (i.e. multiomics).

The plugin accepts as input a prefix and then will assume the file to be mapped is prefix.file1.csv
and the file with the target range is prefix.file2.csv.  It will then take all values in prefix.file1.csv
and scale them accordingly, producing output in the user-specified outputfile.
