import yaml
from copy import deepcopy
with open('sample.yaml', 'r') as f:
  doc = yaml.load(f, Loader=yaml.FullLoader)
  nodes = doc["nodes"]
  config_common_list = [
    ("bigtop::hadoop_head_node", doc["head_node"]),
    ("hadoop::hadoop_storage_dirs", doc["storage_dirs"]),
    ("bigtop::roles_enabled", "true"),
    ]
  for key, value in doc["configs"].items():
    config_common_list.append((key, value))
  config_dict_list = []

  for i in range(0, len(nodes)): 
    config_result = deepcopy(config_common_list)
    config_result.append(("bigtop::roles", nodes[i]["roles"]))
    if nodes[i]["configs"] is not None:
      for key, value in nodes[i]["configs"].items():
        config_result.append((key, value))
    config_dict = dict(config_result)
    # print(nodes[i])
    with open(nodes[i]["hostname"] + "_site.yaml", 'w') as a:
      yaml.dump(config_dict, a)

