def deploy_configuration(environment):
    # Simulate the deployment of configuration changes for the environment
    print(f"Deploying configuration changes to {environment}... Done!")

# List of environment names
environments = ['development', 'staging', 'production']

# Deploy configurations to each environment using a for loop
for environment in environments:
    deploy_configuration(environment)
