import React from 'react';
import { Link } from 'react-router-dom'

const MenuItem = ({item}) => {
    return (
        <li><Link to="{item.url}">{item.name}</Link></li>
    )
}

const MenuItemList = ({menu}) => {
    return (
        <nav>
            <ul>
                {menu.map((item) => <MenuItem item={item} />)}
            </ul>
        </nav>
    )
}

export default MenuItemList;