var path = require("path");

module.exports = {
    mode: "production",
    entry: "./src/Calcpad.Fable.fs.js",
    output: {
        path: path.join(__dirname, "../Calcpad.Web/www/build"),
        filename: "calcpad.js",
        libraryTarget: "var",
        library: "Calcpad"
    },
    module: {
    }
}
