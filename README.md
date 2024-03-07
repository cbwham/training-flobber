# Azure Storage - Backup

## Create Storage Account

Please read the [documentation](https://learn.microsoft.com/de-de/azure/storage/common/storage-account-create?tabs=azure-cli) first.

Example:

```shell
az storage account create --name trainingbackup --resource-group training-01_group --location germanywestcentral --sku Standard_GRS --kind StorageV2 --allow-blob-public-access true
```

## Install Python Packages

```shell
pip install -U -r requirements.txt
```

## Authentication using `cloudpathlib`

[Authentication](https://cloudpathlib.drivendata.org/stable/authentication/) needs to be setup first.

For simplicity `AZURE_STORAGE_CONNECTION_STRING` is used and needs to be set accordingly, example:

```shell
export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=cbwtrainingbackup;AccountKey=fUzVZavGVrlXR2VK4fQWP0c8XKwm/9473641GHhh3OBylmXAG5G5q34rXxSKMbX+z9gT2KwBRg6JJASt/Mf38A==;EndpointSuffix=core.windows.net"
```

> Note: [`direnv`](https://direnv.net/) is well suited to manage environments.

## Anonymous Blob Access

[Allow public access](https://learn.microsoft.com/de-de/azure/storage/blobs/anonymous-read-access-configure) to the blob's in the container if intended.

### Referencing Blob via URI

The uploaded file can be access via [`HTTPS`](https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata) i.e.:

https://cbwtrainingbackup.blob.core.windows.net/cbwtrainingbackup/root/index.html

## Edit Markdown

Example file is located in `root/index.html`.

## Let Flobber do the job

```shell
./flobber.py
local file: root/index.html
cloud root directory: az://cbwtrainingbackup/
writing: az://cbwtrainingbackup/root/index.html
```
