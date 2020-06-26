const express = require('express');
const router = express.Router();
const models = require('../models');

router.get('/', (req, res) => {
    models.Usuario.findAll()
        .then((rows) => {
            res.send(rows);
        });
});

router.get('/:id', (req, res) => {
    let id = req.params.id;

    models.Usuario.findOne({
        where: {
            id: id
        }
    })
        .then((row) => {
            res.send(row);
        });
});

router.post('/', (req, res) => {
    let nombre = req.body.nombre;
    let apellido = req.body.apellido;
    let usuario = req.body.usuario;
    let peso = req.body.peso;
    let altura = req.body.altura;
    let edad = req.body.edad;
    let mail = req.body.mail;
    let menu = req.body.menu;
    let contraseña = req.body.contraseña;



    models.Usuario.

    models.Usuario.findOne({
        where: {
            nombre: nombre,
            apellido: apellido,
            mail: mail
        }
    }).then((usuario){
        res.sendStatus(403)
    }).catch()


    models.Usuario.create({
        nombre: nombre,
        apellido: apellido,
        usuario: usuario,
        peso: peso,
        altura: altura,
        edad: edad,
        mail: mail,
        menu: menu,
        contraseña: contraseña
    }).then(() => {
        res.sendStatus(201)
    })



    models.Comidas.findOne({
        where: {
            id: menu
        }
    })
        .then((departamento) => {
            models.Usuario.create({
                nombre: nombre,
                apellido: apellido,
                edad: edad
            }).then((cliente) => {

                cliente.setDepartamento(departamento);

                res.sendStatus(201);
            })
        })
});

router.put('/:id', (req, res) => {
    let id = req.params.id;
    let nombre = req.body.nombre;
    let apellido = req.body.apellido;
    let edad = req.body.edad;

    models.Usuario.update(
        {
            nombre: nombre,
            apellido: apellido,
            edad: edad
        },
        {
            where: { id: id }
        }
    ).then(() => {
        res.sendStatus(200);
    })
});

router.delete('/:id', (req, res) => {
    let id = req.params.id;

    models.Usuario.destroy({
        where: {
            id: id
        }
    }).then(() => {
        res.sendStatus(200);
    })
});

module.exports = router;