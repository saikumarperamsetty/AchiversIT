import React, { useEffect, useState } from 'react'
import { products } from '../../Assets/Images/products'
import { Link, useParams } from 'react-router-dom'
// import { toast } from 'react-toastify';
// import { useDispatch } from 'react-redux'
// import { addToCart } from '../../redux/productAction/ProductAction'
import cover from '../../Assets/Images/cover.jpg'

const Product = () => {
    
    let {id} = useParams();

    // const dispatch = useDispatch();

    const [product,setProduct] = useState({});
    const [like, setLike] = useState([]);
    const [review,setReview] = useState([]);
    const [coverHeading, setCoverHeading] = useState('productName');

    useEffect(()=>{
        window.scrollTo(0,150);     //for Scoll top off every product
        getItem();
    },id);

    let getItem = ()=>{

        let inputData = products.find((item)=>{
            return item.id === id;
        })
        setProduct(inputData);
        setReview(inputData.reviews);
        setCoverHeading(getItem.productName);

        let mightLike = products.filter((item)=>{
                return item.category === inputData.category && item.id !== inputData.id;
        })
        // console.log(mightLike);
        
        setLike(mightLike);
    }

    let handleSubmit = (e)=>{
        e.preventDefault();
        // toast.success('Item added to Cart!');
      }
  
      let buttonHandler = () => {
        // toast.success("Item added to Cart!");
      }
  return (
    <>
    {/*Cover Photo */}
    <div className="position-relative">
        <img src={cover} alt='cover' className='w-100' style={{height: '25vh', filter: 'brightness(40%)'}} />
        <h3 className="position-absolute top-50 start-50 translate-middle text-light" style={{ zIndex: 2 }}>{product.productName}</h3>
      </div>

     {/* For Single Product info */}
    <div className='container'>
      <div className="row">

        <div className="col-md-6 mt-2">
            <img src={product.imgUrl} className='img-fluid' alt={product.productName}/>
        </div>

        <div className="col-md-6 mt-2">
            <h3 className='pt-4'>{product.productName}</h3>
            <div className='mt-4 mb-4'>
                <i className='bi bi-star-fill' style={{color:'#ffcd4e'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                <span className='ms-4 text-secondary'>{product.avgRating} ratings</span>
            </div>
            <div className='mt-3'>
                <h5 className='p-2'>$ {product.price}<span className='ms-4 text-muted'>category:{product.category}</span></h5>
                <p className='mt-3'>{product.shortDesc}</p>
            </div>
            {/* <form className='mt-3'> */}
            <form className='mt-4' onSubmit={handleSubmit}>
            <input type="text" className='form-control' style={{ width: '100px' }}></input>
            <button className='btn mt-3'type='submit' style={{ backgroundColor: '#0f3460', color: 'white' }}>Add To Cart</button>
            </form>
        </div>
</div>
            {/* Description */}
            <div className='row mt-3 mb-4'>
                <h6>Description 
                    <Link className='text-decoration-none' data-bs-toggle='collapse' data-bs-target='#example'>
                        <span className='ms-4 text-muted'>Reviews ({review.length})</span>
                    </Link>
                </h6>

                <div class='collapse' id='example'>
                    {
                        review.map((index)=>(
                            <div className='mt-2 mb-3'>
                                <p>John Doe 
                                    <br />
                                    <span className='text-warning'>{index.rating} (rating)</span>
                                    <br/>
                                    {index.text}</p>
                            </div>
                        ))
                    }
                </div>
                <p>{product.description}</p>
            </div>
            
            {/* You might also like */}
                <h3 className='ms-0 mt-4 mb-4'>You might also like</h3>
                <div className="row g-2 d-flex justify-content-center">
              {
                    like.map((items)=>(

                <div className="col-md-4">
                    <div className="card" style={{height:'100%'}}>

                    <div className="card-body">
                    <Link to={`/product/${items.id}`}>
                        <div className='card-img-top d-flex justify-content-center'>
                            <img src={items.imgUrl} className="card-img-top w-75" alt={items.productName} style={{height:'12rem'}}/>
                        </div>
                    </Link>
                    </div>

                    <div className="card-title">
                    <h6 className='card-title ms-4'>{items.productName}</h6>
                    <span className='d-flex mt-4 mb-4 ms-4'>
                        <i className="bi bi-star-fill" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill ms-1" style={{color:'#ffcd4e'}}></i>
                    </span>
                    </div>

                    <div className='d-flex justify-content-between m-2'>
                        <h6 className='ms-4'>$ {items.price}</h6>
                        <button className='me-2 mb-2' style={{ border: '0px', borderRadius: '50%', width: '40px', height: '40px', paddingBottom: '4px', fontSize:'25px' }}>+</button>
                    </div>
                    </div>
                </div>
               ))
            }

        </div>
    </div>
    </>
  )
}

export default Product
