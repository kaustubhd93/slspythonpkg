import os
import sys
from ruamel.yaml import YAML

def get_sls_data():
    sls_data = {}
    work_dir = os.getcwd()
    serverless_file = f"{work_dir}/serverless.yml"
    yaml = YAML()
    with open(serverless_file, "r+") as stream:
        ymlDict = yaml.load(stream)
    sls_data['runtime'] = ymlDict['provider']['runtime']
    sls_data['build_dir'] = ymlDict['custom']['pkgPyFuncs']['buildDir']
    sls_data['requirements_file'] = ymlDict['custom']['pkgPyFuncs']['requirementsFile']
    sls_data['global_requirements'] = ymlDict['custom']['pkgPyFuncs']['globalRequirements']
    sls_data['functions'] = list(ymlDict['functions'])
    sls_data['functions_data'] = ymlDict['functions']
    return sls_data

def download_deps(func,stage):
    sls_data = get_sls_data()
    if func not in sls_data['functions']:
        print(f"Function {func} not found.")
        sys.exit(1)
    src_code_dirs = sls_data['functions_data'][func]['package']['include']
    artifact_dir = (sls_data['functions_data'][func]['package']['artifact']).split("/")[1].split("${opt:stage}")
    print(artifact_dir)

def zip_dir():
    return True