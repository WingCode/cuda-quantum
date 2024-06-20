# ============================================================================ #
# Copyright (c) 2022 - 2024 NVIDIA Corporation & Affiliates.                   #
# All rights reserved.                                                         #
#                                                                              #
# This source code and the accompanying materials are made available under     #
# the terms of the Apache License 2.0 which accompanies this distribution.     #
# ============================================================================ #

#[Begin Docs]
import cudaq

# Build a cudaq kernel.


@cudaq.kernel
def kernel():
    # Allocate a single qubit to the kernel.
    qubit = cudaq.qubit()
#[End Docs]
