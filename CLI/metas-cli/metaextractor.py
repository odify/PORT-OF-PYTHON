#!/usr/local/bin/python3
from colored import stylize, fg
from PIL import Image
from PIL.ExifTags import TAGS


# EXTRACT METADATA FROM IMG



class Metadata:
    def __init__(self, file):
        self.file = file

    def __repr__(self):
        metadata = self.extract_metadata(self.file)
        if len(metadata) == 0:
            return stylize(f"\n{self.file} No metadata.\n", fg("red"))
        else:
            print(stylize(f"\nMetadata of {self.file}:\n", fg("red")))
            for data in metadata:
                print(data)
            return ""

    def extract_metadata(self, file):

        image = Image.open(file)


        exifdata = image.getexif()

        metadata = []

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)

            if isinstance(data, bytes):
                data = data.decode()

            metadata.append(f"{tag:25}: {data}")

        return metadata


if __name__ == "__main__":
    filename = input("Filename: ")

    print(Metadata(filename))
