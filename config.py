#Config File

import kagglehub
from pathlib import Path
def get_data_path():
    return Path(
        kagglehub.dataset_download("towardsentropy/oil-storage-tanks")
    )