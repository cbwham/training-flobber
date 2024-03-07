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

## Edit Markdown

Example file is located in `root/index.md`.

## Let Flobber do the job

```shell
./flobber.py
local file: root/index.md
cloud root directory: az://cbwtrainingbackup/
writing: az://cbwtrainingbackup/root/index.md
```

## Work in progress ...
