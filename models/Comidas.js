module.exports = (sequelize, Sequelize) => {

    let Comidas = sequelize.define('Comidas', {
        descripcion: Sequelize.STRING,
        calorias: Sequelize.INTEGER,
        categoria: Sequelize.STRING,
        tipoMenu: Sequelize.STRING
    });

    return Comidas;
};