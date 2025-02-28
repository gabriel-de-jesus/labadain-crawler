import os
import hydra
from hydra.core.config_store import ConfigStore
from common_utils.config import PipelineConfig

# Hydra Config
cs = ConfigStore.instance()
cs.store(name="pipeline_config", node=PipelineConfig)


def create_essential_files(file_paths):
    """Ensure required files exist."""
    for file in file_paths:
        os.makedirs(os.path.dirname(file), exist_ok=True)  # Ensure parent directory exists
        if not os.path.exists(file):
            open(file, 'w').close()  # Create an empty file


@hydra.main(config_path=os.path.abspath("pipeline/conf"), config_name="config", version_base=None)
def create_files(cfg: PipelineConfig):
    """Hydra-managed function to create required files."""
    file_paths = [os.path.join(cfg.paths.data, file) for file in cfg.files.file_names]
    create_essential_files(file_paths)


# Ensure the required files are created before executing seeder
create_files()
