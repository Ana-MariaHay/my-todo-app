import zipfile


def extract_archive(archivep, dest_dir):
    with zipfile.ZipFile(archivep, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:/compressed.zip",
                          "C:/dest")
