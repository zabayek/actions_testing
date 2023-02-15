import json

# read dag.json
with open("actions_testing/dag.json", "r") as f:
    dag_content = json.load(f)

# read ecco_cdp_gold_retailmanagement.json
with open("variables/.helm/ecco_cdp_gold_retailmanagement.json", "r") as f:
    gold_content = json.load(f)

# overwrite current graph node variable
gold_content["graph"] = dag_content
gold_content["project_version"] = proj_ver


# save changes in ecco_cdp_gold_retailmanagement.json file
with open("variables/.helm/ecco_cdp_gold_retailmanagement.json", "w") as f:
    json.dump(gold_content, f, indent=4)


# dag_operate(dag_file="dag.json", rm_file="ecco_cdp_gold_retailmanagement.json", proj_ver="rm1.2.3333")