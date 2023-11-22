def update_server_config(file_path,key,value):
    with open(file_path,'r') as file:
        lines=file.readline()

    with open(file_path,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" +value+ "\n")
            else:
                file.write(line)

server_config_file= 'server.conf'

key_to_update='MAX_CONNECTION'
new_value= '700'

update_server_config(server_config_file,key_to_update,new_value)