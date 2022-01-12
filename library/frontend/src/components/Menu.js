import React from 'react';

const MenuItem = ({item}) => {
    return (
        <li><a href="{item.url}">{item.name}</a></li>
    )
}

const MenuItemList = ({menu}) => {
    return (
        <ul>
            {menu.map((item) => <MenuItem item={item} />)}
        </ul>
    )
}

export default MenuItemList;