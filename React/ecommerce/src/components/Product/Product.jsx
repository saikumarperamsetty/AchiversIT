import React, { useEffect, useState } from 'react'
import { products } from '../../Assets/Images/products'
import { Link, useParams } from 'react-router-dom'
import { products } from '../Images/products';
import { toast } from 'react-toastify';
import { useDispatch } from 'react-redux'
import { addToCart } from '../../redux/productAction/ProductAction'
import cover from '../Images/cover.jpg'

const Product = () => {
    
    let {id} = useParams();
    
      //for Scoll top off every product
      useEffect(()=>{
        window.scrollTo(0,150);
      },[id]);

    const dispatch = useDispatch();

    const [product,setProduct] = useState({});
    const [like, setLike] = useState([]);
    const [review,setReview] = useState([]);
    const [coverHeading, setCoverHeading] = useState('productName');
    useEffect(()=>{
        getData();
    },id);

    let getData = ()=>{
        let inputData = products.find((item)=>{
            return item.id === id;
        })
        setProduct(inputData);
        setReview(inputData.reviews);
        setCoverHeading(getItem.productName);

        let mightLike = products.filter((item)=>{
                return item.category === getItem.category && item.id !== getItem.id;
        })
        setLike(mightLike);
    }

    let handleSubmit = (e)=>{
        e.preventDefault();
        toast.success('Item added to Cart!');
      }
  
      let buttonHandler = () => {
        toast.success("Item added to Cart!");
      }
  return (
    <>
    {/*Cover Photo */}
    <div className="position-relative">
        <img src={cover} alt='cover' style={{ width: '100%', height: '25vh', filter: 'brightness(40%)' }} />
        <h3 className="position-absolute top-50 start-50 translate-middle text-white" style={{ zIndex: 2 }}>{coverHeading}</h3>
      </div>

     {/* For Single Product info */}
    <div className='container mt-4 mb-4' style={{color:'white'}}>
      <div className="row pt-4">
        <div className="col-md-6 mt-2">
            <img src={product.imgUrl} className='img-fluid' alt={product.id} />
        </div>
        <div className="col-md-6 mt-2">
            <h4>{product.productName}</h4>
            <span className='mt-3'>
                <i className='bi bi-star-fill' style={{color:'#ffcde4'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcde4'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcde4'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcde4'}}></i>
                <i className='bi bi-star-fill ms-1' style={{color:'#ffcde4'}}></i>
                <p className='ms-4'>{product.avgRating} ratings</p>
            </span>
            <div className='mt-3'>
                <h3 className='p-2'>${product.price}<span className='ms-4 text-muted'>category:{product.category}</span></h3>
                <p className='mt-3'>{product.shortDesc}</p>
            </div>
            <form className='mt-3' onSubmit={handleSubmit}>
            <input type="text" className='form-control' style={{width:'100px',height:'50px'}}/>
            <button className='btn px-2 py-2 mt-2' style={{backgroundImage:'#0f3460',color:'white'}} onClick={() => { dispatch(addToCart(product)) }}>Add To Cart</button>
            </form>

            <div className='row mt-3 mb-4'>
                <h6>Description 
                    <Link className='text-decoration-none' data-bs-toggle='collapse' data-bs-target='#example'>
                        <span className='ms-4 text-muted'>Reviews ({review.length})</span>
                    </Link>
                </h6>

                <div class='collapse' id='example'>
                    {
                        review.map((index)=>(
                            <div className='ms-2 mb-3'>
                                <p>John Doe 
                                    <br />
                                    <span className='text-warning'>{review.rating} (rating)</span>
                                    <br/>
                                    {index.text}
                                </p>
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
                            <img src={items.imgUrl} class="card-img-top w-75" alt={items.id} />
                        </div>
                    </Link>
                    </div>

                    <div className="card-title">
                    <h6 className='card-title m-2'>{items.productName}</h6>
                    <span className='d-flex mt-4 mb-4 m-2'>
                        <i className="bi bi-star-fill" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star-fill" style={{color:'#ffcd4e'}}></i>
                        <i className="bi bi-star"></i>
                    </span>
                    </div>

                    <div className='d-flex justify-content-between m-2'>
                        <h6>$ {items.price}</h6>
                        <button  style={{ border: '0px', borderRadius: '50%', width: '40px', height: '40px', paddingBottom: '4px', fontSize:'25px' }} onClick={() => { dispatch(addToCart(items)); buttonHandler() }}>+</button>
                    </div>
                    </div>
                </div>
               ))
            }

        </div>
        </div>
      </div>

    </div>
    </>
  )
}

export default Product
