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

        subparser = self.parser.add_subparsers(help="Ações Projeto")

        self.__create_project_parser(subparser)

        parser_args = self.parser.parse_args()

        if parser_args: 
            if parser_args.node:
                self.__create_node_project()
                print("ola")
                
    def __create_project_parser(self, subparser):
        self.project_parser = subparser.add_parser("projeto", help="Gerar projeto")
        self.project_parser.add_argument("--node", "-n", help="gerador de projeto Node.JS", action="store_true", required=False)

    def __create_node_project(self):
        os.system(f"mkdir {path}/teste")
        os.system(f"cd {path}/teste && yarn init -y && ls")


