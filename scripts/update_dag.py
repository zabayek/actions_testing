import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dag_file', help='path to the DAG file')
parser.add_argument('-rm_file', help='path to the RetailManagement file')
parser.add_argument('-proj_ver', help='version of the project')

args = parser.parse_args()

dag_file = args.dag_file
rm_file = args.rm_file
proj_ver = args.proj_ver


# read dag.json
with open(dag_file, "r") as f:
    dag_content = json.load(f)

# read ecco_cdp_gold_retailmanagement.json
with open(rm_file, "r") as f:
    gold_content = json.load(f)

# overwrite current graph node variable
gold_content["graph"] = dag_content
gold_content["project_version"] = proj_ver


# save changes in ecco_cdp_gold_retailmanagement.json file
with open(rm_file, "w") as f:
    json.dump(gold_content, f, indent=4)


# dag_operate(dag_file="dag.json", rm_file="ecco_cdp_gold_retailmanagement.json", proj_ver="rm1.2.3333")