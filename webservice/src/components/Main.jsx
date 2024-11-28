import React from 'react';
import './Main.css';
import imgMain from './imgs/main.jpg'

import Card from 'react-bootstrap/Card';
import { CardGroup } from 'reactstrap';
import Botao from './botao'


const Main = () => {
    return (   
        <CardGroup>
            <Card text='white' style={{ paddingLeft: '2rem' }} >
                <Card.Title >Previsões para o seu negócio</Card.Title>
                <Card.Body >
                    <Card.Text>
                        Previsões para o auxílio financeiro e administrativo para a sua empresa. Acesso a dados preditivos a partir de bancos de dados
                    </Card.Text>
                    <Botao href="/predict" size='sm' className='botao UIButton' style={{width: '100%', height:'2.3rem', fontSize:'1rem', marginTop:'1rem'}} >
                        Comece sua análise
                    </Botao >
                </Card.Body> 
            </Card>
            <Card style={{ paddingRight: '2rem', paddingLeft: '2rem', width: '100%', height: '50%'}}>
                <img className='imagem' src={imgMain} alt=''/>
            </Card>
            </CardGroup>
            
            
    )
}

export default Main