const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CopyWebpackPlugin = require("copy-webpack-plugin")

module.exports = {
    entry: './src/index.js',
    devtool: 'inline-source-map',
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html',
            title: 'Todo List',
            filename: 'index.html',
        }),
        
        new CopyWebpackPlugin({
            patterns: [
                {from: './src/img', to: 'img'},
                {from: './src/about.html', to: 'about.html'},
                {from: './src/contact.html', to: 'contact.html'},
                {from: './src/betting.html', to: 'betting.html'},
                {from: './src/index.html', to: 'index.html'},
                {from: './src/liveStream.html', to: 'liveStream.html'},
                {from: './src/server.py', to: 'server.py'},
                {from: './src/style.css', to: 'style.css'},
            ]
        })

    ],
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist'),
        assetModuleFilename: 'img/[name][ext]',
        clean: true
    },

    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.html$/,
                use: ['html-loader']
            },
            {
                test: /\.(png|svg|jpg)$/,
                type: 'asset/resource'
            }
        ]
    }
}