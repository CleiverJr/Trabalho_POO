from flask import Flask
app = Flask(__name__, template_folder='view') 

from app import route
from app import cliente
from app import funcionario