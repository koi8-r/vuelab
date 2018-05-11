'use strict' ;


const webpack = require('webpack') ;
const path = require('path') ;
const CopyWebpackPlugin = require('copy-webpack-plugin') ;


module.exports = {
    mode: 'development',
    entry: {
        'app': './app/app',
        'test': './app/test'
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'app/[name].js'
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.min.js',  // by default esm runtime does not include template compiler
            '@': path.join(__dirname, '.', '.')
        }
    },
    plugins: [
        new CopyWebpackPlugin([
            { from: './*.html', to: './[name].[ext]' },
        ]),
    ],
    module: {
        rules: [
            {
                test: /\.txt$/,
                use: {
                    loader: 'raw-loader'
                }
            },
            {
                test: /\.js$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['env'],
                        //presets: [['env', {'modules': false}], 'stage-3'],
                        plugins: ['syntax-dynamic-import']
                    }
                },
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpeg)$/,
                use: {
                    loader: 'file-loader',
                    options: {
                        name: '[path][name].[ext]',
                        outputPath: 'assets/',
                        publicPath: '../'
                    }
                }
            }
        ]
    }
}
