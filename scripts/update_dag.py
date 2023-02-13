import zipfile
import json

# read dag.json
with open("dag.json", "r") as f:
    dag_content = json.load(f)

# read ecco_cdp_gold_retailmanagement.json
with open("ecco_cdp_gold_retailmanagement.json", "r") as f:
    gold_content = json.load(f)

# overwrite current graph node variable
gold_content["graph"] = dag_content

# save changes in ecco_cdp_gold_retailmanagement.json file
with open("ecco_cdp_gold_retailmanagement.json", "w") as f:
    json.dump(gold_content, f, indent=4)
