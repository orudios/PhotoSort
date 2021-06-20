import os 

def photo_sort():
    # Populate with most common raw photo file extensions
    # Source: https://en.wikipedia.org/wiki/Raw_image_format
    RAW_IMAGE_FORMATS = [
        '3fr', 'ari', 'arw', 'bay', 'braw', 'crw', 'cr2', 'cr3', 'cap', 'data', 'dcs', 'dcr', 'dng', 'drf',
        'eip', 'erf', 'fff', 'gpr', 'iiq', 'k25', 'kdc', 'mdc', 'mef', 'mos', 'mrw', 'nef', 'nrw', 'obm',
        'orf', 'pef', 'ptx', 'pxn', 'r3d', 'raf', 'raw', 'rw1', 'rw2', 'rwz', 'sr2', 'srf', 'srw', 'tif', 'x3f'
    ]

    # Populate with most common video file extensions
    # Source: https://videoconverter.wondershare.com/dv/full-guide-to-camera-video-file-formats.html
    VIDEO_FORMATS = [
        'mp4', 'm4p', 'm4b', 'm4r', 'm4v', 'm4a', 'divx', 'evo', 'f4v', 'flv',
        'avi', 'qt', 'mxf', 'mov', 'mts', 'm2ts', 'mpeg', 'vob', 'ifo'
    ]

    # Iterate through each file in the directory
    for file in os.listdir(os.curdir):
        # Extract the file extension from the full path, without the '.'
        file_extension = os.path.splitext(file)[1][1:].lower()

        # Create an empty directory for future edits
        createDirectory('Edits')

        # If directory has RAW images, create a folder for them
        if file_extension in RAW_IMAGE_FORMATS:
            populateDirectory(file, 'RAW')

        # If directory has videos, create a folder for them
        if file_extension in VIDEO_FORMATS:
            populateDirectory(file, 'Video')

        # If directory has JPEG images, create a folder for them too
        if file_extension == 'jpeg' or file_extension.lower() == 'jpg':
            populateDirectory(file, 'JPEG')
        

def createDirectory(dir):
    # Check if directory with name dir exists, if not, create it 
    if not os.path.isdir(dir):
        os.mkdir(dir)

def moveFile(dir, file):
    # Move file from its current location into dir
    os.replace(file, f'{dir}/{file}')

def populateDirectory(file, dir):
    # Create the directory and move files
    createDirectory(dir)
    moveFile(dir, file)

if __name__ == '__main__':
    photo_sort()