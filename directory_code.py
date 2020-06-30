# imports
from pathlib import Path

# variables
vols_path = Path('/Volumes/library/DigitalProduction/0_ActiveProjects/lady-vols-basketball')

# functions
def get_identifier(file_path):
    image_stem = file_path.stem
    identifier = image_stem[:-4]
    return identifier

if __name__ == "__main__":

    jpg_list = sorted(vols_path.glob('*.jpg'))

    jpg_list = [x for x in jpg_list if not x.stem.startswith('.')]

    for path in jpg_list:
        identifier = get_identifier(path)
        new_dir_path = vols_path.joinpath(identifier)
        new_dir_path.mkdir(exist_ok=True)
        final_path = new_dir_path.joinpath(path.name)
        path.rename(final_path)
