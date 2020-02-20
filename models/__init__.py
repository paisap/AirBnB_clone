from models.engine.file_storage import FileStorage
from models import base_model
""" models/__init__.py updated to create a unique FileStorage """

storage = FileStorage()
storage.reload()
