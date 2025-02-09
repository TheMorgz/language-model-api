# app/__init__.py

# Import main FastAPI app instance for easier access
from .main import app

# Optionally, import other modules or resources
from .models import TextCompletionRequest, TextSummarizationRequest

# You can also include package-level variables or configurations
__version__ = "1.0.0"