FROM --platform=linux/amd64 downloads.unstructured.io/unstructured-io/unstructured:latest
FROM --platform=linux/amd64 docker.repository.cloudera.com/cloudera/cdsw/ml-runtime-jupyterlab-python3.11-cuda:2024.05.1-b8

USER root

# Upgrade packages in the base image
# RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libmagic-dev poppler-utils tesseract-ocr tesseract-ocr-eng libreoffice pandoc file
RUN apt-get update && apt-get install -y build-essential libsqlite3-dev

# kj

# Add the packages you want to include in this runtime
# RUN pip install
RUN pip install unstructured[all-docs]
RUN pip install streamlit
RUN pip install chromadb
RUN pip install sentence-transformers
RUN pip install configparser
RUN pip install pysqlite3-binary
RUN pip install python-magic

# Set environment variables
ENV ML_RUNTIME_EDITION="ML Runtime for Unstructured IO" \
    ML_RUNTIME_SHORT_VERSION="6" \
    ML_RUNTIME_MAINTENANCE_VERSION="06" \
    ML_RUNTIME_FULL_VERSION="2024.08.06" \
    ML_RUNTIME_DESCRIPTION="ML Runtime to accompany Cohere Toolkit" \
    ML_RUNTIME_EDITOR="JupyterLab" \
    ML_RUNTIME_KERNEL="Python 3.11" \
    ML_RUNTIME_JUPYTER_KERNEL_GATEWAY_CMD="/usr/local/bin/jupyter kernelgateway" \
    ML_RUNTIME_JUPYTER_KERNEL_NAME="python3" \
    ML_RUNTIME_METADATA_VERSION="2" \
    ML_RUNTIME_SHORT_VERSION="2024.08"

# Set labels
LABEL com.cloudera.ml.runtime.edition=$ML_RUNTIME_EDITION \
    com.cloudera.ml.runtime.full-version=$ML_RUNTIME_FULL_VERSION \
    com.cloudera.ml.runtime.short-version=$ML_RUNTIME_SHORT_VERSION \
    com.cloudera.ml.runtime.maintenance-version=$ML_RUNTIME_MAINTENANCE_VERSION \
    com.cloudera.ml.runtime.description=$ML_RUNTIME_DESCRIPTION \
    com.cloudera.ml.runtime.editor=$ML_RUNTIME_EDITOR \
    com.cloudera.ml.runtime.kernel=$ML_RUNTIME_KERNEL \
    com.cloudera.ml.runtime.runtime-metadata-version=$ML_RUNTIME_METADATA_VERSION \
    com.cloudera.ml.runtime.short-version=$ML_RUNTIME_SHORT_VERSION \
    authors="Cloudera"
