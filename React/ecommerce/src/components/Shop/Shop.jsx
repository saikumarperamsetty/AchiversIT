import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
// import useDispatch from 'react-router-dom'
import cover from '../../Assets/Images/cover.jpg'
import { products } from '../../Assets/Images/products'
// import toast from 'react-router-dom'
const Shop = () => {

    const [coverHeading, setCoverHeading] = useState('product');

    // const dispatch = useDispatch();

    let forSofaProducts = products.filter((input)=>{
        return input.category === 'sofa';
    })

    const [productCategory,setProductCategory] = useState(forSofaProducts);

    let linkButtonHandler = (category)=>{
        let getItems = products.filter((temp)=>{
            return temp.category === category;
        })
        setProductCategory(getItems);
        setCoverHeading(category);
    }

        const handleSubmit = (e)=>{
            e.preventDefault();
            let getDropdownItems = products.filter((item)=>{
                return item.category === e.target[0].value;
            })
            if(getDropdownItems){
                setProductCategory(getDropdownItems);
                setCoverHeading(e.target[0].value);
            }
            else
            setProductCategory([]);
        }

        // let buttonHandler = ()=>{
        //     toast.success('Product has been added to Cart!')
        // }
  return (
    <>
    <div className="position-relative">
        <img src={cover} alt="cover" style={{width:'100%',height:'25vh',filter:'brightness(40%)'}}/>
        <h3 className='position-absolute start-50 top-50 translate-middle text-white' style={{zIndex:2}}>{coverHeading}</h3>
    </div>

<div className="container mt-4 mb-4">
    {/* For dropdown and search bar */}
    <div className="row mt-4 mb-4">

        <div className="col-md-4 mt-2">

            <div className="dropdown">
                <button className='btn dropdown-toggle' type='button' data-bs-toggle='dropdown' aria-expanded='false' style={{backgroundColor:'#0f3460',color:'white'}}>fitered by Category</button>
            
            <ul className="dropdown-menu">
                    <li><Link className='dropdown-item' onClick={()=>linkButtonHandler('sofa')}>Sofa</Link></li>
                    <li><Link className='dropdown-item' onClick={()=>linkButtonHandler('chair')}>Chair</Link></li>
                    <li><Link className='dropdown-item' onClick={()=>linkButtonHandler('watch')}>Watch</Link></li>
                    <li><Link className='dropdown-item' onClick={()=>linkButtonHandler('mobile')}>Mobile</Link></li>
                    <li><Link className='dropdown-item' onClick={()=>linkButtonHandler('wireless')}>Wireless</Link></li>
            </ul>
            
            <div className="col-md-8 mt-2">
                <form className='d-flex' role='search' onSubmit={handleSubmit}>
                    <input className='form-control' type="search" placeholder='Search'/>
                    <button type='submit' style={{border:'0px'}}><i className='bi bi-search p-2 ms-2'></i></button>
                </form>
            </div>

            </div>
        </div>
    </div>
</div>
                {/* for Every product */}
            <div className="container mt-4 mb-4">
                <div className="row g-2 d-flex justify-content-center">
                    {
                        productCategory.length > 0 ? (
                        productCategory.map((items)=>(
                            <div className="col-md-4">
                            <div className="card" style={{height:'100%'}}>
                                <div className="card-body">
                                <Link to={`/product/${items.id}`}>
                                <div className='card-img-top d-flex justify-content-center'>
                                    <img src={items.imgUrl} className='card-img-top w-75' alt={items.id} style={{height:'12rem'}}/>
                                </div>
                                </Link>
                                </div>

                                <div className="card-title">
                                    <h6 className='card-title ms-4'>{items.productName}</h6>
                                    <span className='d-flex mt-4 mb-4 ms-4'>
                                        <i className='bi bi-star-fill' style={{color:'#ffcd4e'}}></i>
                                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                                        <i className='bi bi-star-fill ms-1' style={{color:'#ffcd4e'}}></i>
                                    </span>
                                </div>

                                <div className="d-flex justify-content-between align-items-center">
                                    <h6 className='ms-4'>${items.price}</h6>
                                    <button className='me-2 mb-2' style={{border:'0px',borderRadius:'50%',width:'40px',height:'40px',fontSize:'25px',paddingBottom:'4px'}}>+</button>
                                </div>
                            </div>
                        </div>
                        ))
                    ) : (
                        <div className="col bg-light text-center">
                            <h3>product not Found!</h3>
                        </div>
                    )}
                </div>
          </div>
    </>
  )
}

export default Shop
