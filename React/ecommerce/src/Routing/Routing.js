import React from 'react'
import {Route, Routes} from 'react-router-dom'
import Home from '../components/Home/Home'
import Product from '../components/Product/Product'

const Routing = () => {
  return (
    <div>
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/product/:id' element={<Product/>}/>
    </Routes>
    </div>
  )
}

export default Routing
