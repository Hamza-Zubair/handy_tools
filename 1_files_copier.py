from pathlib import Path
import shutil
# function to copy specific files from directory and sub directories
def files_copier(source, extension):
    """
    Copies all files of specified extension from source directory/sub-directories
    Input:
    -----
    source: directory path from where the files to be copied
    extension: str or tuple of str.
    Output:
    -----
    "out" folder in source directory with separated files
    """ 
    # CHECK IF SOURCE DIRECTORY EXISTS OR ELSE THROW EXCEPTION
    source = Path(source)
    if Path.is_dir(source) is True:
        destination = Path.joinpath(source, 'out')
        if Path.exists(destination) is True:
            shutil.rmtree(destination, ignore_errors=True)
            Path.mkdir(destination, exist_ok=True)
        else:
            Path.mkdir(destination)
        for folders in source.glob('**'):
            for file in folders.iterdir():
                path_file = Path.joinpath(folders,file)
                if path_file.suffix in extension:
                    try:
                        shutil.copy(path_file, destination)
                    except:
                        pass
    else:
        raise Exception("Source directory not found")
    # print the count of extracted files to out folder in console
    count = len(list(destination.glob('*')))
    if  count > 0:
        print('{} file/s copied'.format(str(count)))
    else:
        print('No files found with extension: {} '.format(extension))



# set source directory
src = r'YourPathHere'
# extension/s of file/s to be seperated. can be single str or tuple of str,
ext = ('.shp','.dbf','.prj','.py')
# run the function
files_copier(src ,ext)