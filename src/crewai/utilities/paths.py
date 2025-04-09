import os
from pathlib import Path

import appdirs

"""Path management utilities for CrewAI storage and configuration."""

def db_storage_path() -> str:
    """Returns the path for SQLite database storage.

    Returns:
        str: Full path to the SQLite database file
    """
    task_storage_path = get_task_storage_path()
    if task_storage_path:
        return task_storage_path
    
    app_name = get_project_directory_name()
    app_author = "CrewAI"

    data_dir = Path(appdirs.user_data_dir(app_name, app_author))
    data_dir.mkdir(parents=True, exist_ok=True)
    return str(data_dir)


def get_project_directory_name():
    """Returns the current project directory name."""
    project_directory_name = os.environ.get("CREWAI_STORAGE_DIR")

    if project_directory_name:
        return project_directory_name
    else:
        cwd = Path.cwd()
        project_directory_name = cwd.name
        return project_directory_name
    
def get_task_storage_path() -> str | None:
    """Returns the path for task storage.
    Returns:
        str: Full path to the task storage directory.
    """
    task_id = os.getenv("CW_TASK_ID")
    if not task_id:
        return None
    
    project_directory_name = get_project_directory_name()
    task_storage_path = Path(project_directory_name) / "data" / task_id
    task_storage_path.mkdir(parents=True, exist_ok=True)
    return str(task_storage_path)