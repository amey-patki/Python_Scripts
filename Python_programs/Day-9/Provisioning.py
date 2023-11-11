def provision_server(server_name):
    print (f"Provisioning monitoring agents on {server_name}... Done !")


server_names=['server1', 'server2', 'server3']

for server_name in server_names:
    provision_server(server_name)
