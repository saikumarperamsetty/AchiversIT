import React from 'react'
import Header from '../Header/Header'
import Carousel from './Carousel'
import ServiceData from './ServiceData'
import BigDiscount from './BigDiscount'
import NewArrivals from './NewArrivals'
import BestSales from './BestSales'

const Home = () => {
  return (
    <div>
      <Header/>
      <Carousel/>
      <ServiceData/>
      <BigDiscount/>
      <NewArrivals/>
      <BestSales/>
    </div>
  )
}

export default Home
