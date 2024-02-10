import os


class FilesManager:
    def __init__(self, directory: str):
        self.directory = directory

    def list_files(self):
        """
        List all files in the directory.
        """
        files = os.listdir(self.directory)
        for file in files:
            print(file)

    def create_file(self, filename: str):
        """
        Create a new empty file.
        """
        filepath = os.path.join(self.directory, filename)
        with open(filepath, "w") as _:
            pass

    def delete_file(self, filename: str):
        """
        Delete a file.
        """
        filepath = os.path.join(self.directory, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            raise FileNotFoundError(f"The file '{filename}' does not exist.")


class AudioFilesManager(FilesManager):
    _audio_format_supported = (".mp3", ".wav")

    def is_file_format_supported(self, filename: str):
        return any(
            [
                filename.endswith(file_format)
                for file_format in self._audio_format_supported
            ]
        )

    def list_files(self):
        """
        List only audio files (.wav and .mp3) in the directory.
        """
        files = os.listdir(self.directory)
        for file in files:
            if self.is_file_format_supported(file):
                print(file)

    def create_file(self, filename: str):
        """
        Create a new empty file.
        """
        if self.is_file_format_supported(filename):
            super().create_file(filename)
        else:
            raise ValueError("File type not supported")

    def delete_file(self, filename: str):
        """
        Delete a file.
        """
        if self.is_file_format_supported(filename):
            super().delete_file(filename)
        else:
            raise ValueError("File type not supported")
