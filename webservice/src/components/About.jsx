import React from 'react';
import './About.css';
import imgNos from './imgs/nos.png';

import Card from 'react-bootstrap/Card';
import { CardGroup } from 'reactstrap';

function About() {
  return (
    <CardGroup className='card-group' style={{ height: "100%", fontWeight: '500', marginBlock: '2rem' }}>
      <div className="row" style={{ backgroundColor: 'transparent', margin: '3rem 0 3rem 0' }} >
        <Card text='white' style={{ paddingLeft: '2rem' }} >
          <Card.Title style={{ width: '100%' }}>Sobre a BCD Predict</Card.Title>
          <Card.Body style={{ width: '100%' }}>
            <Card.Text >
              BCD Predict é uma empresa focada em trazer informações e previsões para empresas, auxiliando na gestão através de IAs precisas.
            </Card.Text>
            <Card.Text style={{ marginTop: '1rem' }} >
              Utilizando o modelo de regressão com IA, é possível conseguir previsões de até 99% de precisão de informações úteis para uma empresa, como a venda dos próximos dias, necessidade de estoque, quais clientes terão mais chance de comprar determinados produtos e muitas outras coisas.
            </Card.Text>
          </Card.Body>
        </Card>
      </div>
      <Card text='white' style={{ paddingLeft: '2rem', }} >
        <Card.Title style={{ width: '100%' }} >Sobre os membros da BCD Predict</Card.Title>
        <Card.Body >
          <Card.Text>
            A BCD Predict é formado pelos alunos, Bruno Calura, Cleiver Batista e Daniel Rios (da direita para a esquerda na imagem ao lado), do Bacharelado em Inteligência Artificial(BIA) da Universidade Federal de Goiás(UFG). O grupo foi feito para a realização do trabalho de Introdução à Programação(IP) no 1° período curso. Os membros receberam orientações do Prof. Leonardo Alves para a execução do projeto.
          </Card.Text>
          <Card.Text style={{ margin: '1rem 0 0.4rem 0', fontWeight: '600' }}>
            cleiver@discente.ufg.br
          </Card.Text>
          <Card.Text style={{ margin: '0 0 0.4rem 0', fontWeight: '600' }}>
            brunocalura@discente.ufg.br
          </Card.Text>
          <Card.Text style={{ margin: '0 0 0.4rem 0', fontWeight: '600' }}>
            daniel.rios@discente.ufg.br
          </Card.Text>
        </Card.Body>

          

      </Card>
      <Card style={{ paddingRight: '2rem', paddingLeft: '2rem', width: '100%', height: '50%', marginBottom: '2rem' }}>
        <img className='imagem' src={imgNos} alt='' />
      </Card>

    </CardGroup>

  )
}

export default About