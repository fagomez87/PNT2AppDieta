const Sequelize = require('sequelize');
const Usuario = require('./Usuario');
const Comidas = require('./Comidas');

let db = {};

// const sequelize = new Sequelize('mainDb', null, null, {
//     dialect: "sqlite",
//     storage: "./mainDB.sqlite"
// });

const sequelize = new Sequelize('', 'dietasapp', 'admindatabase', {
    dialect: 'mssql',
    dialectModulePath: 'tedious',
    dialectOptions: {
        driver: 'SQL Server Native Client 11.0',
        instanceName: 'SQLSERVER2017',
        trustedConnection: true,
        encrypt: true
    },
    host: 'localhost',
    database: 'dietasapp'
});

sequelize.authenticate()
    .then(function () { console.log('Autenticado'); })
    .catch(function (err) { console.log('Error autenticando: ' + err); })

db.Usuario = Usuario(sequelize, Sequelize);
db.Comidas = Comidas(sequelize, Sequelize);

db.Usuario.belongsTo(db.Comidas);
db.Comidas.belongsTo(db.Usuario);

sequelize.sync({ force: true })
    .then(function (err) {
        console.log('Modelo sincronizado.');
    });

module.exports = db;