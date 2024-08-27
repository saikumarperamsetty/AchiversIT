import React from 'react'
import Header from '../Header/Header'
import Carousel from './Carousel'
import ServiceData from './ServiceData'
import BigDiscount from './BigDiscount'

const Home = () => {
  return (
    <div>
      <Header/>
      <Carousel/>
      <ServiceData/>
      <BigDiscount/>
    </div>
  )
}

export default Home
