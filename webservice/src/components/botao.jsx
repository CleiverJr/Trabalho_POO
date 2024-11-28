//Componente de Botão
import React from 'react';
import './botao.css';

import Button from 'react-bootstrap/Button';

const botao = ({ children, ...restProps }) => {
  return (
    <Button {...restProps}> {children} </Button> 
  )
}

export default botao