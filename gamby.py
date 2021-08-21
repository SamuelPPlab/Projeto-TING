from ting_file_management.file_process import process
from ting_file_management.queue import Queue


if __name__ == "__main__":
    fila = Queue()
    print(process("statics/arquivo_teste.txt", fila))
