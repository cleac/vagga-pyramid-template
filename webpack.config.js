module.exports = {
    entry: "./js/app.js",
    output: {
        path: './static/js',
        filename: 'main.js',
    },
    module: {
        loaders: [
            {
                test: /.\.js$/,
                loader: "babel-loader",
                exclude: /node_modules/,
            },
        ],
    },
    resolve: {
        "react":            __dirname + '/node_modules/react/dist/react-with-addons.js',
    },
}
