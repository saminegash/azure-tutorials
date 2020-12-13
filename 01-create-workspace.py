# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='aml-workspace',  # provide a name for your workspace
                      # provide your subscription ID
                      subscription_id='5c49484d-4088-4ada-a37f-0e0c3d2813d4',
                      resource_group='aml-resource',  # provide a resource group name
                      create_resource_group=True,
                      location='eastus2')  # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')
