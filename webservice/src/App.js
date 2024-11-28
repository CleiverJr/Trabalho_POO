import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import NavBar from './components/Nav';
import Container from 'react-bootstrap/Container';
import Main from './components/Main';
import About from './components/About';
import Plan from './components/Plan';
import Predict from './components/Predict';
import Login from './components/Login';


function App() {
  return (

    <div className="App">
      <header>

      </header>
      <body>
        <Container>
          <NavBar />
        </Container>
      </body>
    </div>


  );
}

export default App;
