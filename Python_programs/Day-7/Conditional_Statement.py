import sys

type= sys.argv[1]

if type =="t2.micro":
    print("Will create t2-micro instance for you")

elif type =="t2.medium":
    print("Will create t2-medium instance for you")

elif type == "t2.xlarge":
    print(" Will create t2-slarge instace for you")

else:
    print("Enter valid Instance type")