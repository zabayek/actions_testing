import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dag_file', help='path to the DAG file')
parser.add_argument('-rm_file', help='path to the RetailManagement file')
parser.add_argument('-proj_ver', help='version of the project')

args = parser.parse_args()

dag_file = args.dag_file
rm_file = args.rm_file
proj_ver = args.proj_ver


print(dag_file, rm_file, proj_ver)



# pr(dag_file="dag.json", rm_file="ecco_cdp_gold_retailmanagement.json", proj_ver="rm1.2.3333")
