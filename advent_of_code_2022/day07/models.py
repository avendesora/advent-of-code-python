from __future__ import annotations


class File:
    def __init__(self: File, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self: Directory, name: str, parent: Directory | None = None) -> None:
        self.name = name
        self.sub_directories: dict[str, Directory] = {}
        self.files: dict[str, File] = {}
        self.parent = parent
        self.total_size = 0

    def add_file(self: Directory, file_name: str, file_size: int) -> None:
        if file_name in self.files:
            return

        new_file = File(file_name, file_size)
        self.files[file_name] = new_file

    def add_directory(self: Directory, directory_name: str) -> None:
        if directory_name in self.sub_directories:
            return

        new_directory = Directory(directory_name, self)
        self.sub_directories[directory_name] = new_directory

    @property
    def full_name(self: Directory) -> str:
        return f"{self.parent.full_name}/{self.name}" if self.parent else self.name
