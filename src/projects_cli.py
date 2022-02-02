import os
import argparse
from projects_control import ProjectsControl

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
        self.parser.add_argument("-l","--list", help="lista os diretorios", action="store_true")

        subparser = self.parser.add_subparsers(help="Ações Projeto")

        self.__create_project_parser(subparser)

        parser_args = self.parser.parse_args()

        if parser_args: 
            self.__verify_arguments(parser_args)
                
    def __create_project_parser(self, subparser):
        self.project_parser = subparser.add_parser("create", help="criar um novo projeto")
        self.project_parser.add_argument("--name","-n", type=str, help="nome do projeto", required=False)
        self.project_parser.add_argument("--template", "-T",
                                    choices=['python', 'node-ts', 'node-js', 'react-ts', 'react-js'],
                                    help="template do projeto", 
                                    required=True)

    def __verify_arguments(self,parser_args):
        try:
            if parser_args.list:
                print("listar todos os projetos")
            elif parser_args.name:
                print("o novo projeto é %s" %(parser_args.name))
                if parser_args.template:
                    controll = ProjectsControl()
                    print("o template é %s" %parser_args.template)
                    controll.createProject(parser_args.template)
        except Exception as e:
            print("Argumento inválido: {}".format(e))