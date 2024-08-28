import React from 'react'

//for Footer
const Footer = () => {
  return (
    <div style={{backgroundColor:'#0f3460'}}>

    <div className='container pt-2'>
    <div className="row m-4" style={{color:'white'}}>

        <div className="col-md-3">
            <h4><i className="bi bi-bag-fill"></i> Mart</h4>
            <p style={{color:'#6C757D'}}>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ducimus nulla commodi quis nesciunt nisi blanditiis, ullam iste velit dolorum minus, numquam repudiandae. Quis, aut beatae!</p>
        </div>

        <div className="col-md-3">
            <h5 className='ms-md-4'>About Us</h5>
            <ul className='ms-md-4' style={{listStyle:'none', padding:'0px', color:'#6C757D'}}>
                <li style={{padding:'2px 0px'}}>Careers</li>
                <li style={{padding:'2px 0px'}}>Our Stores</li>
                <li style={{padding:'2px 0px'}}>Our Cares</li>
                <li style={{padding:'2px 0px'}}>Terms & Conditions</li>
                <li style={{padding:'2px 0px'}}>Privacy Policy</li>
            </ul>
        </div>

        <div className="col-md-3">
            <h5>Customer Care</h5>
            <ul style={{listStyle:'none', padding:'0px', color:'#6C757D'}}>
                <li style={{padding:'2px 0px 2px 0px'}}>Help Center</li>
                <li style={{padding:'2px 0px 2px 0px'}}>How to Buy</li>
                <li style={{padding:'2px 0px 2px 0px'}}>Track Your Order</li>
                <li style={{padding:'2px 0px 2px 0px'}}>Corporate & Bulk Purchasing</li>
                <li style={{padding:'2px 0px 2px 0px'}}>Returns & Refunds</li>
            </ul>
        </div>
        <div className="col-md-3">
            <h5>Contact Us</h5>
            <ul style={{listStyle:'none', padding:'0px', color:'#6C757D'}}>
                <li style={{padding:'2px 0px 2px 0px'}}>28 Tank Bund North, Hyderabad, Telangana 560028, INDIA.</li>
                <li style={{padding:'2px 0px 2px 0px'}}>Email: saikumar.peramsetty77@gmail.com</li>
                <li style={{padding:'2px 0px 2px 0px'}}>Phone: +91 8374563391</li>
            </ul>
        </div>
    </div>
  </div>

</div>
  )
}

export default Footer
