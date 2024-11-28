import React, { createContext, useState, useEffect } from 'react';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [loggedIn, setLoggedIn] = useState(false);
    const [userName, setUserName] = useState('');

    useEffect(() => {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            const user = JSON.parse(storedUser);
            setLoggedIn(true);
            setUserName(user.name);
        }
    }, []);

    const login = (name) => {
        setLoggedIn(true);
        setUserName(name);
        localStorage.setItem('user', JSON.stringify({ name }));
    };

    const logout = () => {
        setLoggedIn(false);
        setUserName('');
        localStorage.removeItem('user');
    };

    return (
        <AuthContext.Provider value={{ loggedIn, userName, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export { AuthContext, AuthProvider };