import React from 'react'
import './Plan.css';

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';


function Plan() {
    return (
        <CardGroup className='card-group-plan'>
            <Card className='card-plan'>
                <Card.Body className='card-body-plan'>
                    <Card.Title className='card-title-plan'>Plano Semestral</Card.Title>
                    <Card.Text>
                        6 Meses com acesso a IA preditiva para ter mais informações da sua empresa
                    </Card.Text>
                    <Button variant="success">Assinar Plano</Button>
                </Card.Body>
            </Card>
            <Card className='card-plan'>
                <Card.Body className='card-body-plan'>
                    <Card.Title className='card-title-plan'>Plano Anual</Card.Title>
                    <Card.Text>
                        12 Meses com acesso a IA preditiva para ter mais informações da sua empresa
                    </Card.Text>
                    <Button variant="success">Assinar Plano</Button>
                </Card.Body>
            </Card>
            <Card className='card-plan'>
                <Card.Body className='card-body-plan'>
                    <Card.Title className='card-title-plan'>Plano Anual Personalizado</Card.Title>
                    <Card.Text>
                        12 Meses com acesso a IA preditiva personalizada para a sua empresa, com diversas informações adicionais
                    </Card.Text>
                    <Button variant="success">Assinar Plano</Button>
                </Card.Body>
            </Card>
        </CardGroup>
    )
}

export default Plan