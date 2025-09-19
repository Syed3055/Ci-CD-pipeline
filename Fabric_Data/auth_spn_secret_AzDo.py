from fabric_cicd import FabricWorkspace, publish_all_items
from azure.identity import ClientSecretCredential
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--WorkspaceId', required=True)
parser.add_argument('--Environment', required=True)
parser.add_argument('--RepositoryDirectory', required=True)
parser.add_argument('--ItemsInScope', required=True)
parser.add_argument('--ClientId', required=True)
parser.add_argument('--ClientSecret', required=True)
parser.add_argument('--TenantId', required=True)
args = parser.parse_args()

credential = ClientSecretCredential(
    client_id=args.ClientId,
    client_secret=args.ClientSecret,
    tenant_id=args.TenantId
)

workspace = FabricWorkspace(
    workspace_id=args.WorkspaceId,
    environment=args.Environment,
    repository_directory=args.RepositoryDirectory,
    item_type_in_scope=args.ItemsInScope.split(","),
    token_credential=credential
)

publish_all_items(workspace)
print(f"✅ Deployment to {args.Environment} completed.")
