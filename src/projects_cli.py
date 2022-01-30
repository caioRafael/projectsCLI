import os
import argparse

user = os.getlogin()
path = f'/home/{user}/Área\ de\ Trabalho'

class ProjectsCLI:
    CLI_VERSION = "1.0.0"
    INI_FILE = "projects.ini"


    def __init__(self):
        self.__run()


    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog="project",
            description="Automação para a criação de projetos pessoais(React, node, python e outras linguagens)",
            epilog="Desenvolvido por: Caio Rafael",
            usage="%(prog)s [options]")

        self.parser.version = self.CLI_VERSION
        self.parser.add_argument("-v", "--version", action="version")

        parser_args = self.parser.parse_args()

        # if parser_args:
        #     if parser_args.teste:
        #         print("teste de execução")