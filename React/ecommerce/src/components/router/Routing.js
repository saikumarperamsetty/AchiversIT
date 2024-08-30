import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from '../Home/Home'
import Product from '../Product/Product'
import Shop from '../Shop/Shop'

const Routing = () => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/product/:id' element={<Product/>}/>
        <Route path='/shop' element={<Shop/>}/>
      </Routes>
    </div>
  )
}

export default Routing
