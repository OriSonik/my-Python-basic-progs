def split_row(row):
    row = row.replace('\n','')
    return row.split(',')

def import_data(filename='albums_data.txt'):
    with open(filename) as f:
        album_list = f.readlines()
    return list(map(split_row, album_list))

def export_data(albums, filename='albums_data.txt', mode='a'):
    mode = input('Please choose [w] to overwrite an existing album or [a] to add an album to the existing library')
        if mode == 'w' or mode == 'a':
            if mode == 'w':
            
            else:
        else:
            raise ValueError
            print('Wrong write mode')

    
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list albums: albums' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """

