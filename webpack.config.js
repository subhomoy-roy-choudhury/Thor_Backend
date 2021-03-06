const path = require("path");
// const HtmlWebPackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./thor_controller/src/index.js",
  output: {
    path: path.resolve(__dirname, "./thor_controller/static/thor_controller"),
    filename: "[name].js",
  },
  stats: {
    errorDetails: true,
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
       {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader", "postcss-loader",
          ],
      },
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "styles.css",
      chunkFilename: "styles.css"
    }),
  //   new HtmlWebPackPlugin({
  //   template: "./src/index.html",
  //   filename: "./index.html"
  // }),
]
};