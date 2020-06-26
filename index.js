const express = require('express');
const bodyParser = require('body-parser');

const routeDepartamentos = require('./routes/departamentos');
const routerUsuarios = require('./routes/usuarios');

const db = require('./models');

const app = express();

app.use(bodyParser.json());
app.use('/departamentos', routeDepartamentos);
app.use('/usuario', routerUsuarios);

app.listen(port=5000, () => {
    console.log('Servidor escuchando...');
});