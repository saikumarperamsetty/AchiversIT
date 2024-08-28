import React, { useEffect, useState } from 'react'
import { products } from '../../Assets/Images/products'

const NewArrivals = () => {

    const[arrivals, setArrivals] = useState([]);

    useEffect(()=>{
        getArrivals();
    },[]);

    let getArrivals = ()=>{
        let temp = products.filter((test)=>{
            return test.category === 'mobile' || test.category === 'wireless';
        })
        setArrivals(temp);
    }

    // for New Arrivals
  return (
    <div className='container mt-4 mb-4' style={{backgroundColor:'white'}}>
        <h2 className='text-center p-4'>New Arrivals</h2>
      <div className="row g-2 d-flex justify-content-center">
        {
            arrivals.map((items)=>(
                <div className="col-md-4">
            <div className="card" style={{height:'100%'}}>
                <div className='card-body d-flex justify-content-center'>
                    <img src={items.imgUrl} className='img-fluid' alt={items.id} style={{height:'12rem'}}/>
                </div>
                <div className="card-title">
                    <h6 className='ms-4 p-1'>{items.productName}</h6>
                    <span className='ms-4'>
                        <i className='bi bi-star-fill' style={{color:'#ffcd4e'}}></i>
                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                    </span>
                </div>
                <div className="d-flex justify-content-between align-items-center m-2">
                    <h6 className='ms-2 p-2'>${items.price}</h6>
                    <button style={{border:'0px',borderRadius:'50%', height:'40px',width:'40px',paddingBottom:'10px',fontSize:'25px'}}>+</button>
                </div>
            </div>
        </div>
            ))
        }
      </div>
    </div>
  )
}

export default NewArrivals
