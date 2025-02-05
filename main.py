from retriever import Retriever
from generator import Generator

def main():
    # User input for file paths
    file_paths = input("Enter the paths of the files to process (comma-separated): ").split(',')
    file_paths = [path.strip() for path in file_paths]

    # Initialize the retriever and generator
    retriever = Retriever(data_source=[])
    retriever.load_files(file_paths)


if __name__ == "__main__":
    main()