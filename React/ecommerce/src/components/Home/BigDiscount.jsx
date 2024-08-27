import React from 'react'
import { discoutProducts } from '../../Assets/Images/products'

const BigDiscount = () => {
  return (
    <div className='container mb-4 mt-4' style={{backgroundColor:'#f6f9fc'}}>
      <h2 className="text-center p-4">Big Discount</h2>
      <div className="row g-2">
        {
        discoutProducts.map((items)=>(
            <div className="col-md-4">
            <div className="card" style={{height:'100%'}}>

                <div className='d-flex justify-content-between m-2'>
                <span className='p-2' style={{backgroundColor:'#0f3460',color:'white',borderRadius:'100px',fontSize:'13px'}}>{items.discount}% Off</span>
                <i class="bi bi-heart-fill" style={{color:'#0f3460'}}></i>
                </div>

                <div className="card-body d-flex justify-content-center">
                    <img src={items.imgUrl} alt={items.id} className='img-fluid' style={{height:'12rem'}}/>
                </div>
                <div className="card-title">
                <h6 className='ms-4 p-1'>{items.productName}</h6>
                <span className='ms-4'><i className="bi bi-star-fill" style={{color:'#ffcd4e'}}></i>
                <i className="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                <i className="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                <i class="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                <i class="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                </span>
                </div>
            <div className="d-flex justify-content-between align-items-center m-2">
                <h5 className='ms-2 p-2'>${items.price}</h5>
                <button style={{height:'40px', width:'40px', fontSize:'25px',border:'0px', borderRadius:'50%', paddingBottom:'10px'}}>+</button>
            </div>
        </div>
        </div>
        ))
}
      </div>
    </div>
  )
}

export default BigDiscount
