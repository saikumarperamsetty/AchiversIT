import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import Routing from './components/router/Routing';
import Header from './components/Header/Header';


function App() {
  return (
    <>
        <Header/>
        <Routing/>
    </>
  );
}

export default App;
