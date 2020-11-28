""" Collection of keyword and operator identifiers """

from typing import *
from dataclasses import dataclass, field

@dataclass
class ActionDescriptor:
    n_args: int
    arg_types: Any


# Table of operators and their relevant information
operator_table: Dict[str, ActionDescriptor] = {

        # Actions descriptors function as a generalized
        # way of validating action calls in the compiler
        "assign": ActionDescriptor(2, (str, int)),
        "write": ActionDescriptor(1, (str, int)),
        "add": ActionDescriptor(2, (str, int)),
        "sub": ActionDescriptor(2, (str, int)) 
    }



