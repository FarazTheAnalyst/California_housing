#!/bin/bash

uvicorn app:app --host 0.0.0.0 --port 8000 &

strealit run streamlit_app.py \
    --server.port=7869 \
    --server.address=0.0.0.0