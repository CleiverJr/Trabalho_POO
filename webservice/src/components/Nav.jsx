import React, { useContext, useState } from 'react';
import './Nav.css';
import Botao from './botao';
import Logo from './imgs/BCD.png';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';

import { BrowserRouter } from "react-router-dom";
import { RoutesApp } from '../routes';
import { AuthContext } from '../AuthContext';

function MyVerticallyCenteredModal(props) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login } = useContext(AuthContext);

    const handleLogin = () => {
        const validCredentials = [
            { email: 'cleiver@discente.ufg.br', password: '12345', name: 'Cleiver' },
            { email: 'BCD@predict.com.br', password: '12345', name: 'BCD Predict' }
        ];

        const user = validCredentials.find(
            cred => cred.email === email && cred.password === password
        );

        if (user) {
            setError('');
            login(user.name);
            props.onHide();
        } else {
            setError('Email ou senha inválidos');
        }
    };

    return (
        <Modal
            {...props}
            size="md"
            aria-labelledby="contained-modal-title-vcenter"
            centered
        >
            <Modal.Header closeButton>
                <Modal.Title id="contained-modal-title-vcenter">
                    Fazer Login
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                {error && <div style={{ color: 'red' }}>{error}</div>}
                <Form className="modal-form">
                    <Form.Group className="mb-3" controlId="formEmail">
                        <Form.Label>Email</Form.Label>
                        <Form.Control
                            type="email"
                            placeholder="name@example.com"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            autoFocus
                        />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formPassword">
                        <Form.Label>Senha</Form.Label>
                        <Form.Control
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={props.onHide}>
                    Cancelar
                </Button>
                <Button variant="primary" onClick={handleLogin}>
                    Fazer Login
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

const NavB = () => {
    const [modalShow, setModalShow] = useState(false);
    const { loggedIn, userName, logout } = useContext(AuthContext);

    return (
        <BrowserRouter>
            <Navbar collapseOnSelect expand="md" className="bg-body-tertiary">
                <Container>
                    <Navbar.Brand href="/" style={{ paddingLeft: '3rem' }}>
                        <img className='logo d-inline-block align-top' src={Logo} alt='' width="55" /> BCD Predict
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link href="/predict">Previsão</Nav.Link>
                            <Nav.Link href="/about">Sobre</Nav.Link>
                            <Nav.Link href="/plans">Planos</Nav.Link>
                        </Nav>
                        <Nav> 
                            {loggedIn ? (
                                <>
                                    <Nav.Link>Bem vindo, {userName}</Nav.Link>
                                    <Button className='UIButton' onClick={logout}>
                                        Sair
                                    </Button>
                                </>
                            ) : (
                                <Nav.Link>
                                    <Botao className='UIButton' onClick={() => setModalShow(true)}>
                                        Login
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-arrow-right" viewBox="0 0 16 16">
                                            <path fillRule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8" />
                                        </svg>
                                    </Botao>
                                </Nav.Link>
                            )}
                        </Nav>
                    </Navbar.Collapse>
                    <MyVerticallyCenteredModal
                        show={modalShow}
                        onHide={() => setModalShow(false)}
                    />
                </Container>
            </Navbar>

            <RoutesApp />
        </BrowserRouter>
    );
}

export default NavB;
