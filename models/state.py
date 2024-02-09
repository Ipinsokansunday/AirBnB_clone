#!/usr/bin/env python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initializes State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
