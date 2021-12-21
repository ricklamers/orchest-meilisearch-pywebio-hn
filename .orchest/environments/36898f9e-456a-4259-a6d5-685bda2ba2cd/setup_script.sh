#!/bin/bash

# Install any dependencies you have in this shell script.
pip install --upgrade pip
pip install --no-cache-dir pywebio requests meilisearch git+https://github.com/orchest/orchest.git#egg=orchest\&subdirectory=orchest-sdk/python