import os
from sys import path

class ProjectsControl:
    user = os.getlogin()
    path = f'/home/{user}/Área\ de\ Trabalho/projects'
    
    def __init__(self, name):
        self.types_prjects = ['node', 'react']
        self.name = name

    def createProject(self, type):
        if type in self.types_prjects:
            self.verifyTemplate(type)

    def verifyTemplate(self, template):
        if template == "node":
            print("criando projeto node...")
            self.createNode()
        if template == "react":
            print("criando projeto react...")
            self.createReact()

    def createNode(self):
        os.system(f'cd {self.path}/node '
        +f'&& mkdir {self.name} && cd {self.name} '
        +'&& yarn init -y' 
        +' && code .'
        )
    
    def createReact(self):
        os.system(f'cd {self.path}/react '
        +f'&& yarn create vite {self.name} --template react-ts' 
        +f'&& cd {self.name}'
        +' && yarn'
        +' && code .'
        )