from flask import Flask
app = Flask(__name__, template_folder='templates') 

from app import route
from app import cliente
from app import funcionario
from app import main