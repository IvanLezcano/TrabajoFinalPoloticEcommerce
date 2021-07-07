import React from 'react'
import { Producto } from './Producto';


export const ProductosFiltrados = (props) => {
    return (
        <div>
            {props.listaProductos.map(producto => (<Producto nombre={producto.nombre} url={producto.url} /> ) )     }      
       
        </div>
    )
}
