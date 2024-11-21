import os
import shutil

# SAMPLE API_KEY and AZURE_ENDPOINT
# API_KEY="1234abcd5678ef901234abcd5678ef90"
# AZURE_ENDPOINT="https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat/completions?api-version=2024-06-01"
API_KEY = "TO_BE_REPLACED"
AZURE_ENDPOINT = "TO_BE_REPLACED"

local_config_path = os.path.join(os.path.dirname(__file__), 'local_azure_openai_config.py')

if not os.path.exists(local_config_path):
    shutil.copy(__file__, local_config_path)
    print("local_azure_openai_config.py has been created. Please update the API_KEY and AZURE_ENDPOINT.")
else:
    from config.local_azure_openai_config import API_KEY, AZURE_ENDPOINT

if API_KEY == "TO_BE_REPLACED" or AZURE_ENDPOINT == "TO_BE_REPLACED":
    raise ValueError("Please update the API_KEY and AZURE_ENDPOINT in local_azure_openai_config.py")