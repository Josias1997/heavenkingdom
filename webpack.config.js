const path = require('path');

module.exports = {
    entry: './hkmfrontend/src',
    output: {
        path: path.resolve(__dirname, "hkmfrontend/static/frontend/js/"),
        filename: "bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
        ],
    }
}