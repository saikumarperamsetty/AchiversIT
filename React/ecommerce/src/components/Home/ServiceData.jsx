import React from 'react'
import { serviceData } from '../../Assets/Images/products'

const ServiceData = () => {
  return (
    <div className="container mt-4 mb-4">
        <div className="row g-3">
            {
                serviceData.map((item)=>(
                    <div className="col-md-3 mb-3 mb-md-0">
                        <div className="card text-center" style={{backgroundColor:item.bg}}>
                            <div className="card-body">
                                <span className="bg-light p-2 rounded-circle text-center">{item.icon}</span>
                                <h5 className='card-title m-3'>{item.title}</h5>
                                <p className='card-text m-3'>{item.subtitle}</p>
                            </div>
                        </div>
                    </div>
                ))
            }
        </div>
    </div>
  )
}

export default ServiceData
