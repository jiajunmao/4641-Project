import React, { useEffect } from 'react'
import Layout from './Layout'
import './Components/Styles/main.scss'
let resizeEvent = new Event('resize');

function update() {
  window.dispatchEvent(resizeEvent);
}
let App = () => {
    useEffect(() => {
        update()
       });
    return(<Layout />);}
export default App
