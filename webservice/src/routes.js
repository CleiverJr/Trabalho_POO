import { Route, Routes} from "react-router-dom"

import Main from './components/Main';
import About from './components/About';
import Plan from './components/Plan';
import Predict from './components/Predict';


export const RoutesApp = () => {
    return (
        <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/about" element={<About />} />
            <Route path="/plans" element={<Plan />} />
            <Route path="/predict" element={<Predict />} />
        </Routes>
    )
}