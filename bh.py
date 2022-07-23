import yaml
import os
from copy import deepcopy
# The command line is create bigtop top hiera yaml config file
def mkdir(path):
    paths = os.getcwd()
    path = os.path.join(paths, path)
    if not os.path.exists(path): 
      os.mkdir(path)

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

    mkdir("tmp")
    # print(nodes[i])
    with open("tmp/" + nodes[i]["hostname"] + "_site.yaml", 'w') as a:
      yaml.dump(config_dict, a)