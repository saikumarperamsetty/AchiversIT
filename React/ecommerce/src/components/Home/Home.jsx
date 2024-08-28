import React from 'react'
import Header from '../Header/Header'
import Carousel from './Carousel'
import ServiceData from './ServiceData'
import BigDiscount from './BigDiscount'
import NewArrivals from './NewArrivals'
import BestSales from './BestSales'
import Footer from '../Footer/Footer'

const Home = () => {
  return (
    <div>
      <Header/>
      <Carousel/>
      <ServiceData/>
      <BigDiscount/>
      <NewArrivals/>
      <BestSales/>
      <Footer/>
    </div>
  )
}

export default Home
