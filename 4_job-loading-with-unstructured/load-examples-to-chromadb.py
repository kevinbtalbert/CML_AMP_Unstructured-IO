import os
import subprocess
import configparser

# Internal configuration dictionary
internal_config = {
    'pdfs_root_directory': '/home/cdsw/assets/example-docs/pdf/DA-619p.pdf',
    'htmls_root_directory': '/home/cdsw/assets/example-docs/htmls/',
    'vector_db_path': '/home/cdsw/assets/examples-chromadb',
    'batch_size': 10
}

# List of other Python scripts to run
scripts_to_run = [
    'load-pdfs-to-chromadb.py',
    'load-htmls-to-chromadb.py'
]

def run_script_with_config(script, config):
    """
    Run a Python script with specified configurations.
    """
    # Set environment variables based on the provided configuration
    env = os.environ.copy()
    for key, value in config.items():
        env[key.upper()] = str(value)

    # Execute the script
    try:
        print(f"Running {script} with config: {config}")
        subprocess.run(['python', script], env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")

def load_config_from_file(file_path='config.ini'):
    """
    Load configuration from the config.ini file.
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    return {
        'pdfs_root_directory': config['settings']['pdfs_root_directory'],
        'htmls_root_directory': config['settings']['htmls_root_directory'],
        'vector_db_path': config['settings']['vector_db_path'],
        'batch_size': int(config['settings'].get('batch_size', 10))
    }

if __name__ == "__main__":
    # Decide whether to use internal config or load from file
    use_internal_config = True  # Set this to False to use the config.ini file

    # Load the appropriate configuration
    config = internal_config if use_internal_config else load_config_from_file()

    # Run each script with the loaded configuration
    for script in scripts_to_run:
        run_script_with_config(script, config)
