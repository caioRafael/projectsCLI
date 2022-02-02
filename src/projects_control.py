import os

class ProjectsControl:
    user = os.getlogin()
    path = f'/home/{user}/Área\ de\ Trabalho'
    
    def __init__(self):
        self.types_prjects = ['python', 'node-ts', 'node-js', 'react-ts', 'react-js']

    def createProject(self, type):
        if type in self.types_prjects:
            self.verifyTemplate(type)

    def verifyTemplate(self, template):
        if template == "node-ts":
            print("criando projeto node typescript...")
        if template == "node-js":
            print("criando projeto node javascript...")
        if template == "react-ts":
            print("criando projeto react typescript...")
        if template == "react-js":
            print("criando projeto react javascript...")