def install_package(package_name):
    try:
        # Install Python packages using pip
        print(f"Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f'{package_name} installed successfully')
    except subprocess.CalledProcessError:
        print(f'Failed to install {package_name}')
