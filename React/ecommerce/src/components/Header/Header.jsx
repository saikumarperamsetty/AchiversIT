import React from 'react'
import logo from '../../Assets/Images/logo.png'
import { Link } from 'react-router-dom'

const Header = () => {
  return (
    <>
    <nav className='navbar navbar-expand-lg navbar-dark p-3 bg-light shadow rounded bg-white'>
    <div className='container-fluid'>
        <img src={logo} style={{height:'70px'}} alt="logo img" />
        <button className='navbar-toggler bg-dark' data-bs-toggle='collapse' data-bs-target='#navbarCollapse'>
            <span className='navbar-toggler-icon'></span>
        </button>
        <div className="collapse navbar-collapse" id='navbarCollapse'>
            <ul className='navbar-nav ms-auto'>

                <li className='nav-item me-4'>
                    <Link className='nav-link text-dark' to='/'>Home</Link>
                </li>

                <li className='nav-item me-4'>
                    <Link className='nav-link text-dark' to='/shop'>Shop</Link>
                </li>

                <li className='nav-item me-4'>
                    <Link className='nav-link text-dark' to='cart'>Cart</Link>
                </li>

                <li className="nav-item me-4">
                    <Link className='nav-link text-dark' to='/userIcon'><i className="bi bi-person-fill"></i></Link>
                </li>

                <div className="nav-item me-4">
                    <Link className='nav-link text-dark' to='/cartIcon'><i className="bi bi-cart-fill"></i>
                        <span className='bg-info p-1 position-absolute rounded-circle translate-middle text-center' style={{height:'25px', width:'25px', lineHeight:'18px'}}></span>
                    </Link>
                </div>
            </ul>
        </div>
    </div>
    </nav>
    </>
  )
}

export default Header
