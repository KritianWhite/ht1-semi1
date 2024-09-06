// app.js
const express = require('express');
const app = express();

// Endpoint 1: /check
app.get('/check', (req, res) => {
    res.status(200).send('Status: OK');
});

// Endpoint 2: /
app.get('/', (req, res) => {
    const data = {
        Instancia: 'Instancia #1 - API 1',
        Curso: 'Seminario de Sistemas 1',
        Seccion: 'Seccion A',
        Periodo: '2do Semestre 2024',
        Estudiante: 'Christian Blanco - 202000173',
    };
    res.json(data);
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`API 1 is running on port ${port}`);
});
