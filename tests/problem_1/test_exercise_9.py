import os

import pytest

from src.problem_1.exercise_9 import FilesManager, AudioFilesManager


def test_files_manager_list_files(tmp_directory, capsys):
    """
    Test exercise_9.FilesManager list_files method
    GIVEN a FilesManager instance with files created,
    WHEN the list_files method is called,
    THEN it should print the names of all files in the directory.
    """
    manager = FilesManager(tmp_directory)
    manager.create_file("file1.txt")
    manager.create_file("file2.txt")
    manager.list_files()
    captured = capsys.readouterr()
    assert captured.out == "file1.txt\nfile2.txt\n"


def test_files_manager_create_file(tmp_directory):
    """
    Test exercise_9.FilesManager create_file method.
    GIVEN a FilesManager instance,
    WHEN the create_file method is called with the name of a new file,
    THEN it should create the file in the directory.
    """
    manager = FilesManager(tmp_directory)
    manager.create_file("test_file.txt")
    assert os.path.exists(os.path.join(tmp_directory, "test_file.txt"))


def test_files_manager_delete_file(tmp_directory):
    """
    Test exercise_9.FilesManager delete_file method.
    GIVEN a FilesManager instance with a file created,
    WHEN the delete_file method is called with the name of the created file,
    THEN it should delete the file from the directory.
    """
    manager = FilesManager(tmp_directory)
    manager.create_file("test_file.txt")
    manager.delete_file("test_file.txt")
    with pytest.raises(FileNotFoundError):
        manager.delete_file("this_doest_exists.top")
    assert not os.path.exists(os.path.join(tmp_directory, "test_file.txt"))


# Test AudioFilesManager class
def test_audio_files_manager_list_files(tmp_directory, capsys):
    """
    Test exercise_9.AudioFilesManager list_files method.

    GIVEN an AudioFilesManager instance with audio files created,
    WHEN the list_files method is called,
    THEN it should print the names of all audio files (.mp3 and .wav) in the directory.
    """
    manager = AudioFilesManager(tmp_directory)
    manager.create_file("audio1.mp3")
    manager.create_file("audio2.wav")
    with pytest.raises(ValueError):
        manager.create_file("text_file.txt")
    manager.list_files()
    captured = capsys.readouterr()
    assert captured.out == "audio1.mp3\naudio2.wav\n"


def test_audio_files_manager_create_file_supported_format(tmp_directory):
    """
    Test exercise_9.AudioFilesManager create_file method with supported file format.

    GIVEN an AudioFilesManager instance,
    WHEN the create_file method is called with the name of a file with a supported format,
    THEN it should create the file in the directory.
    """
    manager = AudioFilesManager(tmp_directory)
    manager.create_file("audio.mp3")
    assert os.path.exists(os.path.join(tmp_directory, "audio.mp3"))


def test_audio_files_manager_create_file_unsupported_format(tmp_directory):
    """
    Test exercise_9.AudioFilesManager create_file method with unsupported file format.

    GIVEN an AudioFilesManager instance,
    WHEN the create_file method is called with the name of a file with an unsupported format,
    THEN it should raise a TypeError.
    """
    manager = AudioFilesManager(tmp_directory)
    with pytest.raises(ValueError):
        manager.create_file("text_file.txt")


def test_audio_files_manager_delete_file_supported_format(tmp_directory):
    """
    Test exercise_9.AudioFilesManager delete_file method with supported file format.

    GIVEN an AudioFilesManager instance with an audio file created,
    WHEN the delete_file method is called with the name of the created file,
    THEN it should delete the file from the directory.
    """
    manager = AudioFilesManager(tmp_directory)
    manager.create_file("audio.mp3")
    manager.delete_file("audio.mp3")
    assert not os.path.exists(os.path.join(tmp_directory, "audio.mp3"))


def test_audio_files_manager_delete_file_unsupported_format(tmp_directory):
    """
    Test exercise_9.AudioFilesManager delete_file method with unsupported file format.

    GIVEN an AudioFilesManager instance,
    WHEN the delete_file method is called with the name of a file with an unsupported format,
    THEN it should raise a ValueError.
    """
    manager = AudioFilesManager(tmp_directory)
    with pytest.raises(ValueError):
        manager.create_file("text_file.txt")
    with pytest.raises(ValueError):
        manager.delete_file("text_file.txt")
