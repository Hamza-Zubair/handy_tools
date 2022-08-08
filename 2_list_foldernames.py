from pathlib import Path
import numpy as np
from datetime import datetime

#Function to take directory path as input and give a CSV containing names of all folders in the directory
def is_folder(input_dir):
    """"
    writes a csv file containing folder names from input directory
    """
    directory = Path(input_dir)
    folder_names = [folder.stem for folder in directory.glob('*') if folder.is_dir() is True]
    csv_name = 'folder_names_{}.csv'.format(datetime.now().strftime("%Y_%m_%d-%I-%M-%S%p"))
    csv_path = Path.joinpath(directory,csv_name)
    np.savetxt(csv_path, folder_names, delimiter=",", fmt="%s", header='Childfolders_in_directory: {}'.format(directory.stem))

    
def main():
    input_raw = input('give the directory path for which u need list of folder names')
    input_dir=Path(input_raw)
    if input_dir.is_dir() is True:
        is_folder(input_dir)
        print('CSV written for the given input directory')
    else:
        #is_folder(Path.cwd()) for jupyterlab
        is_folder((Path(__file__).parent))
        print('Invalid input directory, CSV written for folders(if any) on script location') 

        
if __name__=='__main__':
    main()