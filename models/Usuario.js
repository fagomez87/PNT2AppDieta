module.exports = (sequelize, Sequelize) => {

    let Usuario = sequelize.define('Usuario', {
        nombre: Sequelize.STRING,
        apellido: Sequelize.STRING,
        usuario: Sequelize.STRING,
        peso: Sequelize.INTEGER,
        altura: Sequelize.INTEGER,
        edad: Sequelize.INTEGER,
        mail: Sequelize.STRING,
        menu: Sequelize.STRING,
        contraseña: Sequelize.STRING

    });

    return Usuario;
};